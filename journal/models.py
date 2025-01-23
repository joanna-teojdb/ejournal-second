from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50) 
    class_number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.first_name}:{self.second_name}:{self.class_number}"


class Subject(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    

class Grade(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=1, max_digits=3)
    date_added = models.DateTimeField(auto_now_add=True)

