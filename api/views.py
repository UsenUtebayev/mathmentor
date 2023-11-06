import random

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializer import *


class WrongAnswerViewSet(viewsets.ModelViewSet):
    queryset = WrongAnswer.objects.all()
    serializer_class = WrongAnswerSerializer
    filterset_fields = ['question']


class RightAnswerViewSet(viewsets.ModelViewSet):
    queryset = RightAnswer.objects.all()
    serializer_class = RightAnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['GET'])
    def get_question_instance(self, request, pk=None):
        instance = self.get_object()
        wrong_answers = WrongAnswer.objects.filter(question=instance)
        right_answers = RightAnswer.objects.filter(question=instance)
        answers = []

        for i in wrong_answers:
            answers.append(i.answer)

        answers.append(right_answers[0].answer)

        random.shuffle(answers)
        custom_data = {
            "question": instance.question,
            "answers": answers,
            "right_answer": right_answers[0].answer,
            "pk": instance.pk
        }
        return Response(custom_data)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
