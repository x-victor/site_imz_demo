from django.views.generic import ListView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles-list.html'
    paginate_by = 10
    context_object_name = 'articles'
