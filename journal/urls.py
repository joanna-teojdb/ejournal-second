from django.urls import path

from .views import *

urlpatterns = [
    path('', JournalIndexView.as_view(), name='index'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_add/', StudentCreateView.as_view(), name='student_add'),
    path('subject_list/', SubjectListView.as_view(), name='subject_list'),
    path('subject_add/', SubjectCreateView.as_view(), name='subject_add'),
    path('grade_list/', GradeListView.as_view(), name='grade_list'),
    path('grade_add/', GradeCreateView.as_view(), name='grade_add'),
    path('grade/<int:pk>/edit/', GradeUpdateView.as_view(), name='grade_update'),
    
    path('grade/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
    path('grades/filter', filter_grades, name='grades_filter'),
    path('no_permission/', no_permission, name='no_permission'),
    path('my_grades/', MyGradesListView.as_view(), name='my_grades')
    ]