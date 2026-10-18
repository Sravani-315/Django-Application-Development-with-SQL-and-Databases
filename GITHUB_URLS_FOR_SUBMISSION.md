# GitHub URLs for Assignment Submission

## Your Repository
**Repository URL**: https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases

---

## Task 1: models.py (3 points)
**GitHub URL**:
```
https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/onlinecourse/models.py
```

**What to verify**:
- ✅ Question model with question_text, grade_points, course, lesson
- ✅ Choice model with choice_text, is_correct, question
- ✅ Submission model with enrollment and choices (ManyToManyField)

---

## Task 2: admin.py (3 points)
**GitHub URL**:
```
https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/onlinecourse/admin.py
```

**What to verify**:
- ✅ Seven imported classes: Course, Lesson, Instructor, Learner, Question, Choice, Submission
- ✅ QuestionInline class (line 8)
- ✅ ChoiceInline class (line 13)
- ✅ QuestionAdmin class (line 18)
- ✅ LessonAdmin class (line 25)

---

## Task 3: Admin Site Screenshot (1 point)
**File to upload**: `03-admin-site.png`

**Steps to create this screenshot**:
1. Run these commands:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
2. Go to: http://localhost:8000/admin/
3. Login with your superuser credentials
4. Take a screenshot showing:
   - Authentication and Authorization section
   - OnlineCourse section with all models
5. Save as `03-admin-site.png`

---

## Task 4: course_details_bootstrap.html (2 points)
**GitHub URL**:
```
https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html
```

**What to verify**:
- ✅ Displays course name (line 29)
- ✅ Shows course description (line 30)
- ✅ Django template tags to iterate through lessons (line 57: {% for lesson in course.lesson_set.all %})
- ✅ Bootstrap 5 styling (line 9)
- ✅ Form with CSRF token (line 54)

---

## Task 5: views.py (2 points)
**GitHub URL**:
```
https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/onlinecourse/views.py
```

**What to verify**:
- ✅ `submit()` function (line 48)
  - Creates Submission object (line 65)
  - Extracts choices from POST data (line 68-75)
  - Redirects to show_exam_result (line 80)
- ✅ `show_exam_result()` function (line 85)
  - Calculates score using is_get_score method (line 107)
  - Compares total_score with max_score (line 118)
  - Determines pass/fail with 70% threshold (line 121)

---

## Task 6: urls.py (2 points)
**GitHub URL**:
```
https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/onlinecourse/urls.py
```

**What to verify**:
- ✅ Path for submit (line 16): `path('course/<int:course_id>/submit/', views.submit, name='submit')`
- ✅ Path for show_exam_result (line 19): `path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result')`

---

## Task 7: Final Exam Screenshot (2 points)
**File to upload**: `07-final.png`

**Steps to create this screenshot**:

### 1. Set up sample data in admin:
```bash
python manage.py runserver
```
Go to http://localhost:8000/admin/

### 2. Create test data:
- Create a Course (e.g., "Introduction to Python")
- Create Lessons (e.g., "Python Basics", "Data Structures")
- Create Questions with grade_points
- Create Choices for each question (mark some as is_correct=True)

### 3. Take the exam:
- Logout from admin
- Go to http://localhost:8000/
- Click on your course
- Answer all questions correctly (at least 70%)
- Submit the exam

### 4. Take screenshot showing:
- ✅ "🎉 Congratulations! 🎉" message
- ✅ "You passed the exam!" text
- ✅ Score (e.g., "8/10")
- ✅ Percentage ≥70%
- ✅ "PASSED" badge
- ✅ Detailed exam results showing questions and answers
- ✅ Save as `07-final.png`

---

## Quick Setup Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## Submission Checklist

Before submitting your assignment, make sure you have:

- [ ] **Task 1**: models.py URL copied
- [ ] **Task 2**: admin.py URL copied
- [ ] **Task 3**: Screenshot `03-admin-site.png` created and ready
- [ ] **Task 4**: course_details_bootstrap.html URL copied
- [ ] **Task 5**: views.py URL copied
- [ ] **Task 6**: urls.py URL copied
- [ ] **Task 7**: Screenshot `07-final.png` created (showing ≥70% score with Congratulations message)

---

## Important Notes

1. All URLs are in the format: `https://github.com/Sravani-315/Django-Application-Development-with-SQL-and-Databases/blob/main/path/to/file`

2. Make sure your screenshots clearly show:
   - For Task 3: Admin panel with both sections visible
   - For Task 7: Congratulations message, score, and detailed results

3. Test your application before taking screenshots to ensure everything works correctly

4. The passing grade is 70% (10.5 out of 15 points)

---

## Need Help?

- Check `SUBMISSION_GUIDE.md` for detailed instructions
- Check `setup_project.md` for quick setup guide
- Check `README.md` for project documentation

Good luck with your submission! 🎓✨
