def main():
    n = convert(input('Fraction: '))
    print(gauge(int(n)))

def convert(fraction):
    terms = fraction.split('/')
    x = int(terms[0])
    y = int(terms[1])
    if x > y:
        raise Exception('Invalid Fraction')
    else:
        try:
            z = x / y
        except (ZeroDivisionError):
            print('Impossible to divide by 0')
        else:
            return (z * 100)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage:.0f}%'

if __name__ == "__main__":
    main()
