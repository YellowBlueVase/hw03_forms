from django.shortcuts import get_object_or_404, redirect, render
from .models import Group, Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
