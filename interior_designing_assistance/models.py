from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  # Consider using a hashed password
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.username
