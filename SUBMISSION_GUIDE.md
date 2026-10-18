# Final Project Submission Guide

## Project Overview
This Django Online Course Application includes all required features for the final project submission.

## Assignment Requirements Checklist

### ✅ Task 1: models.py (3 points)
**File Location**: `onlinecourse/models.py`

**Required Models Implemented**:
- ✅ Question model (with question_text, grade_points, course, lesson)
- ✅ Choice model (with choice_text, is_correct, question)
- ✅ Submission model (with enrollment, choices ManyToManyField)

**GitHub URL Format**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/onlinecourse/models.py`

---

### ✅ Task 2: admin.py (3 points)
**File Location**: `onlinecourse/admin.py`

**Required Components**:
- ✅ Seven imported classes: Course, Lesson, Instructor, Learner, Question, Choice, Submission
- ✅ QuestionInline class (StackedInline with extra=2)
- ✅ ChoiceInline class (StackedInline with extra=3)
- ✅ QuestionAdmin class (with ChoiceInline)
- ✅ LessonAdmin class (with QuestionInline)

**GitHub URL Format**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/onlinecourse/admin.py`

---

### ✅ Task 3: Admin Site Screenshot (1 point)
**Screenshot Required**: `03-admin-site.png`

**Steps to Create Screenshot**:
1. Run: `python manage.py migrate`
2. Run: `python manage.py createsuperuser`
3. Run: `python manage.py runserver`
4. Navigate to: `http://localhost:8000/admin/`
5. Login with superuser credentials
6. Take a screenshot showing:
   - Authentication and Authorization section
   - OnlineCourse section (with all models listed)
7. Save as: `03-admin-site.png`

---

### ✅ Task 4: course_details_bootstrap.html (2 points)
**File Location**: `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`

**Required Features**:
- ✅ Displays course name and description
- ✅ Lists all lessons using Django template tags ({% for %})
- ✅ Shows exam questions with choices
- ✅ Bootstrap 5 styling
- ✅ Form with CSRF token for submission

**GitHub URL Format**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html`

---

### ✅ Task 5: views.py (2 points)
**File Location**: `onlinecourse/views.py`

**Required Functions**:
- ✅ `submit()` function - handles exam submission
  - Creates Submission object
  - Extracts selected choices from POST data
  - Links choices to submission
  - Redirects to show_exam_result

- ✅ `show_exam_result()` function - displays exam results
  - Calculates score using Question.is_get_score()
  - Compares total_score with max_score
  - Determines pass/fail (70% threshold)
  - Renders result template with context

**GitHub URL Format**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/onlinecourse/views.py`

---

### ✅ Task 6: urls.py (2 points)
**File Location**: `onlinecourse/urls.py`

**Required URL Patterns**:
- ✅ `path('course/<int:course_id>/submit/', views.submit, name='submit')`
- ✅ `path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result')`

**GitHub URL Format**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/onlinecourse/urls.py`

---

### ✅ Task 7: Final Exam Screenshot (2 points)
**Screenshot Required**: `07-final.png`

**Steps to Create Screenshot**:
1. Set up the database and create sample data:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

2. Access admin panel and create:
   - A course
   - Lessons for the course
   - Questions for each lesson
   - Choices for each question (mark correct answers)

3. Take the exam:
   - Navigate to course details page
   - Select correct answers
   - Submit the exam

4. Capture screenshot showing:
   - ✅ "Congratulations!" message (for passed exam)
   - ✅ Score display (e.g., "8/10")
   - ✅ Percentage (must be ≥70%)
   - ✅ Detailed exam results with questions and answers

5. Save as: `07-final.png`

---

## How to Upload to GitHub

### Step 1: Create GitHub Repository
1. Go to https://github.com/
2. Click "New repository" or "+"
3. Name: `django-online-course-app` (or your preferred name)
4. Description: "Django Online Course Application with Exam Features - Final Project"
5. Select "Public" repository
6. DON'T initialize with README (we already have one)
7. Click "Create repository"

### Step 2: Push to GitHub
```bash
# Add GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify Files on GitHub
Visit your repository and confirm all files are uploaded:
- ✅ onlinecourse/models.py
- ✅ onlinecourse/admin.py
- ✅ onlinecourse/views.py
- ✅ onlinecourse/urls.py
- ✅ onlinecourse/templates/onlinecourse/course_details_bootstrap.html

### Step 4: Get GitHub URLs
For each required file, get the URL:
1. Navigate to the file on GitHub
2. Click the file name
3. Copy the URL from browser address bar
4. Format should be: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/path/to/file.py`

---

## Creating Test Data for Screenshots

### Using Django Admin
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Navigate to `http://localhost:8000/admin/` and create:

1. **Create a Course**:
   - Name: "Introduction to Python"
   - Description: "Learn Python programming from scratch"
   - Total enrollment: 0

2. **Create Lessons**:
   - Lesson 1: "Python Basics" (order: 1)
   - Lesson 2: "Data Structures" (order: 2)

3. **Create Questions with Choices**:
   
   **Question 1** (for Lesson 1):
   - Text: "What is Python?"
   - Grade points: 2
   - Choices:
     - "A programming language" ✅ (is_correct = True)
     - "A snake" ❌
     - "A framework" ❌

   **Question 2** (for Lesson 1):
   - Text: "Which keyword is used to define a function in Python?"
   - Grade points: 2
   - Choices:
     - "def" ✅ (is_correct = True)
     - "function" ❌
     - "define" ❌

   **Question 3** (for Lesson 2):
   - Text: "Which of the following are mutable data types?"
   - Grade points: 3
   - Choices:
     - "List" ✅ (is_correct = True)
     - "Dictionary" ✅ (is_correct = True)
     - "Tuple" ❌
     - "String" ❌

4. **Create a User for Testing**:
   - Go to Users in admin
   - Create a test student account

5. **Take the Exam**:
   - Logout from admin
   - Login as test student
   - Navigate to course
   - Complete exam with correct answers
   - Take screenshot of results page

---

## Final Submission Checklist

Before submitting, ensure you have:

- [ ] GitHub repository created and public
- [ ] All code files pushed to GitHub
- [ ] GitHub URLs for all 4 required files:
  - [ ] models.py URL
  - [ ] admin.py URL
  - [ ] course_details_bootstrap.html URL
  - [ ] views.py URL
  - [ ] urls.py URL
- [ ] Screenshot: 03-admin-site.png
- [ ] Screenshot: 07-final.png (showing successful exam with ≥70%)
- [ ] All screenshots clearly show required information

---

## Grading Criteria

| Task | Points | Requirement |
|------|--------|-------------|
| Task 1 | 3 | models.py with Question, Choice, Submission |
| Task 2 | 3 | admin.py with 7 imports and inline classes |
| Task 3 | 1 | Admin site screenshot |
| Task 4 | 2 | course_details_bootstrap.html template |
| Task 5 | 2 | views.py with submit and show_exam_result |
| Task 6 | 2 | urls.py with exam paths |
| Task 7 | 2 | Final exam result screenshot |
| **Total** | **15** | **Passing grade: 70% (10.5 points)** |

---

## Support

If you encounter issues:
1. Check that all migrations are run: `python manage.py migrate`
2. Verify superuser exists: `python manage.py createsuperuser`
3. Check that server is running: `python manage.py runserver`
4. Review Django documentation: https://docs.djangoproject.com/

Good luck with your submission! 🎓
