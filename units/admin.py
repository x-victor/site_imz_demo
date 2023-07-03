from django.contrib import admin

from units.models import Unit, Member


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['position', 'first_name', 'last_name', 'email', 'phone', 'unit']
