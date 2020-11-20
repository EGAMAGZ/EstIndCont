from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from core.models import TeamMember
from util.mixins import VisitContextMixin


# Create your views here.
class TeamMembersList(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/team_members_list.html'
    context_object_name = 'team_members'

class Home(VisitContextMixin,TemplateView):
    template_name = 'core/home.html'
