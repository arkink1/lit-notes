from django.shortcuts import render
from .models import Play, Poem, Prose

# Create your views here.
def index(request):
    plays = Play.objects.all()
    poems = Poem.objects.all()
    proses = Prose.objects.all()
    context = {
        "plays": plays,
        "poems": poems,
        "proses": proses
    }
    return render(request, "main/index.html", context)



