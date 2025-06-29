from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'pasien', PasienViewSet)
router.register(r'dokter', DokterGigiViewSet)
router.register(r'tindakan', TindakanGigiViewSet)
router.register(r'rekam-medis', RekamMedisGigiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
