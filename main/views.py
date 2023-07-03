from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView

from announcements.models import Announcement
from articles.models import Article
from blog.models import Post
from main.models import Menu, Page


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(published=True).order_by('-created_at')[:3]
        context['announcements'] = Announcement.objects.order_by('-created_at')[:3]
        context['articles'] = Article.objects.order_by('-created_at')[:3]
        context['menu'] = Menu.objects.filter(
            is_active=True,
            parent=None
        ).order_by('name').select_related('page').prefetch_related('children__page')
        return context


class PageView(DetailView):
    queryset = Page.objects.all()
    template_name = 'main/page-detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Page, menu__slug=self.kwargs['slug'])
