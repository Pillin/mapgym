# -*- coding: utf-8 -*-
from rest_framework import serializers

# Custom
from .models import Direction, Commune, State


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State


class CommuneSerializer(serializers.ModelSerializer):

    state = StateSerializer(read_only=True)

    class Meta:
        model = Commune


class DirectionSerializer(serializers.ModelSerializer):

    commune = CommuneSerializer(read_only=True)

    class Meta:
        model = Direction
