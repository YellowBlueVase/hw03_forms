from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path

handler404 = "posts.views.page_not_found" #noqa
handler500 = "posts.views.server_error" #noqa

# Ниже в трех путях прописал внутри include дополнительные названия + name spaces. Например, 
# для users.urls название "users" добавил и namespace="users"
# дополнительно в users/urls.py добавил app_name="users", по аналогии в posts/urls.py и about/urls.py
# все это сделал, чтобы заработал код в posts/tests/test_views.py и test_forms.py в части reverse() в соответствии с заданием
urlpatterns = [
    path("auth/", include(("users.urls", "users"), namespace="users")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include(("posts.urls", "posts"), namespace="posts")),
    path("admin/", admin.site.urls),
    path("about/", include(("about.urls", "about"), namespace="about"))
]
