import sys

rows = []

try:
    program = sys.argv[1]
except IndexError:
    sys.exit('Too feel arguments')

extension = len(program) - 2

if len(sys.argv) > 2:
    sys.exit('Too many arguments')
elif program[extension:] != 'py':
    sys.exit('Not a python file')

try:
    with open(sys.argv[1]) as file:
        rows.append(file.readlines())
except FileNotFoundError:
    sys.exit('File do not exist.')


comments = 0
empty = 0
code = 0
rows = rows[0]


for row in rows:
    if row.isspace():
        empty += 1
    else:
        row = row.lstrip()
        if row.startswith('#'):
            comments += 1
        else:
            code += 1
print(code, end='')
