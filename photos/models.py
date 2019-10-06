from django.db import models

# Create your models here.


class Image(models.Model):
    image_name = models.CharField(max_length=300)
    image_description = models.TextField()
    image_location = models.CharField(max_length=300)
    image_category = models.CharField(max_length=300)

class tags(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)