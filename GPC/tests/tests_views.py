from django.test import TestCase, Client

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_emconstrucao_view(self):
        response = self.client.get('/emconstrucao/')
        self.assertEqual(response.status_code, 200)
