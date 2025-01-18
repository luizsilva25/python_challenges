import random


def main():
    level = get_level()
    errors = 0
    points = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        while True:
            try:
                r = int(input(f'{x} + {y} = '))
            except ValueError:
                print('EEE')
                pass
            else:
                if r == z:
                    points += 1
                    break
                else:
                    if errors < 2:
                        print ('EEE')
                        errors += 1
                    else:
                        print(f'{x} + {y} = {z}')
                        errors = 0
                        break
    print(f'Score: {points}')



def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n >= 1 and n <= 3:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        return a
    elif level == 2:
        a = random.randint(10, 99)
        return a
    elif level == 3:
        a = random.randint(100, 999)
        return a


if __name__ == "__main__":
    main()
