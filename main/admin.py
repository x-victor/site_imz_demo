from django.contrib import admin

from main.models import Page, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
