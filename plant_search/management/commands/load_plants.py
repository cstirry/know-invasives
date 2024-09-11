import os
import pandas as pd
from django.core.management.base import BaseCommand
from plant_search.models import Plant

class Command(BaseCommand):
    help = 'Load plant data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Delete all existing data from the Plant table
        #Plant.objects.all().delete()

        # TODO: Make file paths configurable via settings
        # Define the file paths
        data_file = 'data/data.xlsx'
        fallback_file = 'data/data_sample.xlsx'

        # Check if data.xlsx exists, otherwise load data_sample.xlsx
        if os.path.exists(data_file):
            self.stdout.write(self.style.SUCCESS(f"Loading data from {data_file}"))
            excel_data = pd.read_excel(data_file)
        else:
            self.stdout.write(self.style.WARNING(f"{data_file} not found. Loading data from {fallback_file} instead."))
            excel_data = pd.read_excel(fallback_file)

        for index, row in excel_data.iterrows():
            Plant.objects.create(
                common_name=row['common_name'],
                scientific_name=row['scientific_name'],
                synonym=row.get('synonym', None),  # Handling missing values
                state=row.get('state', None),
                category=row.get('habit', None),  # 'habit' refers to 'category'
                invasive=row.get('invasive', False),  # Assume False if missing
                symbol=row.get('symbol', False),
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
