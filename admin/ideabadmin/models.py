from django.db import models

# Create your models here.

class Elemen1(models.Model):
    pilihan = models.TextField()
    lokasi = models.TextField()
    butiran = models.TextField()

    def __str__(self):
        return self.pilihan

class Lokasi(models.Model):
    lid = models.AutoField(primary_key=True)
    list_lokasi = models.CharField(max_length=255)
