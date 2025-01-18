def main():
    a = str(input())
    convert(a)

def convert(x):
    x = x.replace(':)', '🙂')
    x = x.replace(':(', '🙁')
    print(x)


main()
