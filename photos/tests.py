from django.test import TestCase
from .models import Image,Picture,tags

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.lynn= Image(first_name = 'lynn',last_name = 'nyawera')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lynn,Image))