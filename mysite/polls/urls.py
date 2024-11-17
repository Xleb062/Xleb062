from django.urls import path

from . import views

urlpatterns = [
    # .../polls/
    path("", views.index, name="index"),
    # .../polls/detail
    path("<int:question_id>/detail/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]

#  http://127.0.0.1:8000/polls



















