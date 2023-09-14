from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    likes = models.ManyToManyField(User, related_name='question_post')
    dates_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - Question'

    def get_absolute_url(self):
        return reverse('stackbase:question-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    question = models.ForeignKey(Question, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_success_url(self):
        return reverse('stackbase:question-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)