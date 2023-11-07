import random

from rest_framework import viewsets, generics
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


class FilterQuestionsByLevel(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        level_id = self.kwargs['level_id']
        return Question.objects.filter(level__id=level_id)


class GetLevelByQuestion(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def get_object(self):
        question_id = self.kwargs['question_id']
        return Level.objects.filter(questions__id=question_id).first()
