from django.test import TestCase

from ..forms import PostForm
from ..models import Post


class PostFromTest(TestCase):
    def test_from_should_use_post_model(self):
        expected = Post
        self.assertEqual(PostForm.Meta.model, expected)

    def test_form_should_set_field(self):
        expected = [
            'title',
            'url',
        ]
        self.assertEqual(PostForm.Meta.fields, expected)
