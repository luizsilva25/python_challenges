import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    address = re.search(r'"http(s)?://(www)?\.?youtube\.com/embed/([a-z0-9]+)"', s, re.IGNORECASE)
    if address:
        return f'https://youtu.be/{address[3]}'



if __name__ == "__main__":
    main()
