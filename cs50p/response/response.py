import validators
def main():
    print(validation(input("What's your e-mail address? ")))

def validation(email):
   valid = validators.email(email)
   if valid:
       return 'Valid'
   else:
       return 'Invalid'


if __name__ == '__main__':
    main()
