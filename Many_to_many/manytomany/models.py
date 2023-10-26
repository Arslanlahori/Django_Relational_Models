from django.db import models

# Create your models here.
#Many to many relation 

class Student(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    DateOfBirth=models.DateField()
    Gender=models.CharField(max_length=10)
    DateOfAdmission=models.DateField()


class Subject(models.Model):
    SubjectName=models.CharField(max_length=70)
    SubDescription=models.TextField()
    student=models.ManyToManyField(Student)

class Studentclass(models.Model):
    ClassName=models.CharField(max_length=60)
    ClassDescription=models.TextField()
    student=models.ManyToManyField(Student)
