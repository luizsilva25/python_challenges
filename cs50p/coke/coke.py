amount = 50

while True:
    c = int(input('Insert Coin: '))
    if c  == 25 or c == 10 or c == 5:
        amount -= c
    if amount > 0:
        print(f'Amount Due: {amount}')
    if amount <= 0:
        print(f'Change Owed: {amount * -1}')
        break
