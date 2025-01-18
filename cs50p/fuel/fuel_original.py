def main():
    while True:
        try:
            n = float(get_fraction(input('Fraction: ')))

        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    if n <= 1:
        print('E')
    elif n >= 99:
        print('F')
    else:
        print(f'{n:.0f}%')


def get_fraction(prompt):
    fraction = prompt.split('/')
    x = int(fraction[0])
    y = int(fraction[1])
    if x > y:
        return 0/0
    else:
        z = x / y * 100
        return z



if __name__ == '__main__':
    main()
