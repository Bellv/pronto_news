from django.test import TestCase

from ..admin import PostAdmin

class PostAdminTest(TestCase):
    def test_post_admin_should_be_accessible(self):
        response = self.client.get('/admin/posts/post/')
        self.assertTrue(response.status_code, 302)

    def test_post_admin_should_set_list_dispaly(self):

        expected = (
            'title',
            'url',
            'number_of_votes'
        )

        self.assertEqual(PostAdmin.list_display, expected)

    def test_search_admin_shoud_seact_title(self):

        expected = [
            'title'
        ]

        self.assertEqual(PostAdmin.search_fields, expected)
