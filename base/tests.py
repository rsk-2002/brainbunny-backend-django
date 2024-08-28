from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
from django.urls import reverse

class MessageModelTest(TestCase):
    # set up
    def setUp(self):
        # create user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # create a sample message
        self.message = Message.objects.create(
            user=self.user, 
            subject='Message subject', 
            message='This is my message'
        )

    # test creation
    def test_message_creation(self):
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.subject, 'Message subject')
        self.assertEqual(self.message.message, 'This is my message')

        self.assertFalse(self.message.is_read)

        self.assertIsNotNone(self.message.created_at)

    # str representation
    def test_str_representation(self):
        self.assertEqual(str(self.message), f"{self.user.username}, {self.message.subject}")


# Message URL test



class MessageUrlTest(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(username='superuser', password='testpass')

        self.message = Message.objects.create(
            user=self.superuser, 
            subject='Message subject', 
            message='This is my message'
        )

    def test_message_url_superuser(self):
        self.client.login(username='superuser', password='testpass')

        # response 
        url = reverse('message', args=[self.message.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    def test_message_url_normaluser(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client.login(username='testuser', password='testpass')

        # response 
        url = reverse('message', args=[self.message.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)