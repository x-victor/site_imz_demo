from django.urls import path

from announcements.views import AnnouncementListView, AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcements-home'),
    path('<uuid:pk>/', AnnouncementDetailView.as_view(), name='announcements-detail'),
]
