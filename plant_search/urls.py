from django.urls import path
from .views import home, plant_search

urlpatterns = [
    path('', home, name='home'),  # Home page with search form
    path('search/', plant_search, name='plant_search'),  # Search results page
]
