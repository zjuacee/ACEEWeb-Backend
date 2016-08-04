# coding:utf-8
from django.contrib import admin
from ACEEWeb.models import Author, Tag, Article

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'id', 'author', 'publish_time',)
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)