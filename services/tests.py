from django.test import TestCase
from .models import Service, ServiceImage

class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name_services="Limpieza",
            description="Servicio de limpieza general",
            price=100.00
        )


    def test_service_creation(self):
        self.assertEqual(self.service.name_services, "Limpieza")
        self.assertEqual(self.service.description, "Servicio de limpieza general")
        self.assertEqual(self.service.price, 100.00)


