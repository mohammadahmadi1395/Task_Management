from django.urls import path

from . import views

urlpatterns = [
    # ex: /tasks/
    path('', views.index, name='index'),
    # ex: /tasks/5/
    path('tasks/<int:question_id>/', views.detail, name='detail'),
    # ex: /tasks/5/results/
    path('tasks/<int:question_id>/results/', views.results, name='results'),
    # ex: /tasks/5/vote/
    path('tasks/<int:question_id>/vote/', views.vote, name='vote'),
]