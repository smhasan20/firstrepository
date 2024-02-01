

from django.shortcuts import get_object_or_404, redirect, render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.views.decorators.csrf import csrf_protect
from myapp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .backends import StudentBackend, TeacherBackend
import seaborn as sns



def login_view(request):
    if request.method == 'POST':
        sId = request.POST.get('sId')
        password = request.POST.get('password')
        if sId is not None and password is not None:
            student = authenticate(request, sId=sId, password=password)
            if student is not None:
                assessment1 = ContinuousAssessment.objects.filter(student = student).select_related('course'
                ).values('course__courseName','marks','comment').order_by('course')
                course_attendance = CourseAttendance.objects.filter(student = student).select_related('course').values('course__courseName','attendance')

                context = {
                    'course_attendance':course_attendance,
                    'assessment1':assessment1,
                    
                    'student': student,
                   
                }

                return render(request, 'dashboard.html', context)
            else:
                return render(request, 'home.html')
        else:
            return render(request, 'login_student.html')

    return render(request, 'login_student.html')

def login_teacherview(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
    
        teacher = authenticate(request, email=email,password = password)
       
        if teacher is not None:
            auth_login(request, teacher)
            
            return redirect('teacherActivity')  
        else:
            # Invalid login, show error message or handle as needed
            return render(request, 'login_teacher.html')

    
    return render(request, 'login_teacher.html')

def login_teacher(request):
    return render(request,'login_teacher.html')
def teacherActivity(request):
    return render(request,'teacherActivity.html')
def home(request):
    return render(request,'home.html')
def loginst(request):
    return render(request,'loginst.html')
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')
def login_student(request):
    return render(request,'login_student.html')



def dashboard(request):
    student = request.user
    
    # Fetching courses and marks for the logged-in student
    student_courses = ContinuousAssessment.objects.filter(student=student).select_related('course').values(
        'course__courseName', 'marks'
    )

    return render(request, 'dashboard.html', {'student': student, 'student_courses': student_courses})


def input_student_course(request):
    if request.method == 'POST':
        form = CourseAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_student_course')  # Redirect to a success page
    else:
        form = CourseAttendanceForm

    return render(request, 'input_student_course.html', {'form': form})

def add_course_marks(request):
    if request.method == 'POST':
        form = ContinuousAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('continuousassesment')  # Rirect to a course list page or another desired page
    else:
        form = ContinuousAssessmentForm()

    return render(request, 'continuousassesment.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')  # Redirect to a student list page or another desired page
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_teacher')  # Redirect to a teacher list page or another desired page
    else:
        form = TeacherForm()

    return render(request, 'add_teacher.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')  # Rirect to a course list page or another desired page
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def signupteacher(request):
    return render(request,'signupStudent.html')
def signupstudent(request):
    return render(request,'signupTeacher.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, cid):
    course = get_object_or_404(Course, cId=cid)
    return render(request, 'course_detail.html', {'course': course})


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_add.html', {'form': form})


def course_update(request, cid):
    course = get_object_or_404(Course, cId=cid)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_update.html', {'form': form})

def course_delete(request, cid):
    course = get_object_or_404(Course, cId=cid)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_delete.html', {'course': course})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, sid):
    student = get_object_or_404(Student, sId=sid)
    return render(request, 'student_detail.html', {'student': student})

def student_update(request, sid):
    student = get_object_or_404(Student, sId=sid)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_update.html', {'form': form})


def student_delete(request, sid):
    student = get_object_or_404(Student, sId=sid)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})

def courseattendance_list(request):
    course_attendances = CourseAttendance.objects.all()
    return render(request, 'courseattendance_list.html', {'course_attendances': course_attendances})


def courseattendance_detail(request, attendance_id):
    attendance = get_object_or_404(CourseAttendance, id=attendance_id)
    return render(request, 'courseattendance_detail.html', {'attendance': attendance})


def courseattendance_add(request):
    if request.method == 'POST':
        form = CourseAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseattendance_list')
    else:
        form = CourseAttendanceForm()
    return render(request, 'courseattendance_add.html', {'form': form})


def courseattendance_update(request, attendance_id):
    attendance = get_object_or_404(CourseAttendance, id=attendance_id)
    if request.method == 'POST':
        form = CourseAttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('courseattendance_list')
    else:
        form = CourseAttendanceForm(instance=attendance)
    return render(request, 'courseattendance_update.html', {'form': form, 'attendance': attendance})


def courseattendance_delete(request, attendance_id):
    attendance = get_object_or_404(CourseAttendance, id=attendance_id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('courseattendance_list')
    return render(request, 'courseattendance_delete.html', {'attendance': attendance})