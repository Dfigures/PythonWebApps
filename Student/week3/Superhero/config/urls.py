from django.urls import path
from hero.views import HeroListView, HeroDetailView

urlpatterns = [
    path('', HeroListView.as_view(), name='photo_list'),
    path('hero/<str:id>/', HeroDetailView.as_view(), name='photo_detail'),  # Use <str:id> to accept string IDs
]