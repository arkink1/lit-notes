from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.poetry, name="poetry"),
    path('<int:id>/<str:info>', views.info, name="info")
]