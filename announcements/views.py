from django.views.generic import ListView, DetailView

from announcements.models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcements-list.html'
    context_object_name = 'announcements'
    paginate_by = 10


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcements-detail.html'
