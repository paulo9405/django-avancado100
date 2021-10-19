from django.db import models
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count



class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desconto(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def min(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def max(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def num_ped(self):
        return self.all().aggregate(Count('valor'))['valor__count']

    def n_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('nfe_emitida'))['nfe_emitida__count']