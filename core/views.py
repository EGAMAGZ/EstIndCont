from core.models import TeamMember
from unities.models import Unity
from django.views.generic.list import ListView


# Create your views here.
from util.mixins import VisitContextMixin


class UnityList(VisitContextMixin, ListView):
    model = Unity
    context_object_name = 'unities_list'
    template_name = 'core/unities_list.html'


class TeamMembersList(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/team_members_list.html'
