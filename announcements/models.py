from django.db import models
from prose.fields import RichTextField

from core.models import BaseModel


class Announcement(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    short_description = models.TextField(max_length=500, blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
