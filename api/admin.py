from django.contrib import admin

from api.models import *


# Register your models here.
@admin.register(TypeOfQuestion)
class TypeOfQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(WrongAnswer)
class WrongAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(RightAnswer)
class RightAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Difficult)
class DifficultAdmin(admin.ModelAdmin):
    pass


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass
