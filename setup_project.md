# Quick Setup Instructions

## Prerequisites
Make sure you have Python 3.8+ installed.

## Setup Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser for Admin Access
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Access the Application
- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## Quick Test Data Creation

After logging into the admin panel, create in this order:

1. **Create Instructor** (if needed)
   - Link to a User
   - Set as full_time
   - Set total_learners (e.g., 100)

2. **Create a Course**
   - Name: "Introduction to Python"
   - Description: "Learn Python programming"
   - Select instructors
   - Set pub_date
   - Upload an image (optional)

3. **Create Lessons** (use the Course you created)
   - Lesson 1: Title "Python Basics", Order: 1
   - Lesson 2: Title "Data Structures", Order: 2
   - Add Questions directly within each lesson using the inline form

4. **Add Questions** (within Lesson admin)
   - Click on a Lesson
   - Use the "Question" inline section
   - Add question text and grade points
   - Add Choices directly within each question using the inline form

5. **Add Choices** (within Question admin)
   - Add 3-4 choices per question
   - Check "is_correct" for the right answer(s)
   - For multiple correct answers, check multiple boxes

## Testing the Exam

1. Create a regular user account (not superuser) or logout and register
2. Navigate to the course page
3. View lessons and exam questions
4. Select answers for all questions
5. Click "Submit Exam"
6. View your results with score and detailed feedback

## Troubleshooting

### ImportError: No module named 'django'
```bash
pip install Django
```

### ImportError: No module named 'PIL'
```bash
pip install Pillow
```

### Database is locked
Close any other processes using the database or delete db.sqlite3 and run migrations again.

### Static files not loading
```bash
python manage.py collectstatic
```

## File Locations for Submission

- **models.py**: `onlinecourse/models.py`
- **admin.py**: `onlinecourse/admin.py`
- **views.py**: `onlinecourse/views.py`
- **urls.py**: `onlinecourse/urls.py`
- **course_details_bootstrap.html**: `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
- **exam_result_bootstrap.html**: `onlinecourse/templates/onlinecourse/exam_result_bootstrap.html`

## Next Steps

Refer to `SUBMISSION_GUIDE.md` for:
- Detailed assignment requirements
- How to upload to GitHub
- How to take required screenshots
- Submission checklist
