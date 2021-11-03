from django.db import models
import datetime

# Create your models here.

class Client(models.Model):
    key = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    organizacao = models.FloatField(default=0, blank=False, null=False)
    tecnica = models.FloatField(default=0, blank=False, null=False)
    comportamento = models.FloatField(default=0, blank=False, null=False)
    empreendedorismo = models.FloatField(default=0, blank=False, null=False)
    intraempreendedorismo = models.FloatField(default=0, blank=False, null=False)
    lideranca = models.FloatField(default=0, blank=False, null=False)
    geral = models.FloatField(default=0, blank=False, null=False)
    last_data = models.DateField(default=datetime.date.today())

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'
    
    def __str__(self):
        return self.key
