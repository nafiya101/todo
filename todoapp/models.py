from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todos(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    status=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)