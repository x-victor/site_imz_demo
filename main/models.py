from django.db import models
from django.urls import reverse_lazy
from prose.fields import RichTextField
from pytils.translit import slugify

from core.models import BaseModel


class Menu(BaseModel):
    created_at = None
    updated_at = None
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.parent:
            self.slug = '{}-{}'.format(self.parent.slug, self.slug)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent} - {self.name}'
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['slug']


class Page(BaseModel):
    created_at = None
    updated_at = None
    content = RichTextField()
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('menu-page', kwargs={'slug': self.menu.slug})

    def __str__(self):
        return f'{self.menu}'

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
