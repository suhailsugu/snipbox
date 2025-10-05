
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title         = models.CharField(max_length=50, unique=True, db_index=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title         = models.CharField(max_length=200)
    note          = models.TextField()
    user          = models.ForeignKey(User,on_delete=models.CASCADE,related_name='snippets')
    tags          = models.ManyToManyField(Tag,related_name='snippets',blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'

    def __str__(self):
        return self.title