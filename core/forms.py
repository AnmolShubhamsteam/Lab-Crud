from django import forms
from core.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"