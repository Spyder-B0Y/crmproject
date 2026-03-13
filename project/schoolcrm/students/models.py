from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    roll = models.IntegerField()

    def __str__(self):
        return self.name