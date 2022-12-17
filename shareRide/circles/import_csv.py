import csv

from .models.circles import Circle


def import_csv(csv_filename):
    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            circle = Circle(**row)
            circle.save()
            print(circle.name)
