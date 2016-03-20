# -*- coding: utf-8 -*-
from rest_framework import serializers

# Custom
from .models import BranchOffice


class BranchOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
