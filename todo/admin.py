from django.contrib import admin
from .models import ToDo

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user', 'created_at', )
    list_filter = ('category', 'status', 'user')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at', 'user')

    fieldsets = (
        ('Fillable', {
            'fields': ('title', 'description', 'category', 'status', )
        }),
        ('Read only', {
            'fields': ('user', 'created_at', 'updated_at', ),
            'classes': ('collapse',)  # Biar bagian ini bisa disembunyikan
        }),
    )
admin.site.register(ToDo, ToDoAdmin)