from django.contrib.auth import get_user_model
from django.forms.widgets import Textarea
from django.test import Client, TestCase
from django.urls import reverse
from django import forms
from posts.models import Post, Group, User
from django.utils import timezone


class PostPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Post.objects.create(
            text='Random text for test',
            pub_date=timezone.now(),
            author=User.objects.create_user(username='Donkey'),
            group=Group.objects.create(title="Monkeys", slug="monkeys", description="some description"),
        )

    def setUp(self):
        self.user = User.objects.get(username='Donkey')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # !!! Вот этот дурацкий код, из-за которого решил все эти манипуляции провести. 
    # Короче не смог выполнить задания по test_views.py и test_forms.py
    def test_pages_uses_correct_template(self):
        templates_pages_names = {
            'index.html': reverse('posts:index'),
            'group.html': reverse('posts:group_posts'),
            'new_post.html': reverse('posts:new_post'),
        }
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template) 

  # !!! И вот еще этот reverse
    def test_new_post_page_show_correct_context(self):
        response = self.authorized_client.get(reverse('posts:new_post'))
        form_fields = {
            'text': forms.fields.CharField(widget=Textarea),         
            'group': forms.fields.ChoiceField,
        }        

        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected)