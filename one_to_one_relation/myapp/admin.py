from django.contrib import admin

from myapp.models import Student,Subject,Studentclass

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'DateOfBirth', 'Gender', 'DateOfAdmission']
   
admin.site.register(Student,StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['SubjectName', 'SubDescription', 'student']

admin.site.register(Subject,SubjectAdmin)


class StudentclassAdmin(admin.ModelAdmin):
    list_display = ['ClassName', 'ClassDescription', 'student']


admin.site.register(Studentclass,StudentclassAdmin)
