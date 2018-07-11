from django.conf.urls import url

from .views import PostListView


urlpatterns = [
    url('', PostListView.as_view(), name='post_list'),
]
