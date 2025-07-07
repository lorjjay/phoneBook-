# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Users(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class savedContacts(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='savedContacts', null=True, blank=True)
    contactUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='linked_as_contact')
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100, blank=True)
    saved_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} (saved by {self.owner.username})"
    
class CallLog(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='calls', null=True, blank=True)
    contact = models.ForeignKey(savedContacts, on_delete=models.CASCADE, related_name='call_logs')
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, null=True, blank=True)
    time_spent = models.FloatField()
    date_called = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call to {self.phone} on {self.date_called}"
