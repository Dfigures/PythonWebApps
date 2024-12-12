from django.urls import path
from django.contrib import admin
from hero.views import HeroView, MainView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', MainView.as_view(), name = 'home'),
    path('<str:name>',HeroView.as_view()),
]