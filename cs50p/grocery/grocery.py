list = {}

while True:
    try:
        item = input().upper()
        if item not in list:
            list.update({item: 1})
        else:
            n = list.get(item)
            n += 1
            list.pop(item)
            list.update({item: n})
    except EOFError:
        print()
        break

#sorte the dic alphabetically

keys = [*list]
keys.sort()

#print out the list

for i in keys:
    print(f'{list.get(i)} {i}')

