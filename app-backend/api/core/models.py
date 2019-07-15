from django.db import models
from django.db.models import Q

class GarmentQuerySet(models.QuerySet):
    def search(self, query):
        print("working")
        lookup = (
                    Q(name__icontains=query) |
                    Q(description__icontains=query) 
                    )
        return self.filter(lookup)

class GarmentManager(models.Manager):
    def get_queryset(self):
        return GarmentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().all()
        return self.get_queryset().published().search(query)


class Garment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    picture = models.ImageField()
    
    objects = GarmentManager()
    def __str_(self):
        return f"Garment: {self.name}"