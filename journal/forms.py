from django import forms
from .models import Student, Subject, Grade

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student 
        fields = ['first_name', 'second_name', 'class_number']  


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name']  


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade 
        fields = ['subject', 'student', 'value']  

    