from django.db import models

# Create your models here.
class Assessor(models.Model):

    def __str__(self):
        return self.email

    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)