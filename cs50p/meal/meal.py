def main():
    x = input('What time is it? ')
    h = convert(x)
    if h >= 7 and h <= 8:
        meal = 'breakfast time'
    elif h >= 12 and h <= 13:
        meal = 'lunch time'
    elif h >= 18 and h <= 19:
        meal = 'dinner time'

    return meal


def convert(time):
    time = time.split(':')
    minutes = float(time[1]) * 100 / 60 / 100
    hora = float(time[0]) + minutes
    return hora


if __name__ == "__main__":
    print(main())
