from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Role(models.Model):
#     role_name = models.CharField(max_length=20)
#     class Meta:
#         verbose_name_plural = "Role"
#     def __str__(self):
#         return self.role_name

class Profile(models.Model):
    ROLE_CHOICES = [
        ('manager', 'MANAGER'),
        ('normal user', 'NORMAL USER'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100, choices=ROLE_CHOICES, default='normal user')

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        full_name = self.user.first_name+" "+self.user.last_name
        return full_name+' - '+self.role_name


# class UserAuthorization(models.Model):
#     ROLE_CHOICES = [
#         ('student', 'STUDENT'),
#         ('coordinator', 'COORDINATOR'),
#         ('supervisor', 'SUPERVISOR'),
#         ('admin', 'ADMIN'),
#     ]
#     role_name = models.CharField(max_length=100, choices=ROLE_CHOICES)
#     manage_users = models.BooleanField(default=False)
#     submit_tasks = models.BooleanField(default=False)
#     add_field_place = models.BooleanField(default=False)
#     view_field_place = models.BooleanField(default=False)
#     class Meta:
#         verbose_name_plural = "User authorization"
#     def __str__(self):
#         return str(self.role)
