from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
class tests(TestCase):
    username= 'test'
    email= 'test@test.com'

    def test_home(self):
        response= self.client.get(reverse('home'))
        response2= self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response2, 'home.html')

    def test_SignUp_Response(self):
        response= self.client.get(reverse('signup'))
        response2= self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertTemplateUsed(response2, 'signup.html')


    def test_SignUp_Form(self):
        user=get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)
