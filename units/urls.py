from django.urls import path

from units.views import UnitListView, UnitDetailView, UnitMemberDetailView

urlpatterns = [
    path('', UnitListView.as_view(), name='units-home'),
    path('<slug:slug>/', UnitDetailView.as_view(), name='units-detail'),
    path('member/<uuid:pk>/', UnitMemberDetailView.as_view(), name='units-member-detail'),
]
