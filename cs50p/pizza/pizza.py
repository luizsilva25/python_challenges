import sys
from tabulate import tabulate
import csv

try:
    menu = sys.argv[1]
    if len(sys.argv) > 2:
        sys.exit('Too many arguments')
except IndexError:
    sys.exit('Too few arguments')

extension = len(menu) - 3
name = menu[:-4].title()
extension = menu[extension:]


if extension != 'csv':
    sys.exit('Not a CSV file')

table = []

try:
    with open(menu) as file:
        items =  csv.DictReader(file)
        for row in items:
            table.append({f'{name} Pizza': row[f'{name} Pizza'], 'Small': row['Small'], 'Large': row['Large']})

except FileNotFoundError:
    sys.exit('Not found')

print(tabulate(table, headers="keys", tablefmt="grid"))
#print(table)
