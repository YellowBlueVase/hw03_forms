from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        "index.html",
        {'page': page,}
    )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
        return render(request, "new_post.html", {"form": form})
    form = PostForm()
    return render(request, "new_post.html", {"form": form})


# ДОБАВИЛ НОВЫЕ ФУНКЦИИ + ТЕМПЛЕЙЕТЫ ДЛЯ УРОКОВ ПО ПРОФИЛЮ ПОЛЬЗОВАТЕЛЯ В СПРИНТЕ 5
# Страницу профайла пользователя с постами. Добавьте на неё паджинатор, количество записей автора вы умеете вычислять
def profile(request, username):
    author_posts = Post.objects.all().filter(author=username)
    count_posts = author_posts.count()
    full_name = request.user.get_full_name()
    return render(request, "profile.html", {
        "username": username,
        "count_posts": count_posts,
        "full_name": full_name,
    })

# Страницу просмотра отдельной записи
def post_view(request, username, post_id):
    return render(request, "post.html", {})

#Страницу с формой редактирования существующей записи: расширьте готовый шаблон с формой создания поста. 
# В зависимости от ситуации заголовок формы должен меняться: «Добавить запись» или «Редактировать запись». 
# Надпись на кнопке отправки формы тоже должна зависеть от операции: «Добавить» для новой записи и «Сохранить» 
# — для редактирования.
def post_edit(request, username, post_id):
    if username == Post.objects.get(id=post_id).author:
        return render(request, "new_post.html", {})
    else:
        pass


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию, 
    # выводить её в шаблон пользователской страницы 404 мы не станем
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500) 