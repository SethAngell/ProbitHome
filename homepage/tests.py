from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.
## Consider using TestCase instead of SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_evan_page_statues_code(self):
        response = self.client.get('/EvanPatterson/')
        self.assertEqual(response.status_code, 200)

    def test_seth_page_statues_code(self):
        response = self.client.get('/SethAngell/')
        self.assertEqual(response.status_code, 200)