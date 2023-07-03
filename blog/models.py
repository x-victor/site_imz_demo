from django.db import models
from prose.fields import RichTextField
from pytils.translit import slugify

from core.models import BaseModel


class Tag(BaseModel):
    created_at = None
    updated_at = None
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']


class Post(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = RichTextField()
    short_description = models.TextField(max_length=500, blank=True)
    unit = models.ForeignKey('units.Unit', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
