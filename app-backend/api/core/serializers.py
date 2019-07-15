from rest_framework import serializers
from .models import Garment 

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garment
        fields = ("product_id",
                  "url",
                  "gender",
                  "brand",
                  "product_description",
                  "image_urls",
                  "product_imgs_src",
                  "source",
                  "product_categories",
                  "product_categories_mapped",
                  "price",
                  "product_title")
