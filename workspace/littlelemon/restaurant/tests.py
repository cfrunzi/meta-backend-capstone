from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=4, title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream  : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        item_one = Menu.objects.create(id=5, title="Gnocchi", price=20, inventory=150)
        self.assertEqual(str(item_one), "Gnocchi  : 20")
    def test_getall(self):
        super(MenuViewTest, self).setUp()