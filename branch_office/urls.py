# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

# Custom
from .views import BranchOfficeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'branch-office', BranchOfficeViewSet)
router.register(r'branch-office/', BranchOfficeViewSet)
urlpatterns = router.urls
