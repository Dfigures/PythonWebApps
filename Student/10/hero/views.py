from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Hero

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Hero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Hero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = '__all__'


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')