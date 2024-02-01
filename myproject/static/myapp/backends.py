# myapp/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import Student,Teacher

class StudentBackend(ModelBackend):
    def authenticate(self, request, sId=None, password=None, **kwargs):
        try:
            student = Student.objects.get(sId=sId)
        except Student.DoesNotExist:
            return None

        if student.password == password:
            return student

        return None
class TeacherBackend(ModelBackend):
    def authenticate(self, request,  email=None,password=None, **kwargs):
        try:
            teacher = Teacher.objects.get( email=email,password = password)
        except Teacher.DoesNotExist:
            return None

        

        return teacher
