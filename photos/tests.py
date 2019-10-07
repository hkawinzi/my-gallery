from django.test import TestCase
from .models import Image,Name,tags

# Create your tests here.
class NameTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.lynn= Name(first_name = 'lynn',last_name = 'nyawera')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lynn,Name))

 # Testing Save Method
    def test_save_method(self):
        self.lynn.save_name()
        names = Name.objects.all()
        self.assertTrue(len(names) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new name and saving it
        self.lynn= Name(first_name = 'lynn', last_name ='Nyawera')
        self.lynn.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Article',post = 'This is a random test Post',editor = self.lynn)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Name.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
