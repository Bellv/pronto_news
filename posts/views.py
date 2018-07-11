from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from .models import Post

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        html = '<ul>'
        for post in posts:
            html += f'<li><a href="{post.url}" target="_blank">' \
                f'{post.title}</a></li>'
        
        html += '</ul>'

        return HttpResponse(html)
