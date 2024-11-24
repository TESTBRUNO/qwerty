from django.test import TestCase

# Create your tests here.
from myapp.models import Animal


class AnimalTestCase(TestCase):
   def setUp(self):
       Animal.objects.create(name="lion", sound="roar")
       Animal.objects.create(name="cat", sound="meow")
   def test_animals_can_speak(self):
      """Animals that can speak are correctly identified"""
      lion = Animal.objects.get(name="lion")
      cat = Animal.objects.get(name="cat")
      self.assertEqual(lion.speak(2,2), 4)
      self.assertEqual(cat.speak(3,3), 27)
      self.assertEqual(cat.speak(0,0), 27)
      self.assertEqual(cat.speak(0), 27)


