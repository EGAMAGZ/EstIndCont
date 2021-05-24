from core.form import ContactForm
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib import messages

from core.models import ProsoftDoc, TeamMember
from util.mixins import VisitContextMixin

# Create your views here.
# https://medium.com/@MicroPyramid/handling-custom-error-pages-404-500-in-django-ff1f9e0cf2b5
class AboutUsView(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/aboutus.html'
    context_object_name = 'team_members'

class HomeView(VisitContextMixin, ListView):
    model = ProsoftDoc
    template_name = 'core/home.html'
    context_object_name = 'last_docs'
    queryset = ProsoftDoc.objects.order_by('-created')[:5]


class PortafolioView(VisitContextMixin, TemplateView):
    template_name = 'core/portafolio.html'

class ContactView(VisitContextMixin, FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form) -> HttpResponse:
        
        messages.success(self.request, 'Mensaje de contacto correctamente creado')

        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


def handler404(request,exception) -> HttpResponse:
    return render(request,'core/404.html', status=404)

def handler500(request) -> HttpResponse:
    return render(request, 'core/500.html', status=500)
