from django.urls import path

from . import views

# добавил для работы reverse()
app_name = "about"

urlpatterns = [
    path("author/", views.AboutAuthorView.as_view(), name="author"), #изменено свойство name
    path("tech/", views.AboutTechView.as_view(), name='tech'),
]
