from django.core.management.base import BaseCommand
from bookapp.models import Book
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        names = ['computerEra', 'RisingSun', 'Boss', 'Nirmala']
        authors = ['Sridhar', 'Ramesh', 'Jhon', 'Smith']
        prices = [str(100.0), str(200.20), str(300.30), str(500.50)]
        for each in range(100):
            name=random.choices(names)
            author=random.choices(authors)
            price=random.choices(prices)
            book_data=Book.objects.bulk_create([Book(name=name[0],author=author[0],price=price[0])])


