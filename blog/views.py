from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Post, Tag


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'blog/post-detail.html'


class PostListView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'blog/post-list.html'

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        if tag := self.request.GET.get('tag'):
            queryset = queryset.filter(tags__name=tag)
        return queryset.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['selected_tag'] = self.request.GET.get('tag')
        print(context['selected_tag'])
        return context
