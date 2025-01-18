def main():
    phrase = shorten(input('Input: '))
    print(phrase)

def shorten(word):
    twttr = []
    for c in word:
        if c not in 'AEIOUaeiou':
            twttr.append(c)
    return ''.join(twttr)

if __name__ == '__main__':
    main()
