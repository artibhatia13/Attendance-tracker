from django.contrib import admin
from .models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subj1', 'subj2', 'subj3')


admin.site.register(Student, StudentAdmin)
