# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Tag, Snippet


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'note',
        'user',
        'created_at',
        'updated_at',
    )
    list_filter = ('user', 'created_at', 'updated_at')
    raw_id_fields = ('tags',)
    date_hierarchy = 'created_at'
