from django.db import models
from quizz_app.models import Quiz

class Question(models.Model):
    text = models.CharField(max_length=250, blank=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.text)


    def get_answer(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=250, blank=False)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return f'Q: {self.question.text}, A: {self.text}, C: {self.correct}'