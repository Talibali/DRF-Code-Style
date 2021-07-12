from django.db import models

# Create your models here.



class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    department = models.ForeignKey('classAPIview.Department', null=True,  on_delete=models.CASCADE, related_name='department')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'Student'

