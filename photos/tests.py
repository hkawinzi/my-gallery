from django.test import TestCase
from .models import Image,Name,tags

# Create your tests here.
class NameTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nairobi= Name(location = 'nairobi')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Name))

 # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_name()
        names = Name.objects.all()
        self.assertTrue(len(names) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new name and saving it
        self.nairobi= Name(location = 'nairobi')
        self.nairobi.save_name()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(image_name = 'frr',image_description = 'This is a random test Post',image_location = self.nairobi)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Name.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

class LocationTestClass(TestCase):
    '''
    Tests for Location class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.location = Location(id = 50, name = 'Kenya')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Location class.
        '''
        
        self.assertTrue(isinstance(self.location, Location))
        
        
    def test_delete_method(self):
        '''
        Test if the object can be deleted from the database.
        '''
        self.location.save_location()
        self.location = Location.objects.get(id = 50)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)
        