# myapp/models.py
from django.db import models

class Student(models.Model):
    sId = models.IntegerField(primary_key=True)
    sName = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=15)
    Address = models.TextField()
    password = models.CharField(max_length=15,default = '')  # Assuming password will be hashed
    last_login = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.sName


class Teacher(models.Model):
    tId = models.IntegerField(primary_key=True)
    tName = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=128,default='')  # Password field for the teacher
    last_login = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.tName

class Course(models.Model):
    cId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.courseName

class ContinuousAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(default=" ")
    def __str__(self):
        return f"{self.student} - {self.course}"

class CourseAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance = models.CharField(default="0%", max_length=5)
    
    
    def __str__(self):
        return f"{self.student} - {self.course}"
