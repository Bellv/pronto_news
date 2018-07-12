from django.test import TestCase
from django.urls import reverse

from ..models import Post

class PostListViewTest(TestCase):
    def test_post_list_view_should_be_accessible(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_should_show_list_of_post(self):
        Post.objects.create(
            title='Hello World',
            url='http://hello.world.me'
        )
        Post.objects.create(
            title='Hello World 2',
            url='http://hello.world2.me'
        )

        response = self.client.get(reverse('post_list'))

        expected = '<li><a href="http://hello.world.me" target="_blank">Hello World</a></li>'
        self.assertContains(response, expected, status_code=200)

        expected = '<li><a href="http://hello.world2.me" target="_blank">Hello World 2</a></li>'
        self.assertContains(response, expected, status_code=200)

    def test_post_list_view_should_have_post_form(self):
        response = self.client.get(reverse('post_list'))

        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type=\'hidden\' name=\'csrfmiddlewaretoken\''
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="text" name="title" maxlength="300" required id="id_title" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<input type="url" name="url" maxlength="200" required id="id_url" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<button type="submit">Submit</button>'
        self.assertContains(response, expected, status_code=200)


    def test_post_list_view_should_save_data_when_post_data(self):
        data = {
            'title': 'Pronto Marketing',
            'url': 'https://www.prontomarketing.com'
        }
        response = self.client.post(reverse('post_list'), data=data, follow=True)

        post = Post.objects.last()
        
        self.assertEqual(post.title, 'Pronto Marketing')
        self.assertEqual(post.url, 'https://www.prontomarketing.com')
        self.assertEqual(post.number_of_votes, 0)
