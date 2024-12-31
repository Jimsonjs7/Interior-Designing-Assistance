from django.db import models

class User(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    full_name=models.CharField(max_length=100,null=True) 
    email=models.EmailField(default='example@example.com')
    def _str_(self):
        return self.username
