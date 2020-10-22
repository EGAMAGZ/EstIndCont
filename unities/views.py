from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.db.models import QuerySet

from .models import Unity, UnityContent

# Create your views here.
class UnityListContent(ListView):
    template_name = 'unities/unity_content_list.html'
    context_object_name = 'content_list'

    def get_queryset(self) -> QuerySet:
        unity = Unity.objects.get(slug=self.kwargs['unity_slug'])
        return UnityContent.objects.filter(unity=unity)

class UnityContentView(View):
    
    template_name = 'unities/unity_content.html'

    def get(self, request, unity_slug, topic_slug,*args,**kwargs) -> HttpResponse:
        content = UnityContent.objects.get(slug=topic_slug)
        return render(request, self.template_name, {'content':content})
