
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('loginst/',views.loginst,name ='loginst'),
    path('login_view/',views.login_view,name ='login_view'),
    path('login_student/',views.login_student,name ='login_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/',views.signup,name ='signup'),
    path('input_student_course/', views.input_student_course, name='input_student_course'),
    
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_course/', views.add_course, name='add_course'),
    path('login_teacherview/',views.login_teacherview, name='login_teacherview'),
    path('login_teacher/',views.login_teacher, name='login_teacher'),
    path('teacherActivity/',views.teacherActivity, name='teacherActivity'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('signupstudent/',views.signupstudent, name='signupstudent'),
    path('signupteacher/',views.signupteacher, name='signupteacher'),
    path('continuousassesment/',views.add_course_marks, name='continuousassesment'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:cid>/', views.course_detail, name='course_detail'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/<int:cid>/update/', views.course_update, name='course_update'),
    path('courses/<int:cid>/delete/', views.course_delete, name='course_delete'),

    
    path('students/', views.student_list, name='student_list'),
    path('students/<int:sid>/', views.student_detail, name='student_detail'),
    path('add_student/', views.add_student, name='add_student'),
 
    path('students/<int:sid>/update/', views.student_update, name='student_update'),
    path('students/<int:sid>/delete/', views.student_delete, name='student_delete'),
    path('courseattendances/', views.courseattendance_list, name='courseattendance_list'),
    path('courseattendances/<int:attendance_id>/', views.courseattendance_detail, name='courseattendance_detail'),
    path('courseattendances/add/', views.courseattendance_add, name='courseattendance_add'),
    path('courseattendances/<int:attendance_id>/update/', views.courseattendance_update, name='courseattendance_update'),
    path('courseattendances/<int:attendance_id>/delete/', views.courseattendance_delete, name='courseattendance_delete')
]

