from django.urls import path
from .views import projects

urlpatterns = [
    path('', view=projects, name='projects')
]
