from django.db import models

# Create your models here.
class Image(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Picture(models.Model):
    image_name = models.CharField(max_length = 300)
    image_description = models.TextField()
    image_location = models.ForeignKey(Image)
    image_category = models.ForeignKey(Image)