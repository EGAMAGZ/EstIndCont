from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render

from core.models import TeamMember
from util.mixins import VisitContextMixin

# Create your views here.
# https://medium.com/@MicroPyramid/handling-custom-error-pages-404-500-in-django-ff1f9e0cf2b5
class AboutUsView(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/aboutus.html'
    context_object_name = 'team_members'

# class Home(VisitContextMixin, ListView):
#     model = UnityContent
#     template_name = 'core/home.html'
#     context_object_name = 'last_posts'
#     queryset = UnityContent.objects.order_by('-created')[:5]

class Home(VisitContextMixin, TemplateView):
    template_name = 'core/home.html'


def handler404(request, exception) -> HttpResponse:
    return render(request,'core/404.html', status=404)

def handler500(request) -> HttpResponse:
    return render(request, 'core/500.html', status=500)
