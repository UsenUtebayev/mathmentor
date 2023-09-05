from rest_framework import viewsets

from api.models import *
from api.serializer import *


class TypeOfQuestionViewSet(viewsets.ModelViewSet):
    queryset = TypeOfQuestion.objects.all()
    serializer_class = TypeOfQuestionSerializer


class WrongAnswerViewSet(viewsets.ModelViewSet):
    queryset = WrongAnswer.objects.all()
    serializer_class = WrongAnswerSerializer


class RightAnswerViewSet(viewsets.ModelViewSet):
    queryset = RightAnswer.objects.all()
    serializer_class = RightAnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class DifficultViewSet(viewsets.ModelViewSet):
    queryset = Difficult.objects.all()
    serializer_class = DifficultSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
