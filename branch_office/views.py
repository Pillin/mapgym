# -*- coding: utf-8 -*-
from rest_framework import viewsets

# Custom
from .serializers import BranchOfficeSerializer
from .models import BranchOffice


class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer
