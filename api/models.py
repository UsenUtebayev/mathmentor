from django.db import models


class TypeOfQuestion(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)

    def __str__(self):
        return f"Тип уровня: {self.name}"


class WrongAnswer(models.Model):
    name = models.CharField(max_length=127)
    answer = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.name}, {self.answer}"


class RightAnswer(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    answer = models.CharField(max_length=127, blank=False, null=False)

    def __str__(self):
        return f"{self.name}, {self.answer}"


class Question(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    question = models.CharField(max_length=127, blank=False, null=False)
    type_of_question = models.ForeignKey(TypeOfQuestion, on_delete=models.CASCADE)
    wrong_answers = models.ManyToManyField(WrongAnswer)
    right_answer = models.OneToOneField(RightAnswer, on_delete=models.CASCADE)
    difficult = models.ForeignKey("Difficult", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.question}, {self.type_of_question}, {self.right_answer}"


class Difficult(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Level(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    levels = models.ManyToManyField(Level)
    image = models.ImageField()

    def __str__(self):
        return self.name
