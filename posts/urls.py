from django.urls import path

from . import views

# добавил для работы reverse()
app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>/", views.group_posts, name="group_posts"),
    path("new/", views.new_post, name="new_post"),
    # ДОБАВИЛ НОВЫЕ ПУТИ ДЛЯ УРОКОВ ПО ПРОФИЛЮ ПОЛЬЗОВАТЕЛЯ В СПРИНТЕ 5
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/<int:post_id", views.post_view, name="post"),
    path("<str:username>/<int:post_id>/edit/", views.post_edit, name="post_edit"),
]
