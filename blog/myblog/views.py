from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            'myblog/home.html',
            context={'page_obj': page_obj}
        )
