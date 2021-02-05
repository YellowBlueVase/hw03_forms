from django.urls import path

from . import views

# добавил для работы reverse()
#app_name = "users"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup")
]
