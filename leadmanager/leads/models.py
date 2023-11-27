from django.db import models

# Create your models here.

class Leads(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=60,unique=True)
    message=models.TextField(max_length=200,blank=True)
    Create_at=models.DateTimeField(auto_now_add=True)
class articles(models.Model):
    name_article=models.CharField(max_length=20)
    numero_articles=models.IntegerField()
    Create_at=models.DateTimeField(auto_now_add=True)
