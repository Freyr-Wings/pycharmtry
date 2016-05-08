from django.contrib import admin

# Register your models here.
from .models import User, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comments","left"]
    list_display_links = ["comments"]

admin.site.register(Comment, CommentAdmin)#connect Post with PostModelAdmin