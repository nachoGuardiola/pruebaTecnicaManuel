# agenda/models.py

from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
