from typing import Dict, Iterable, List

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.db.models import QuerySet

from core.models import TeamMember
from util.mixins import VisitContextMixin
from unities.models import UnityContent, Unity

# Create your views here.
# https://medium.com/@MicroPyramid/handling-custom-error-pages-404-500-in-django-ff1f9e0cf2b5
class TeamMembersList(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/team_members_list.html'
    context_object_name = 'team_members'

class Home(VisitContextMixin, ListView):
    model = UnityContent
    template_name = 'core/home.html'
    context_object_name = 'last_posts'
    queryset = UnityContent.objects.order_by('-created')[:5]


def handler404(request, exception) -> HttpResponse:
    try:
        if not request.session['page_visited_session']:
            request.session['page_visited_session'] = True
    except KeyError:
        request.session['page_visited_session'] = False

    return render(request,'core/404.html', {
        'page_visited': request.session['page_visited_session']
        # 'menu_elements': get_info_menu()
        }, status=404)

def handler500(request) -> HttpResponse:
    return render(request, 'core/500.html', status=500)

def get_info_menu(self) -> Iterable[Dict[str,str]]:
    menu_info:List[Dict[str,str]] = []
    for unity in Unity.objects.all():
        list_content_info = []
        for content in UnityContent.objects.filter(unity=unity):
            list_content_info.append({
                'url': content.get_absolute_url(),
                'title': content.title
            })
        menu_info.append({
            'unity_number': unity.number,
            'slug': unity.slug,
            'content': list_content_info,
            'name': unity.name
        })
    return menu_info
