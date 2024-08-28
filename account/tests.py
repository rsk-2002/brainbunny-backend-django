from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from quiz.models import QuizSubmission, Quiz, Category
from django.urls import reverse

class ProfileViewTest(TestCase):
    # setup
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # profile
        self.profile = Profile.objects.create(user=self.user, bio='This is bio')

        self.category = Category.objects.create(name='Science')
        # quiz
        self.quiz = Quiz.objects.create(
            title='Quiz title', 
            description='Desc', 
            category=self.category,
        )
        
        # submisssion
        self.submission = QuizSubmission.objects.create(user=self.user, quiz=self.quiz, score=7)

    def test_profile_view(self):
        # Login the user
        self.client.login(username='testuser', password='testpass')

        # response
        url = reverse('profile', args=[self.user.username])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'profile.html')

        self.assertEqual(response.context['user_profile2'], self.profile)
        self.assertIn(self.submission, response.context['submissions'])

    def test_profile_view_redirect(self):
        url = reverse('profile', args=[self.user.username])
        response = self.client.get(url)

        self.assertRedirects(response, f'/user/login?next={url}')