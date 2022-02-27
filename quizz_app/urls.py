from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizzListView.as_view(), name='home'),
    path('<int:quiz_id>/', views.quiz_view, name='quiz'),
    path('<int:quiz_id>/data', views.quiz_data, name='quiz-data')
]