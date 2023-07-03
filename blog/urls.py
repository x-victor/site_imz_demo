from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog-detail'),
]
