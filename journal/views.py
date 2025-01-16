from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm

# Create your views here.
def index(request):
  context = {"pagename": "Index"}
  return render(request, 'journal/index.html', context)

# Student

def student_list(request):
  students = Student.objects.all()
  context = {"students":students}
  return render(request, "journal/student_list.html", context)

def student_add(request):
  form = StudentForm()
  context = {"form":form}
  return render(request, "journal/student_form.html", context)

# Subject

def subject_list(request):
  subjects = Subject.objects.all()
  context = {"subjects":subjects}
  return render(request, "journal/subject_list.html", context)

def subject_add(request):
  form = SubjectForm()
  context = {"form":form}
  return render(request, "journal/subject_form.html", context)

# Grade

def grade_list(request):
  grades = Grade.objects.all()
  context = {"grades":grades}
  return render(request, "journal/grade_list.html", context)

def grade_add(request):
  form = GradeForm()
  context = {"form":form}
  return render(request, "journal/grade_form.html", context)

def grade_update(request, pk):
  grade = get_object_or_404(Grade, pk=pk)
  form = GradeForm(request.POST, instance=grade)
  context = {"form":form}
  return render(request, "journal/grade_form.html", context)

# def grade_delete(request, pk):
#   grade = get_object_or_404(Grade, pk=pk)
#   form = GradeForm(request.POST, instance=grade)
#   context = {"form":form}
#   return render(request, "journal/grade_form.html", context)