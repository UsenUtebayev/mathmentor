from django.urls import path, include
from rest_framework import routers

from api.views import *

router = routers.SimpleRouter()
router.register(r"wrong_answer", WrongAnswerViewSet)
router.register(r"right_answer", RightAnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"level", LevelViewSet)
urlpatterns = [
    path('', include(router.urls))
]
