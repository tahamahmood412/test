from django.contrib import admin
from .models import Chapter, Question, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    list_filter = ('subject',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'get_question_type', 'marks', 'chapter', 'subject')
    list_filter = ('chapter', 'subject', 'question_type')
    search_fields = ('sr_no', 'short_question', 'long_question', 'numerical_question', 'chapter__title', 'subject__name')

    def get_question_type(self, obj):
        return obj.get_question_type_display()
    get_question_type.short_description = 'Question Type'  # Sets column header in admin

@admin.register(Question)
class CustomQuestionAdmin(QuestionAdmin):
    pass
