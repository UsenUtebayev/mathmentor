from rest_framework.serializers import ModelSerializer

from api.models import *


class TypeOfQuestionSerializer(ModelSerializer):
    class Meta:
        model = TypeOfQuestion
        fields = "__all__"


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


class DifficultSerializer(ModelSerializer):
    class Meta:
        model = Difficult
        fields = "__all__"


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class StageSerializer(ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"
