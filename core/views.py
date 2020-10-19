from core.models import TeamMember
from unities.models import Unity
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class UnityList(ListView):
    model=Unity

class TeamMembersList(ListView):
    model=TeamMember
    template_name = 'core/team_members_list.html'
