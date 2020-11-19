from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from core.models import TeamMember
from unities.models import Unity
from util.mixins import VisitContextMixin


# Create your views here.
class UnityList(VisitContextMixin, ListView):
    model = Unity
    context_object_name = 'unities_list'
    template_name = 'core/unities_list.html'


class TeamMembersList(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/team_members_list.html'

class Home(VisitContextMixin,TemplateView):
    template_name = 'core/unities_list.html'

