from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


class HomePage(ListView):
    model = PortfolioModel
    template_name = 'portfolio/home_page.html'
    context_object_name = 'item'
