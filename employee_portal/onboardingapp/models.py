from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeOnboardInfo(models.Model):

    employee = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_url = models.URLField(blank=True)
    profile_img = models.ImageField(upload_to='profile_img', blank=True)

    def __str__(self):
        return self.employee.username