# get a string from the user
n = input('camelCase: ')
snake = []

#convert camel case into snake case
for caracter in n:
    if caracter.islower():
        snake.append(caracter)
    else:
        snake.append('_')
        snake.append(caracter.lower())

# output
print('snake_case: ', end='')
for c in snake:
    print(c, end='')
print()
