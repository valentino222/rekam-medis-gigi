from rest_framework import serializers
from .models import Pasien, DokterGigi, TindakanGigi, RekamMedisGigi

class PasienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasien
        fields = '__all__'

class DokterGigiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DokterGigi
        fields = '__all__'

class TindakanGigiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TindakanGigi
        fields = '__all__'

class RekamMedisGigiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RekamMedisGigi
        fields = '__all__'
