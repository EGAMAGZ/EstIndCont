from typing import Any, Dict
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import QuerySet
from django.shortcuts import get_list_or_404

from util.mixins import VisitContextMixin
from .models import Unity, UnityContent


# Create your views here.
class UnityListContent(VisitContextMixin, ListView):
    template_name = 'unities/unity_content_list.html'
    context_object_name = 'content_list'
    allow_empty = False

    def get_queryset(self) -> QuerySet:
        return get_list_or_404(UnityContent, unity__slug=self.kwargs['unity_slug'])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context['unity'] = Unity.objects.get(slug=self.kwargs['unity_slug'])
        return context

class UnityContentView(VisitContextMixin, DetailView):
    template_name = 'unities/unity_content.html'
    context_object_name = 'content'
    model = UnityContent
    slug_url_kwarg = 'topic_slug'
