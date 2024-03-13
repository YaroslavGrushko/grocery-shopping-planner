from django.contrib.auth.models import User
from django.test import TestCase

from products.models import Category, Product
from django.core.exceptions import ValidationError

class ModelsTestCase(TestCase):
    def test_product_negative_price(self):
        user = User.objects.create(username="test")
        category = Category.objects.create(user=user, name="test_category")
        product = Product.objects.create(name="test_product", quantity=2, price=-1, category=category, )
        
        with self.assertRaises(ValidationError) as context:
            product.full_clean()

        self.assertEqual(context.exception.messages[0], 'Будь ласка вкажіть коректну ціну.')

    def test_product_positive_price(self):
        user = User.objects.create(username="test")
        category = Category.objects.create(user=user, name="test_category")
        product = Product.objects.create(name="test_product", quantity=2, price=20, category=category, )
    
        product.full_clean()
