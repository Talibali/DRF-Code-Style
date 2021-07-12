from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    class Meta:
        db_table = "Department"

    def __str__(self):
        return self.name
