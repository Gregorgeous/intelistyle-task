from django.db import models
from django.db.models import Q

class GarmentQuerySet(models.QuerySet):
    def search(self, query):
        print("working")
        lookup = (
            Q(product_title__icontains=query) |
            Q(product_categories__icontains=query) |
            Q(gender__icontains=query) |
            Q(brand__icontains=query)
                    )
        return self.filter(lookup)

class GarmentManager(models.Manager):
    def get_queryset(self):
        return GarmentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().all()
        return self.get_queryset().published().search(query)


class Image(models.Model):
    url = models.URLField(blank=True, primary_key=True)
    path = models.CharField(max_length=300)
    checksum = models.CharField(max_length=35)

class Garment(models.Model):
    product_categories_mapped = models.IntegerField()
    product_id = models.CharField(primary_key=True, max_length=13)
    url = models.URLField()
    gender = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    product_description = models.TextField(blank=True)
    image_urls = models.URLField(blank=True)
    product_imgs_src = models.URLField(blank=True)
    source = models.URLField(blank=True)
    product_categories = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    product_title = models.CharField(max_length=125)
    images = models.OneToOneField(Image,
                                  on_delete=models.CASCADE, null=True)
    objects = GarmentManager()
    def __str_(self):
        return f"Garment: {self.product_title}"

