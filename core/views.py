from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from core.models import *
from core.forms import *
from django.urls import reverse_lazy

class ViewStudent(ListView):
    model=Students
    template_name="studentlist.html"
    ordering=["-id"]

class DetailStudent(DetailView):
    model=Students
    template_name="details.html" 

class addCourse(CreateView):
    model=Course
    form_class=CourseForm
    template_name="addCourse.html"
    success_url=reverse_lazy("show_student")

class addStudent(CreateView):
    model=Students
    form_class=StudentForm
    template_name="addstudent.html"
    success_url=reverse_lazy("show_student")

class EditStudent(UpdateView):
    model=Students
    form_class=StudentForm
    template_name="edit.html"
    success_url=reverse_lazy("show_student")

class DeleteStudent(DeleteView):
    model=Students
    template_name="delete.html"
    success_url=reverse_lazy("show_student")