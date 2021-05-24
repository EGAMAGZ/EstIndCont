from django.urls import path

from .views import AboutUsView, ContactView, HomeView, PortafolioView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('prosoft/', name='prosoft'),
    # path('prosoft/<slug:document-slug>', name='prosoft'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('portafolio/', PortafolioView.as_view(), name='portafolio')
]
