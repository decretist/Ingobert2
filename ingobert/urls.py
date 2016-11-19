from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="ingobert/index.html")),
    url(r'demo/', views.demo),
    url(r'home/', views.home),
    url(r'2column/', views.two_column),
    url(r'3column/', views.three_column),
    url(r'4column/', views.four_column),
]

