from datetime import date
import re
import sys
import inflect


def main():
    print(f"{count_minutes(get_date(input('Date of Birth: ')))} minutes")

def get_date(date):
    valid_date = re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', date)
    if valid_date:
        return valid_date.groups()
    else:
        sys.exit('Invalid Date')


def count_minutes(d):
    today = date.today()
    birth = date.fromisoformat(f'{d[0]}-{d[1]}-{d[2]}')
    days_lived = today - birth
    minutes = days_lived.days * 24 * 60
    p = inflect.engine()
    result = p.number_to_words(minutes).capitalize().split(' ')
    phrase = []
    for word in result:
        if word != 'and':
            phrase.append(word)
    a = ''
    for word in phrase:
        a += f'{word} '
    return a.rstrip()

if __name__ == "__main__":
    main()
