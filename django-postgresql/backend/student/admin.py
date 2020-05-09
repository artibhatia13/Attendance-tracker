from django.contrib import admin
from .models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subj1', 'subj2', 'subj3', 'class_att_subj1', 'class_att_subj2', 'class_att_subj3')


admin.site.register(Student, StudentAdmin)
