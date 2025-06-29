from rest_framework import viewsets
from .models import Pasien, DokterGigi, TindakanGigi, RekamMedisGigi
from .serializers import *

class PasienViewSet(viewsets.ModelViewSet):
    queryset = Pasien.objects.all()
    serializer_class = PasienSerializer

class DokterGigiViewSet(viewsets.ModelViewSet):
    queryset = DokterGigi.objects.all()
    serializer_class = DokterGigiSerializer

class TindakanGigiViewSet(viewsets.ModelViewSet):
    queryset = TindakanGigi.objects.all()
    serializer_class = TindakanGigiSerializer

class RekamMedisGigiViewSet(viewsets.ModelViewSet):
    queryset = RekamMedisGigi.objects.all()
    serializer_class = RekamMedisGigiSerializer
