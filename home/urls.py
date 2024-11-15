from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  # Route to the home view
]