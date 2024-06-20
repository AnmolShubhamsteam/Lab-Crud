from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Course(models.Model):
    course_name=models.CharField(max_length=122)
    course_credit=models.PositiveIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(4)
                    ]
    )
    def __str__(self) -> str:
        return f"{self.course_name}"

class Students(models.Model):
    student_name=models.CharField(max_length=122)
    student_usn=models.CharField(max_length=122,unique=True)
    student_sem=models.PositiveIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(8)
                    ]
    )
    enrollment=models.ManyToManyField(Course)
    def __str__(self) -> str:
        return f"{self.student_name} ( {self.student_usn} )"
