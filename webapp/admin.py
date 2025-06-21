from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Course,Student
# Register your models here.
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Student)