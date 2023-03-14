from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class Manager(UserManager):

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['created_at'] = timezone.now()
        extra_fields['role'] = 'admin'
        super(Manager, self).create_superuser(
            username, password=password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ("customer", "Customer"),
        ("staff", "Staff"),
        ("admin", "Admin")
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    firebase_uid = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_profile_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    objects = Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.ForeignKey(
        'State', related_name='addresses', on_delete=models.SET_NULL,
        null=True)
    pincode = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses")
