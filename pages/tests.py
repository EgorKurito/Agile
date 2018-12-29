from django.test import TestCase


class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/pages/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)