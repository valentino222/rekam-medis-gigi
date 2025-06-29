from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PasienViewSet, DokterGigiViewSet, TindakanGigiViewSet, RekamMedisGigiViewSet

# Custom Router dengan judul & deskripsi yang dimodifikasi
class CustomRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        view = super().get_api_root_view(api_urls)
        view.cls.__name__ = "Sistem Informasi Rekam Medis "
        view.cls.__doc__ = "Halaman root untuk API Rekam Medis Gigi"
        return view

router = CustomRouter()
router.register(r'pasien', PasienViewSet)
router.register(r'dokter', DokterGigiViewSet)
router.register(r'tindakan', TindakanGigiViewSet)
router.register(r'rekam-medis', RekamMedisGigiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
