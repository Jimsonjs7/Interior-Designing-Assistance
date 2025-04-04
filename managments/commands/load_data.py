import pandas as pd
from django.core.management.base import BaseCommand
from budget_estimator.models import InteriorDesign

class Command(BaseCommand):
    help = 'Load interior design data from Excel into the database'

    def handle(self, *args, **kwargs):
        # Load the Excel file
        df = pd.read_excel('interior_design_prices.xlsx')

        # Clear existing data
        InteriorDesign.objects.all().delete()

        # Load data into the database
        for index, row in df.iterrows():
            InteriorDesign.objects.create(
                component=row['Component'],
                modern_price=row['Modern (INR)'],
                classic_price=row['Classic (INR)'],
                minimalist_price=row['Minimalist (INR)'],
                bohemian_price=row['Bohemian (INR)']
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))