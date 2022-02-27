from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Quiz
from random import shuffle

# Create your views here.
class QuizzListView(ListView):
    model = Quiz
    template_name = 'quizz_app/main.html'
    context_object_name = 'quizes'
    ordering = ['quiz_id']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


def view_404(request, *args, **kwargs):
    return redirect('https://mateuszk-quizz.herokuapp.com')

def quiz_view(request, quiz_id):
    return render(request, 'quizz_app/quiz.html', {'title': f'{quiz_id} - Have fun!'})


def quiz_data(request, quiz_id):
    quiz = Quiz.objects.get(quiz_id=quiz_id)

    # append quiz's questions to json response
    questions = [
        {
            'question': str(q),
            'answers': [{'text': str(a.text), 'correct': a.correct} for a in q.get_answer()]
        }
        for q in quiz.get_questions()
        ]

    for question in questions:
        shuffle(question['answers'])

    return JsonResponse({
        'data': questions
    })
