from django.urls import path

from . import views

# добавил для работы reverse()
app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>/", views.group_posts, name="group_posts"),
    path("new/", views.new_post, name="new_post"),
]
