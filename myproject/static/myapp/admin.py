from django.contrib import admin


from myapp.models import *
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(CourseAttendance)
admin.site.register(ContinuousAssessment)


