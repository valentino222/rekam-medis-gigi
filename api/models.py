from django.db import models

class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class DokterGigi(models.Model):
    nama = models.CharField(max_length=100)
    spesialis = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class TindakanGigi(models.Model):
    nama_tindakan = models.CharField(max_length=100)
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_tindakan

class RekamMedisGigi(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(DokterGigi, on_delete=models.CASCADE)
    tindakan = models.ForeignKey(TindakanGigi, on_delete=models.CASCADE)
    keluhan = models.TextField()
    tanggal_periksa = models.DateField(auto_now_add=True)
    catatan = models.TextField()

    def __str__(self):
        return f"{self.pasien.nama} - {self.tanggal_periksa}"
