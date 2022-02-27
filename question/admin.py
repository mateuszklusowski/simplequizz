from django.contrib import admin
from .models import Answer, Question

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer


admin.site.register(Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
