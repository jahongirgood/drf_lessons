from django.db import models

# Create your models here.


class Categry(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null= True)
    category = models.ForeignKey(Categry, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    