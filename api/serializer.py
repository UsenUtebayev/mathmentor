from rest_framework.serializers import ModelSerializer

from api.models import *


class WrongAnswerSerializer(ModelSerializer):
    class Meta:
        model = WrongAnswer
        fields = "__all__"


class RightAnswerSerializer(ModelSerializer):
    class Meta:
        model = RightAnswer
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"
