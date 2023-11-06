from django.contrib.auth.models import AbstractUser
from django.db import models


class WrongAnswer(models.Model):
    answer = models.CharField(max_length=127)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.answer}, {self.question}"


class RightAnswer(models.Model):
    answer = models.CharField(max_length=127, blank=False, null=False)

    def __str__(self):
        return f"{self.answer}"


class Question(models.Model):
    question = models.CharField(max_length=127, blank=False, null=False)
    right_answer = models.OneToOneField(RightAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}, {self.right_answer}"


class Level(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    questions = models.ManyToManyField(Question)
    image = models.ImageField()

    def __str__(self):
        return self.name
