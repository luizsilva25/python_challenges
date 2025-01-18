month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November":11,
    "December": 12,
}

def main():
    while True:
        date = input('Date: ').strip()
        if date[0].isnumeric():
            if valid_date_numeric(date):
                break
        elif date[0].isalpha():
            if valid_date_alpha(date):
                break


def valid_date_alpha(date):
    if '/' in date:
        return False

    n = date.split(' ')
    mes = n[0]
    ano = int(n[2])
    dia = n[1]

    if ',' not in dia:
        return False

    dia = int(dia[:-1])

    if mes in month:
        if ano > 0:
            if dia > 0 and dia <= 31:
                print(f'{ano}-{month.get(mes):02}-{dia:02}')
                return True



def valid_date_numeric(date):
    if ',' in date:
        return False
    n = date.split('/')
    dia = int(n[1])
    mes = int(n[0])
    ano = int(n[2])
    if mes <= 12:
        if dia <=31:
            if ano > 0:
                print(f'{ano}-{mes:02}-{dia:02}')
                return True


main()
