from django.test import Client, TestCase
from django.utils import timezone

from posts.models import Group, Post, User


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создадим запись в БД для проверки доступности адреса task/test-slug/
        Post.objects.create(
            text='Random text for test',
            pub_date=timezone.now(),
            author=User.objects.create_user(username='Donkey'),
            group=Group.objects.create(title="Monkeys", slug="monkeys", description="some description"),
        )

    def setUp(self):
        # Создаем экземпляр клиента
        self.guest_client = Client()
        self.user = User.objects.get(username='Donkey')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.public_pages = ['/', '/group/monkeys/']
        self.private_pages = ['/new/']

    def test_public_urls_exist_at_desired_location(self):
        for page in self.public_pages:
            response = self.guest_client.get(page)
            with self.subTest():
                self.assertEqual(response.status_code, 200)

    def test_private_urls_exist_at_desired_location(self):
        for page in self.private_pages:
            response = self.authorized_client.get(page)
            with self.subTest():
                self.assertEqual(response.status_code, 200)

    def test_private_urls_redirect_anonymous(self):
        for page in self.private_pages:
            response = self.guest_client.get(page, follow=True)
            with self.subTest():
                self.assertRedirects(response, '/auth/login/?next=/new/')

    def test_urls_uses_correct_template(self):
        templates_url_names = {
            'index.html': '/',
            'group.html': '/group/monkeys/',
            'new_post.html': '/new/',
        }
        for template, reverse_name in templates_url_names.items():
            with self.subTest():
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
