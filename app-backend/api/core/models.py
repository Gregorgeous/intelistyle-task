from django.db import models
class Garment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    picture = models.ImageField()
    
    def __str_(self):
        return f"Garment: {self.name}"