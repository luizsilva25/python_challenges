a = input('Expression: ')

b = a.split(' ')
x = int(b[0])
z = int(b[2])
y = b[1]

match y:
    case '+':
        r = float(x + z)
        print(f'{r:.1f}')
    case '-':
        r = float(x - z)
        print(f'{r:.1f}')
    case '*':
        r = float(x * z)
        print(f'{r:.1f}')
    case '/':
        r = float(x / z)
        print(f'{r:.1f}')
