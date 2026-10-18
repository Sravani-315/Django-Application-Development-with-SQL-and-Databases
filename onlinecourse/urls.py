from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home page - list all courses
    path('', views.index, name='index'),
    
    # Course detail page
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    
    # Enrollment
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    
    # Submit exam
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Show exam result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='show_exam_result'),
]
