from django.shortcuts import render
from django.http import HttpResponse
from .models import Theme, Character, Chapter
from main.models import Prose

def prose(request, id): 
    title = Prose.objects.get(id=id) 
    themes = Theme.objects.filter(prose=id)
    characters = Character.objects.filter(prose=id)
    chapters = Chapter.objects.filter(prose=id)
    context = {
        "title": title,
        "themes": themes,
        "characters": characters,
        "chapters": chapters
    }
    return render(request, 'proses/proses.html', context)

def info(request, info):
    x = info.split("_")

    if x[0] == "character":
        character = Character.objects.get(id=x[1])
        context = {
            "type": "character",
            "thing": character
        }
        return render(request, "proses/info.html", context)

    elif x[0] == "theme":
        theme = Theme.objects.get(id=x[1])
        context = {
            "type": "theme",
            "thing": theme
        }
        return render(request, "proses/info.html", context)

    elif x[0] == "chapter":
        chapters = Chapter.objects.get(id=x[1])
        context = {
            "type": "chapters",
            "thing": chapters
        }
        return render(request, "proses/info.html", context)

    else:
        return render(request, "main/error.html")
