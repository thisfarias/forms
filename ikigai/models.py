from django.db import models

# Create your models here.
class Client(models.Model):
    key = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    profissao = models.CharField(max_length=35, blank=False)
    vocacao = models.CharField(max_length=35, blank=False)
    missao = models.CharField(max_length=35, blank=False)
    paixao = models.CharField(max_length=35, blank=False)

    class Meta:        
        verbose_name = 'Client'
        verbose_name_plural = 'Client'
    
    def __str__(self):
        return self.key
