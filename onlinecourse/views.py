from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Course, Enrollment, Question, Choice, Submission


# Home view - list all courses
def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'onlinecourse/index.html', context)


# Course detail view
def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)


# Enrollment view
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    
    # Check if user is already enrolled
    is_enrolled = Enrollment.objects.filter(user=user, course=course).exists()
    
    if not is_enrolled:
        # Create a new enrollment
        Enrollment.objects.create(
            user=user,
            course=course,
            date_enrolled=datetime.now().date(),
            mode='honor'
        )
        # Update course enrollment count
        course.total_enrollment += 1
        course.save()
    
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))


# Submit exam view
@login_required
def submit(request, course_id):
    # Get the current user and course
    user = request.user
    course = get_object_or_404(Course, pk=course_id)
    
    # Get or create the enrollment
    enrollment, created = Enrollment.objects.get_or_create(
        user=user,
        course=course,
        defaults={
            'date_enrolled': datetime.now().date(),
            'mode': 'honor'
        }
    )
    
    # Create a new submission
    submission = Submission.objects.create(enrollment=enrollment)
    
    # Get submitted choices from the form
    submitted_choices = []
    for key in request.POST:
        if key.startswith('choice_'):
            # Extract question_id from the key (e.g., 'choice_1' -> '1')
            question_id = key.split('_')[1]
            # Get all selected choice IDs for this question
            choice_ids = request.POST.getlist(key)
            for choice_id in choice_ids:
                submitted_choices.append(int(choice_id))
    
    # Add all selected choices to the submission
    if submitted_choices:
        submission.choices.set(submitted_choices)
    
    # Redirect to the exam result page
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', 
                                       args=(course.id, submission.id)))


# Show exam result view
@login_required
def show_exam_result(request, course_id, submission_id):
    # Get the course and submission
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Get all submitted choices
    submitted_choices = submission.choices.all()
    submitted_choice_ids = [choice.id for choice in submitted_choices]
    
    # Calculate the score
    total_score = 0
    max_score = 0
    
    # Get all questions for this course
    questions = Question.objects.filter(course=course)
    question_results = []
    
    for question in questions:
        max_score += question.grade_points
        
        # Get choices for this question that were submitted
        question_choices = question.choice_set.all()
        selected_ids = [choice.id for choice in question_choices 
                       if choice.id in submitted_choice_ids]
        
        # Check if the answer is correct using the is_get_score method
        is_correct = question.is_get_score(selected_ids)
        
        if is_correct:
            total_score += question.grade_points
        
        # Prepare result data for this question
        question_results.append({
            'question': question,
            'choices': question_choices,
            'selected_ids': selected_ids,
            'is_correct': is_correct
        })
    
    # Calculate percentage
    percentage = (total_score / max_score * 100) if max_score > 0 else 0
    
    # Determine if passed (70% or higher)
    passed = percentage >= 70
    
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'max_score': max_score,
        'percentage': round(percentage, 2),
        'passed': passed,
        'question_results': question_results,
        'submitted_choice_ids': submitted_choice_ids
    }
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
