from django.views.generic import ListView, DetailView

from units.models import Unit, Member


class UnitListView(ListView):
    model = Unit
    queryset = Unit.objects.filter(parent=None).prefetch_related('under_units')
    context_object_name = 'units'
    template_name = 'units/unit-list.html'


class UnitDetailView(DetailView):
    model = Unit
    queryset = Unit.objects.prefetch_related('under_units', 'members')
    context_object_name = 'unit'
    template_name = 'units/unit-detail.html'


class UnitMemberDetailView(DetailView):
    model = Member
    queryset = Member.objects.all().select_related('unit')
    context_object_name = 'member'
    template_name = 'units/unit-member-detail.html'
