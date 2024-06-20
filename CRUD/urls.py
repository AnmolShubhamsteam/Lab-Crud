from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("course/",addCourse.as_view(),name="course_list"),
    path("student/",addStudent.as_view(),name="student_list"),
    path("edit/<int:pk>",EditStudent.as_view(),name="edit_student"),
    path("",ViewStudent.as_view(),name="show_student"),
    path("detail/<int:pk>",DetailStudent.as_view(),name="Detail_student"),
    path("delete/<int:pk>",DeleteStudent.as_view(),name="Delete_student")
]
