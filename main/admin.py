from django.contrib import admin
from .models import Play, Poem, Prose

# Register your models here.
admin.site.register(Play)
admin.site.register(Poem)
admin.site.register(Prose)