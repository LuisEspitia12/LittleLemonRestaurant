from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title='Menu 1', price=15.99 , inventory = 80)
        Menu.objects.create(title='Menu 2', price=17.99 , inventory = 70)
        Menu.objects.create(title='Menu 3', price=22.99, inventory = 50)

    def test_getall(self):
         # Retrieve all Menu objects added for the test purpose
        response = self.client.get('/restaurant/menu/')  # Simula una solicitud GET a la URL de la vista
        
        # Verifica si la solicitud fue exitosa (código de estado HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Serialize the retrieved objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)