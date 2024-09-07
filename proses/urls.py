from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.prose, name="prose"),
    path('<str:info>', views.info, name="info")
]