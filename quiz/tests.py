from django.test import TestCase
from .models import Quiz, Question, Choice, Category
import pandas as pd
import io
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from django.contrib.auth.models import User
from django.urls import reverse

class QuizModelTest(TestCase):
    # setup
    def setUp(self):
        # category
        self.category = Category.objects.create(name='AI')

        # create excel file
        self.excel_file = io.BytesIO()
        df = pd.DataFrame({
            'Question': ['What is 2+2?', 'What is 3+5?'], 
            'A': ['1', '2'], 
            'B': ['3', '4'], 
            'C': ['5', '8'], 
            'D': ['4', '9'], 
            'Answer': ['D', 'C']
        })
        df.to_excel(self.excel_file, index=False, engine="openpyxl")
        self.excel_file.seek(0)

        self.uploaded_file = SimpleUploadedFile('test_quiz.xlsx', self.excel_file.read(), content_type='application/vnd.ms-excel')

        # quiz
        self.quiz = Quiz.objects.create(
            title='Quiz title', 
            description='Quiz desc', 
            category=self.category, 
            quiz_file=self.uploaded_file
        )

    @patch('quiz.models.pd.read_excel')
    def test_import_quiz_from_excel(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'Question': ['What is 2+2?', 'What is 3+5?'], 
            'A': ['1', '2'], 
            'B': ['3', '4'], 
            'C': ['5', '8'], 
            'D': ['4', '9'], 
            'Answer': ['D', 'C']
        })

        mock_read_excel.return_value = mock_df

        self.quiz.save()

        # questions are created or not
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Choice.objects.count(), 8)

        question1 = Question.objects.get(text='What is 2+2?')
        question2 = Question.objects.get(text='What is 3+5?')

        self.assertEqual(Choice.objects.filter(question=question1).count(), 4)
        self.assertEqual(Choice.objects.filter(question=question2).count(), 4)

    # str
    # additionals
    def test_plural_quizzes(self):
        self.assertEqual(str(Quiz._meta.verbose_name_plural), 'Quizzes')


# Template Test 


class AllQuizTemplateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.category1 = Category.objects.create(name='Science')
        self.category2 = Category.objects.create(name='English')

        self.quiz1 = Quiz.objects.create(title='Quiz 1', description='Desc 1', category=self.category1)
        self.quiz2 = Quiz.objects.create(title='Quiz 2', description='Desc 2', category=self.category2)


    def test_all_quiz_template(self):
        response = self.client.get(reverse('all_quiz'))

        self.assertTemplateUsed(response, 'all-quiz.html')

        self.assertIn('quizzes', response.context)
        self.assertIn('categories', response.context)

        self.assertContains(response, 'Quiz 1')
        self.assertContains(response, 'Quiz 2')
        self.assertContains(response, 'Science')
        self.assertContains(response, 'English')

    def test_no_quizzes(self):
        Quiz.objects.all().delete()

        response = self.client.get(reverse('all_quiz'))

        self.assertContains(response, 'There is no quiz available for this category or search.')
