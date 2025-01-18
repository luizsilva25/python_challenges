import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    words = s.lower().split(' ')
    for word in words:
        if re.search(r'^um(\W*)?$', word):
            print(word)
            counter += 1
    return counter



if __name__ == "__main__":
    main()
