from django.db import models
from prose.fields import RichTextField
from pytils.translit import slugify

from core.models import BaseModel


class Unit(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='under_units',
        blank=True,
        null=True
    )
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} - {self.name}'
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.parent:
            self.slug = '{}-{}'.format(self.parent.slug, self.slug)
        super(Unit, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['slug']


class Member(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    position = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    note = RichTextField(default='', blank=True)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name='members',
        blank=True,
        null=True
    )
    photo = models.ImageField(upload_to='members', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
