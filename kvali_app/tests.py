from django.test import TestCase
from django.urls import reverse


class HealthEndpointIntegrationTest(TestCase):
    def test_root_endpoint_returns_200(self):
        url = reverse("kvali_index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
