from django.contrib import admin
from .models import ToDo

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at')
    search_fields = ('title',)
    list_filter = ('status',)

admin.site.register(ToDo, ToDoAdmin)