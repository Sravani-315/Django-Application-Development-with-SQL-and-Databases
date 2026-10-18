from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline admin classes
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Admin class for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course', 'lesson', 'grade_points']
    list_filter = ['course', 'lesson']
    search_fields = ['question_text']


# Admin class for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    search_fields = ['title']


# Admin class for Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date', 'total_enrollment']
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Admin class for Instructor
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_time', 'total_learners']
    list_filter = ['full_time']
    search_fields = ['user__username']


# Admin class for Learner
class LearnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'occupation', 'social_link']
    list_filter = ['occupation']
    search_fields = ['user__username']


# Admin class for Choice
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'is_correct']
    list_filter = ['is_correct', 'question__course']
    search_fields = ['choice_text']


# Admin class for Submission
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'get_user', 'get_course']
    list_filter = ['enrollment__course']
    search_fields = ['enrollment__user__username']

    def get_user(self, obj):
        return obj.enrollment.user.username
    get_user.short_description = 'User'

    def get_course(self, obj):
        return obj.enrollment.course.name
    get_course.short_description = 'Course'


# Register models with admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
