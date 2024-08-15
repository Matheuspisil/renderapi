
from django.test import TestCase
from django.urls import resolve, reverse

class TestUrls(TestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_emconstrucao_url(self):
        url = reverse('emconstrucao')
        self.assertEqual(url, '/emconstrucao/')

