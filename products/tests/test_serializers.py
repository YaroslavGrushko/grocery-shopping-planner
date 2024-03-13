from django.test import TestCase
from django.contrib.auth.models import User

from products.serializers import CategorySerializer

class SerializersTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="test")
        
        class TestRequest:
            def __init__(self, user):
                self.user = user

        testRequest = TestRequest(self.user)
        self.context = {"request": testRequest}

    def test_category_serializer_no_name(self):
        category_data = {
            'name': '',
        }
        serializer = CategorySerializer(data=category_data, context=self.context)
        
        self.assertEqual(serializer.is_valid(), False)

    def test_category_serializer_with_name(self):
        category_data = {
            'name': 'Test Name',
        }
        serializer = CategorySerializer(data=category_data, context=self.context)
        
        self.assertEqual(serializer.is_valid(), True)