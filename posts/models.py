from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название группы", 
        help_text="Обязательное поле для заполнения",
        )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг группы", 
        help_text="Обязательное поле для заполнения, уникальное",
        )
    description = models.TextField(
        verbose_name="Описание группы", 
        help_text="Обязательное поле для заполнения",
        )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст публикации", 
        help_text="Обязательное поле для заполнения",
        )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", 
        help_text="Автоматическое заполнение",
        auto_now_add=True,
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор публикации", 
        help_text="Автоматическое заполнение",
        )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группа публикаций", 
        help_text="Не обязательное поле для заполнения",
        )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text[:15]
