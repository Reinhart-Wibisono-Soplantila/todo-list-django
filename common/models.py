from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length= 100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    class Meta:
        verbose_name_plural="Categories"
        
    def __str__(self):
        return self.name

class Status(models.Model):
    name=models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    class Meta:
        verbose_name_plural="Status"
        
    def __str__(self):
        return self.name

