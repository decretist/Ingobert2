from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="ingobert/index.html")),
    url(r'demo/', views.demo, name='demo'),
    url(r'load/', views.load, name='load'),
]

