from django.contrib import admin
from .models import News, Task


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at')
    list_editable = ('is_published',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'category', 'is_completed', 'deadline', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'category')
    list_filter = ('is_completed', 'category', 'priority')
    list_editable = ('is_completed', 'priority')
    ordering = ('priority', 'deadline')
