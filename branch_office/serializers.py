# -*- coding: utf-8 -*-
from rest_framework import serializers

# Custom
from .models import BranchOffice

from commons.serializers import DirectionSerializer


class BranchOfficeSerializer(serializers.ModelSerializer):

    direction = DirectionSerializer(read_only=True)

    class Meta:
        model = BranchOffice
