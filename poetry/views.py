from django.shortcuts import render
from django.http import HttpResponse
from .models import Theme, Analysis, Context
from main.models import Poem

def poetry(request, id): 
    title = Poem.objects.get(id=id) 
    themes = Theme.objects.filter(poem=id)
    analyses = Analysis.objects.filter(poem=id)
    context = Context.objects.filter(poem=id)
    context = {
        "title": title,
        "themes": themes,
        "analyses": analyses,
        "context": context
    }
    return render(request, 'poetry/poetry.html', context)

def info(request, id, info):

    title = Poem.objects.get(id=id)

    if info == "themes":
        themes = Theme.objects.filter(poem=id)
        context = {
            "type": "theme",
            "thing": themes,
            "title":title
        }
        return render(request, "poetry/info.html", context)

    elif info == "analysis":
        analyses = Analysis.objects.filter(poem=id)
        context = {
            "type": "analysis",
            "thing": analyses,
            "title":title
        }
        return render(request, "poetry/info.html", context)

    elif info == "context":
        context = Context.objects.filter(poem=id)
        context = {
            "type": "context",
            "thing": context,
            "title":title
        }
        return render(request, "poetry/info.html", context)

    else:
        return render(request, "main/error.html")
