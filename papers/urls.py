from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_papers, name='research_papers'),
]
