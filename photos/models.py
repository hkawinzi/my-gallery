from django.db import models

# Create your models here.
class Name(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

    def save_name(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_name = models.CharField(max_length = 300)
    image_description = models.TextField()
    image_location = models.ForeignKey(Name)
    
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photos