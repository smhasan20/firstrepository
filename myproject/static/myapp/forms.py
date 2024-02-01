# myapp/forms.py
from django import forms
from .models import Course, Student, CourseAttendance, Teacher,ContinuousAssessment

class CourseAttendanceForm(forms.ModelForm):
    class Meta:
        model = CourseAttendance
        fields = ['student', 'course','attendance']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sId', 'sName', 'contactNo', 'Address', 'password']

    def clean_password(self):
    
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['tId', 'tName', 'contactNo', 'email','password']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cId', 'courseName', 'teacher']

class ContinuousAssessmentForm(forms.ModelForm):
    class Meta:
        model = ContinuousAssessment
        fields =['student','course','marks','comment']
