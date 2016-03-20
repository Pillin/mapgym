# -*- coding: utf-8 -*-
from django.contrib import admin

#custom
from .models import BranchOffice


@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', ]
