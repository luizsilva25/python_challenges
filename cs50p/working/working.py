import re
import sys

conv_hour = {
    '12 AM': '00',
    '1 AM' : '01',
    '2 AM' : '02',
    '3 AM' : '03',
    '4 AM' : '04',
    '5 AM' : '05',
    '6 AM' : '06',
    '7 AM' : '07',
    '8 AM' : '08',
    '9 AM' : '09',
    '10 AM' : '10',
    '11 AM' : '11',
    '12 PM': '12',
    '01 PM' : '13',
    '2 PM' : '14',
    '3 PM' : '15',
    '4 PM' : '16',
    '5 PM' : '17',
    '6 PM' : '18',
    '7 PM' : '19',
    '8 PM' : '20',
    '9 PM' : '21',
    '10 PM' : '22',
    '11 PM' : '23',
}

def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour = re.search(r'(^\d?\d)(:\d\d)?\s(AM|PM)\sto\s(\d?\d)(:\d\d)?\s(AM|PM)$', s)
    if hour:
        start = hour[1]
        start_p = hour[3]
        end = hour[4]
        end_p = hour[6]
        if hour[2]:
            minutes = hour[2]
            if int(minutes[1:]) > 59:
                raise ValueError
            else:
                if hour[5]:
                    minutes_end = hour[5]
                    if int(minutes_end[1:]) > 59:
                        raise ValueError
                    else:
                        start = f'{hour[1]} {hour[3]}'
                        end = f'{hour[4]} {hour[6]}'
                        return f'{conv_hour.get(start)}{minutes} to {conv_hour.get(end)}{minutes_end}'
                else:
                    # #:## AA to # AA
                    start = f'{hour[1]} {hour[3]}'
                    end = f'{hour[4]} {hour[6]}'
                    return f'{conv_hour.get(start)}{minutes} to {conv_hour.get(end)}:00'
        else:
            # # AA to #:## AA
            if hour[5]:
                minutes_end = hour[5]
                if int(minutes_end[1:]) > 59:
                    raise ValueError
                else:
                    start = f'{hour[1]} {hour[3]}'
                    end = f'{hour[4]} {hour[6]}'
                    return f'{conv_hour.get(start)}:00 to {conv_hour.get(end)}{minutes_end}'

            else:
            # # AA to # AA
                start = f'{hour[1]} {hour[3]}'
                end = f'{hour[4]} {hour[6]}'
                return f'{conv_hour.get(start)}:00 to {conv_hour.get(end)}:00'
    else:
        raise ValueError

if __name__ == "__main__":
    main()
