from django.urls import path, include, re_path
from rest_framework import routers

from api.views import *

router = routers.SimpleRouter()
router.register(r"wrong_answer", WrongAnswerViewSet)
router.register(r"right_answer", RightAnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"level", LevelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('filter-questions/<int:level_id>/', FilterQuestionsByLevel.as_view(), name='filter-questions-by-level'),
    path('get-level/<int:question_id>/', GetLevelByQuestion.as_view(), name='get-level-by-question'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
