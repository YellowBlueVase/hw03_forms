from django.test import Client, TestCase
from django.urls import reverse
from posts.forms import PostForm
from posts.models import Post, Group, User
from django.utils import timezone


class PostCreateFormTests(TestCase):
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
        self.guest_client = Client()
        self.user = User.objects.get(username='Donkey')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Тестовый текст',
        }
        # !!! Тут тоже reverse эта проблемка
        response = self.authorized_client.post(
            reverse('posts:index'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, '/new/')
        self.assertEqual(Post.objects.count(), posts_count+1)