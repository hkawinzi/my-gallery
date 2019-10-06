from django.db import models

# Create your models here.
class Image(models.Model):
    Image_name = models.CharField(max_length = 300)
    Image_description = models.CharField(max_length = 300)
    Image_location = models.CharField(max_length = 300)
    Image_category =  models.CharField(max_length = 300)
    