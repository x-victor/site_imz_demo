from django.urls import path

from main.views import IndexPageView, PageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index-page'),
    path('menu/<slug:slug>/page', PageView.as_view(), name='menu-page'),
]
