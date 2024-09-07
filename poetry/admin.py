from django.contrib import admin
from .models import Theme, Analysis, Context

# Register your models here.
admin.site.register(Theme)
admin.site.register(Analysis)
admin.site.register(Context)