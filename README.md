# Django Online Course Application

A comprehensive online course platform built with Django that includes exam functionality with automated grading.

## Features

- **Course Management**: Browse and view available courses
- **User Enrollment**: Register and enroll in courses
- **Lesson Content**: Access course lessons with detailed content
- **Exam System**: Take exams with multiple-choice questions
- **Automated Grading**: Instant exam results with detailed feedback
- **Admin Interface**: Comprehensive admin panel for managing courses, lessons, questions, and choices

## Models

### Core Models
- **Course**: Represents an online course with name, description, image, and instructors
- **Lesson**: Course content organized by order within a course
- **Instructor**: Course instructors with user relationship
- **Learner**: Students with occupation and profile information
- **Enrollment**: Tracks user enrollment in courses

### Exam Models
- **Question**: Exam questions linked to courses and lessons with grade points
- **Choice**: Multiple choice answers with correct/incorrect flag
- **Submission**: Tracks user exam submissions with selected choices

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd "Django Application Development with SQL and Databases"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application:
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

## Admin Interface

The admin interface includes:
- **QuestionInline**: Add questions directly within lesson editing
- **ChoiceInline**: Add answer choices directly within question editing
- **QuestionAdmin**: Manage questions with choices
- **LessonAdmin**: Manage lessons with nested questions

## URL Structure

- `/` - Home page with course list
- `/course/<id>/` - Course details with lessons and exam
- `/course/<id>/enroll/` - Enroll in a course
- `/course/<id>/submit/` - Submit exam answers
- `/course/<id>/submission/<submission_id>/result/` - View exam results

## Exam Grading

The exam system uses the `is_get_score()` method to evaluate submissions:
- Students must select ALL correct choices for a question to receive points
- Passing grade: 70%
- Results show detailed feedback with correct answers highlighted

## Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── onlinecourse/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        └── onlinecourse/
            ├── index.html
            ├── course_details_bootstrap.html
            └── exam_result_bootstrap.html
```

## Technologies Used

- Django 4.x
- Bootstrap 5.1.3
- SQLite (default database)
- Pillow (for image handling)

## License

This project is for educational purposes.
