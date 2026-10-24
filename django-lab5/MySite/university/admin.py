from django.contrib import admin
from .models import Group, Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'specialty')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'specialty')
    list_filter = ('course',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'record_book', 'email', 'group')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name', 'record_book', 'email')
    list_filter = ('group', 'group__course')


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
