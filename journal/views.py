from django.views.generic import (CreateView, DeleteView, ListView, UpdateView, TemplateView)
from django.shortcuts import render, redirect
from .models import Student, Grade, Subject
from .forms import StudentForm, SubjectForm, GradeForm
from django.urls import reverse_lazy
from .mixins import TeacherRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Widoki ogolne 
class JournalIndexView(TemplateView):
    
    template_name = "journal/index.html"

# Students
class StudentListView(ListView):
    
    template_name = "journal/student_list.html"
    model = Student
    context_object_name = "students"
    
# kontrola przez nauczyciela
class StudentCreateView(TeacherRequiredMixin, CreateView):
    
    template_name = "journal/student_form.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("student_list")

class StudentUpdateView(TeacherRequiredMixin, UpdateView):
    
    template_name = "journal/student_update_form.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("student_list")

class StudentDeleteView(TeacherRequiredMixin, DeleteView):
    
    template_name = "journal/student_confirm_delete.html"
    model = Student
    success_url = reverse_lazy("student_list")


# Subjects
class SubjectListView(ListView):
    
    template_name = "journal/subject_list.html"
    model = Subject
    context_object_name = "subjects"
    

class SubjectCreateView(TeacherRequiredMixin, CreateView):
    
    template_name = "journal/subject_form.html"
    model =  Subject
    form_class = SubjectForm
    success_url = reverse_lazy("subject_list")

class SubjectUpdateView(TeacherRequiredMixin, UpdateView):
    
    template_name = "journal/subject_update_form.html"
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy("subject_list")

class SubjectDeleteView(TeacherRequiredMixin, DeleteView):
    
    template_name = "journal/subject_confirm_delete.html"
    model = Subject
    success_url = reverse_lazy("subject_list")



# Grades
class GradeListView(ListView):
    
    template_name = "journal/grade_list.html"
    model = Grade
    context_object_name = "grades"
    

class GradeCreateView(TeacherRequiredMixin, CreateView):
    
    template_name = "journal/grade_form.html"
    model =  Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

class GradeUpdateView(TeacherRequiredMixin, UpdateView):
    
    template_name = "journal/grade_form.html"
    model =  Grade
    form_class = GradeForm
    success_url = reverse_lazy("grade_list")

class GradeDeleteView(DeleteView, TeacherRequiredMixin):
    
    template_name = "journal/grade_confirm_delete.html"
    model =  Grade
    success_url = reverse_lazy("grade_list")


# user site
class MyGradesListView(ListView):
    model = Grade
    template_name = "journal/my_grades.html"
    context_object_name = "grades"

    def get_queryset(self):
        student = self.request.user.student
        try:
            return Grade.objects.filter(student=student).order_by("-date_added") #filtrowanie po polu student
        except Student.DoesNotExist:
            return Grade.objects.none()

def filter_grades(request):
    query = Grade.objects.all()
    subject_id = request.GET.get('subject_id')
    student_id = request.GET.get('student_id')
    if subject_id:
        query = query.filter(subject_id=subject_id)
    if student_id:
        query = query.filter(student_id=student_id)
        
    subjects = Subject.objects.all()
    students = Student.objects.all()

    context = {"grades":query, "subjects":subjects, "students":students}
    return render(request, "journal/grade_list.html", context)

def no_permission(request):
    return render(request, "journal/no_permission.html", {})


# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         print("Wchodze do 109")
#         if form.is_valid():
#             form.save()
#             print("Wchodze do 112")
#             return redirect("student_list")   
#         else:
#             form = UserCreationForm()
#             return render(request, "register.html", {"form":form})
#     else:
#         form = UserCreationForm()
#     return render(request, "register.html", {"form":form})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("student_list")

