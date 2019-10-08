from django.db import models

# Create your models here.
class Name(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

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
    image_path = models.ImageField(upload_to = 'images/')

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photos

class location(models.Model):
    location = models.CharField(max_length=30)

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        location = Location.objects.all().delete()
        return location


class Category(models.Model):
    Category = models.CharField(max_length=30)

    def __str__(self):
        return self.Category