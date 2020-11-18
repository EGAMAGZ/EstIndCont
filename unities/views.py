from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import QuerySet

from util.mixins import VisitContextMixin
from .models import Unity, UnityContent


# Create your views here.
class UnityListContent(VisitContextMixin, ListView):
    template_name = 'unities/unity_content_list.html'
    context_object_name = 'content_list'

    def get_queryset(self) -> QuerySet:
        unity = Unity.objects.get(slug=self.kwargs['unity_slug'])

        return UnityContent.objects.filter(unity=unity)

class UnityContentView(VisitContextMixin, DetailView):

    template_name = 'unities/unity_content.html'
    context_object_name = 'content'
    model = UnityContent
    slug_url_kwarg = 'topic_slug'
