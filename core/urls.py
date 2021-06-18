from django.urls import path

from .views import AboutUsView, ContactView, DescriptionView, HomeView, MarketRateView, PortafolioView, ProsoftListView, ProsoftDocView, ServicesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('description/', DescriptionView.as_view(), name='description'),
    path('market-rates/', MarketRateView.as_view(), name="market-rates"),
    path('services/', ServicesView.as_view(), name= 'services'),
    path('prosoft/', ProsoftListView.as_view(), name='prosoft'),
    path('prosoft/<slug:document_slug>/', ProsoftDocView.as_view(), name='prosoft-doc'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('portafolio/', PortafolioView.as_view(), name='portafolio')
]
