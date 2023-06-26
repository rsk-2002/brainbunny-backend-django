from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    quiz_file = models.FileField(upload_to='quiz/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title