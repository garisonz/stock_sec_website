# python manage.py import_stock_info stocks/stockApp/data/company_tickers.json

import json
from django.core.management.base import BaseCommand, CommandError
from stockApp.models import Stock_info  # Adjust 'stocks.models' to your app name and model

class Command(BaseCommand):
    help = 'Imports data from company_tickers JSON file into the Stock model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to import')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                for entry in data.values():
                    Stock_info.objects.update_or_create(
                        cik_number=entry['cik_str'],
                        defaults={
                            'ticker_symbol': entry['ticker'],
                            'company_name': entry['title']
                        }
                    )
            self.stdout.write(self.style.SUCCESS('Successfully imported stocks'))
        except FileNotFoundError:
            raise CommandError(f'File "{json_file}" does not exist')
        except json.JSONDecodeError:
            raise CommandError('Error decoding JSON')
        except KeyError as e:
            raise CommandError(f'Missing key in JSON data: {e}')