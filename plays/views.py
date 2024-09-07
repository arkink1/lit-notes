from django.shortcuts import render
from django.http import HttpResponse
from .models import Theme, Character, Act
from main.models import Play

def play(request, id): 
    title = Play.objects.get(id=id) 
    themes = Theme.objects.filter(play=id)
    characters = Character.objects.filter(play=id)
    acts = Act.objects.filter(play=id)
    context = {
        "title": title,
        "themes": themes,
        "characters": characters,
        "acts": acts
    }
    return render(request, 'plays/plays.html', context)

def info(request, info):
    x = info.split("_")

    if x[0] == "character":
        character = Character.objects.get(id=x[1])
        context = {
            "type": "character",
            "thing": character
        }
        return render(request, "plays/info.html", context)

    elif x[0] == "theme":
        theme = Theme.objects.get(id=x[1])
        context = {
            "type": "theme",
            "thing": theme
        }
        return render(request, "plays/info.html", context)

    elif x[0] == "act":
        acts = Act.objects.get(id=x[1])
        context = {
            "type": "acts",
            "thing": acts
        }
        return render(request, "plays/info.html", context)

    else:
        return render(request, "main/error.html")
