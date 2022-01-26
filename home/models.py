from django.db import models

class Todo(models.Model):
    title= models.CharField(max_length=200)
    email= models.EmailField(unique=True)
    body=models.TextField()
    created=models.DateTimeField()
# Create your models here.
