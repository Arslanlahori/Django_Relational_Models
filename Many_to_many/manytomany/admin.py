from django.contrib import admin
from manytomany.models import Student, Subject, Studentclass

class StudentAdmin(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'DateOfBirth', 'Gender', 'DateOfAdmission']

admin.site.register(Student, StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['SubjectName', 'SubDescription', 'display_students']

    def display_students(self, obj):
        return ", ".join([student.FirstName for student in obj.student.all()])
    display_students.short_description = "Students"

admin.site.register(Subject, SubjectAdmin)

class StudentclassAdmin(admin.ModelAdmin):
    list_display = ['ClassName', 'ClassDescription', 'display_students']

    def display_students(self, obj):
        return ", ".join([student.FirstName for student in obj.student.all()])
    display_students.short_description = "Students"

admin.site.register(Studentclass, StudentclassAdmin)
