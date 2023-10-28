from rest_framework import viewsets

from api.models import *
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


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer



