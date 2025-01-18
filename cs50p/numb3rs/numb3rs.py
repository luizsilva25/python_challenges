import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^((?:\d)?(?:\d)?(?:\d))\.((?:\d)?(?:\d)?(?:\d))\.((?:\d)?(?:\d)?(?:\d))\.((?:\d)?(?:\d)?(?:\d))$", ip)
    try:
        for group in matches.groups():
            if int(group) > 255:
                return False
        return True
    except AttributeError:
        return False

if __name__ == "__main__":
    main()
