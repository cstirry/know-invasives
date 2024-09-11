# plant_search/views.py
import os
from django.shortcuts import render
from django.conf import settings
from .models import Plant
from fuzzywuzzy import fuzz
from .forms import PlantSearchForm

def home(request):
    """Renders the home page with the search form."""
    form = PlantSearchForm()

    # TODO: Make file paths configurable via settings
    # Define paths to the templates
    template_name = 'plant_search/home.html'
    fallback_template = 'plant_search/home_basic.html'

    # Construct the full path to the template
    template_path = os.path.join(settings.BASE_DIR, 'plant_search/templates', template_name)

    # Check if the home.html template exists, otherwise use home_basic.html
    if os.path.exists(template_path):
        return render(request, template_name, {'form': form})
    else:
        return render(request, fallback_template, {'form': form})

def plant_search(request):
    form = PlantSearchForm(request.GET or None)
    results = None

    if form.is_valid():
        query = form.cleaned_data.get('query')
        state = form.cleaned_data.get('state')

        plants = Plant.objects.all()

        if query:
            plants = [plant for plant in plants if fuzz.partial_ratio(query, plant.common_name) > 90
                                                or fuzz.partial_ratio(query, plant.scientific_name) > 90
                                                or fuzz.partial_ratio(query, plant.synonym) > 90
                                                or fuzz.partial_ratio(query, plant.symbol) > 90]

        if state:
            plants = plants.filter(state__icontains=state)

        results = plants

    return render(request, 'plant_search/search_results.html', {'form': form, 'results': results})