from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='ingobert/index.html')),
    path('demo/', views.demo),
    path('home/', views.home),
    path('2column/', views.two_column),
    path('3column/', views.three_column),
    path('4column/', views.four_column),
]

