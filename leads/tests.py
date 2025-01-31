from django.test import TestCase
from django.urls import reverse

class LandingPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('landing-page'))
        self.assertTemplateUsed(response, 'landing.html')

    # def test_contains_correct_html(self):
    #     response = self.client.get(reverse('landing-page'))
    #     self.assertContains(response, '<h1>Landing Page</h1>')

    def test_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('landing-page'))
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    # def test_url_resolves_landing_page_view(self):
    #     view = resolve('/')
    #     self.assertEqual(view.func, landing_page)



# class TestHomePage(TestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_home_page_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'home.html')

#     def test_home_page_contains_correct_html(self):
#         response = self.client.get('/')
#         self.assertContains(response, '<h1>Home</h1>')

#     def test_home_page_does_not_contain_incorrect_html(self):
#         response = self.client.get('/')
#         self.assertNotContains(response, 'Hi there! I should not be on the page.')

#     def test_home_page_url_resolves_home_page_view(self):
#         view = resolve('/')
#         self.assertEqual(view.func, home)