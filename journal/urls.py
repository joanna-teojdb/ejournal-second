from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_list', views.student_list, name='student_list'),
    path('student_add', views.student_add, name='student_add'),
    path('subject_list', views.subject_list, name='subject_list'),
    path('subject_add', views.subject_add, name='subject_add'),
    path('grade_list', views.grade_list, name='grade_list'),
    path('grade_add', views.grade_add, name='grade_add'),
    path('grade/<int:pk>/', views.grade_update, name='grade_update')
    ]