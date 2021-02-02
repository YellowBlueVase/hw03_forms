from django.test import TestCase
from django.utils import timezone

from posts.models import Group, Post, User


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            id=1,
            title='Monkeys',
            slug='monkeys',
            description='Group about monkeys'
        )
        cls.group = Group.objects.get(id=1)

    def test_group_verboso_name(self):
        group = GroupModelTest.group
        field_verboses = {
            'title': 'Название группы',
            'slug': 'Слаг группы',
            'description': 'Описание группы',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).verbose_name, expected)

    def test_group_help_text_name(self):
        group = GroupModelTest.group
        field_help_texts = {
            'title': 'Обязательное поле для заполнения',
            'slug': 'Обязательное поле для заполнения, уникальное',
            'description': 'Обязательное поле для заполнения',
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).help_text, expected)

    def test_group_self_name(self):
        group = GroupModelTest.group
        self_name_target = group.title
        self_name_actual = str(group)
        self.assertEquals(self_name_target, self_name_actual)  


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Post.objects.create(
            text='Random text for test',
            pub_date=timezone.now(),
            author=User.objects.create_user(username='Donkey'),
            group=Group.objects.create(title="Monkeys", slug="monkeys", description="some description"),
        )
        cls.post = Post.objects.get(id=1)

    def test_post_verboso_name(self):
        post = PostModelTest.post
        field_verboses = {
            'text': 'Текст публикации',
            'pub_date': 'Дата публикации',
            'author': 'Автор публикации',
            'group': 'Группа публикаций',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).verbose_name, expected)

    def test_post_help_text_name(self):
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Обязательное поле для заполнения',
            'pub_date': 'Автоматическое заполнение',
            'author': 'Автоматическое заполнение',
            'group': 'Не обязательное поле для заполнения',
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).help_text, expected)

    def test_post_self_name(self):
        post = PostModelTest.post
        length_self_name_target = 15
        length_self_name_actual = (len(str(post)))
        self.assertIs(length_self_name_actual <= length_self_name_target, True) 