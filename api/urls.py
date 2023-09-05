from django.urls import path, include
from rest_framework import routers

from api.views import *

router = routers.SimpleRouter()
router.register(r"type_of_question", TypeOfQuestionViewSet)
router.register(r"wrong_answer", WrongAnswerViewSet)
router.register(r"right_answer", RightAnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"difficult", DifficultViewSet)
router.register(r"level", LevelViewSet)
router.register(r"stage", StageViewSet)
urlpatterns = [
    path('', include(router.urls))
]
