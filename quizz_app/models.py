from django.db import models


DIFFICULT_CHOICES = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard')
)


class Quiz(models.Model):
    quiz_id = models.PositiveSmallIntegerField(primary_key=True)
    category = models.CharField(max_length=30, blank=False)
    number_of_questions = models.PositiveSmallIntegerField(blank=False)
    difficulty = models.CharField(max_length=30, choices=DIFFICULT_CHOICES, blank=False)


    def __str__(self):
        return f'{self.category}'
    

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]


    class Meta:
        verbose_name_plural = 'Quizes'
        ordering = ['quiz_id']
