from django.db import models
from django.utils import timezone

from core.models import BaseModel


class ArticleCategory(BaseModel):
    created_at = None
    updated_at = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикаций'
        ordering = ['name']


class Article(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    members = models.ManyToManyField('units.Member', blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    published_at = models.DateField(null=True, blank=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-published_at']
