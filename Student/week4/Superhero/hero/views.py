from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

superheroes = [
    {
        'id': 'Batman',
        'name': 'Batman',
        'image': 'batman.jpg',
        'strengths': 'Martial Arts, Rich, Smart',
        'weaknesses': 'Mortal, No Special Abilities',
    },
    {
        'id': 'Blue Beetle',
        'name': 'Blue Beetle',
        'image': 'bluebeetle.jpg',
        'strengths': 'Scarab that can do almost anything he wants',
        'weaknesses': 'Armor Penetration, Magic',
    },
    {
        'id': 'Daredevil',
        'name': 'Daredevil',
        'image': 'daredevilpic.jpg',
        'strengths': 'Intelligence, Lawyer, Enhanced Senses',
        'weaknesses': 'Blind, Loud Noises, Overpowering Odors',
    },
    {
        'id': 'flash',
        'name': 'The Flash',
        'image': 'flash.jpg',
        'strengths': 'Intelligence, Speed, Determination',
        'weaknesses': 'DC, Wears Red',
    },
    {
        'id': 'Spiderman',
        'name': 'Spiderman',
        'image': 'spiderman.jpg',
        'strengths': 'Intelligence, Spidey Sense, Spider-like powers',
        'weaknesses': 'Bullets, Knives',
    },
    # Add more superheroes as needed
]

from django.urls import reverse

class HeroListView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        
        heroes = [{
            'name': hero['name'],
            'image': f"/static/images/{hero['image']}",
            'url': reverse('photo_detail', kwargs={'id': hero['id']})  
        } for hero in superheroes]
        return {'heroes': heroes}

    


class HeroDetailView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        id = kwargs['id']

        # Find the superhero by name in the 'superheroes' list
        superhero = next((hero for hero in superheroes if hero['id'] == id), None)

        if superhero:
            context = {
                'name': superhero['name'],
                'image': f"/static/images/{superhero['image']}",
                'strengths': superhero['strengths'],
                'weaknesses': superhero['weaknesses'],
            }
        else:
            # Handle the case where the superhero is not found
            context = {
                'name': 'Superhero Not Found',
                'image': '/static/images/placeholder.jpg',  # Provide a placeholder image
                'strengths': 'N/A',
                'weaknesses': 'N/A',
            }

        return context