from django.db import models


# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    studentID = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
