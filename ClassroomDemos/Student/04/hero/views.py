from pathlib import Path
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Hero
from django.shortcuts import get_object_or_404


class MainView(TemplateView):
    template_name = 'hero.html'


class HeroView(TemplateView):
     template_name = 'heroes.html'


     def get_context_data(self, **kwargs):
         return {
             'hero': Hero.objects.get(name=kwargs['name'])
         }

