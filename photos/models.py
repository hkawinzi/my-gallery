from django.db import models

# Create your models here.
class Image(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)

class tags(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)