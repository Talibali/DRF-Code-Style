from django.db import models
from django.core.validators import RegexValidator
from common.constants import ConstantMessages

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message=ConstantMessages.PHONE_MESSAGE)
    phone = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    marital_status = models.BooleanField(default=False)
    dob = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Employee'
