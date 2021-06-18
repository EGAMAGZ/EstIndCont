from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from django.utils.decorators import method_decorator

from core.form import ContactForm
from core.models import ConstitucionalAct, Description, ProsoftDoc, TeamMember
from util.mixins import VisitContextMixin

# Create your views here.
# https://medium.com/@MicroPyramid/handling-custom-error-pages-404-500-in-django-ff1f9e0cf2b5
class AboutUsView(VisitContextMixin,ListView):
    model = TeamMember
    template_name = 'core/aboutus.html'
    context_object_name = 'team_members'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['document'] = ConstitucionalAct.load()

        return context

class HomeView(VisitContextMixin, ListView):
    model = ProsoftDoc
    template_name = 'core/home.html'
    context_object_name = 'last_docs'
    queryset = ProsoftDoc.objects.order_by('-created')[:5]


class PortafolioView(VisitContextMixin, TemplateView):
    template_name = 'core/portafolio.html'


class ProsoftListView(VisitContextMixin, ListView):
    template_name = "core/prosoft_list.html"
    model = ProsoftDoc
    context_object_name = "documents"
    queryset = ProsoftDoc.objects.order_by('created')


@method_decorator(xframe_options_exempt, name='dispatch')
class ProsoftDocView(VisitContextMixin, DetailView):
    template_name = 'core/prosoft_doc.html'
    context_object_name = 'document'
    model = ProsoftDoc
    slug_url_kwarg = 'document_slug'


class ContactView(VisitContextMixin, FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form) -> HttpResponse:
        
        messages.success(self.request, 'Mensaje de contacto correctamente creado')

        return self.render_to_response(
            self.get_context_data(request=self.request, form=form)
        )

class ServicesView(VisitContextMixin, TemplateView):
    template_name = 'core/services.html'


class MarketRateView(VisitContextMixin, FormView):
    template_name = 'core/market_rate.html'
    form_class = ContactForm
    success_url = '/market-rates/'

    def form_valid(self, form: ContactForm) -> HttpResponse:

        messages.success(self.request, 'Mensaje de contacto correctamente creado')

        return self.render_to_response(
            self.get_context_data(request=self.request, form=form)
        )

class DescriptionView(VisitContextMixin, TemplateView):
    template_name = 'core/description.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['document'] = Description.load()

        return context

def handler404(request, exception) -> HttpResponse:
    return render(request,'core/404.html', status=404)

def handler500(request) -> HttpResponse:
    return render(request, 'core/500.html', status=500)
