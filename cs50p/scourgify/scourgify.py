import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit('Too few arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many arguments')
else:
    file_name = sys.argv[1]
    file_name = file_name[:-4]
    extension = sys.argv[1]
    extension = extension[len(file_name):]
    if extension != '.csv':
        sys.exit('Not a CSV file')

data = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({'name': row['name'], 'house':row['house']})
except FileNotFoundError:
    sys.exit('File not found')

new_data = []

for student in data:
    n = data.index(student)
    name = data[n].get('name')
    house = data[n].get('house')
    first, second = name.split(', ')
    new_data.append({'first name': first,'surname':second, 'house': house})



with open((sys.argv[2]), 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['first', 'last', 'house'])
    for element in new_data:
        x = new_data.index(element)
        name = new_data[x].get('surname')
        surname = new_data[x].get('first name')
        house = new_data[x].get('house')
        writer = csv.writer(file)
        writer.writerow([name, surname, house])


#print (tabulate(new_data, headers='keys'))
