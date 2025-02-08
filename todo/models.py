from django.db import models
from common.models import Category, Status

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural='Todos'
    
    def __str__(self):
        return self.title