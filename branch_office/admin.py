# -*- coding: utf-8 -*-
from django.contrib import admin

#custom
from .models import BranchOffice
from utils.wrappers import custom_titled_filter


@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', ]
    list_display = ['name', 'direction', 'is_active']
    search_fields = [
        'direction__commune__state__name',
        'direction__commune__name',
        'direction__street'
    ]
    list_filter = [
        'is_active',
        ('direction__commune__state__name', custom_titled_filter('Región')),
        ('direction__commune__name', custom_titled_filter('Comuna')),
    ]
