from multiprocessing.reduction import register

from django.contrib import admin
from .models import Article, Comment


class Filter(admin.ModelAdmin):
    list_filter = ['title',]
    search_fields = ['title',]
    raw_id_fields = ['user',]

class CommentAdmin(admin.ModelAdmin):
    title = ('user','article','text')
    search_fields = ['text']
    list_filter = ['user']
    list_display = ['user', 'article']
    list_editable = ['article']

# Register your models here.
admin.site.register(Article, Filter)
admin.site.register(Comment, CommentAdmin)
