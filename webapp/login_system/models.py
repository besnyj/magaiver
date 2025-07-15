from django.db import models
from django.contrib.auth.models import User

class AssessorModel(models.Model):

    def __init__(self, email, password):
        self.email = models.EmailField(max_length=128)
        self.password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password
        }
