from django.db import models

# Create your models here.
class Image(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

    def save_image(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Picture(models.Model):
    picture_name = models.CharField(max_length = 300)
    picture_description = models.TextField()
    picture_location = models.ForeignKey(Image)
    
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)