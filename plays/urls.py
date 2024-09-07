from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.play, name="play"),
    path('<str:info>', views.info, name="info")
]