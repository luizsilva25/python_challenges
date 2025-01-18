def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if s.isalnum():
        if len(s) <= 6 and len(s) >= 2:
            if starts_letters(s[0], s[1]):
                if correct_number(s):
                   if correct_zero(s):
                        return True
                   else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


# Regra 3:
def starts_letters(x, y):
    if x.isalpha() and y.isalpha():
        return True
    else:
        return False

#Regra 4, Numero 0 não pode aparecer primeiro,:
 def correct_zero(a):
    for c in a:
        if c == '0':
            if a[a.index('0') - 1].isalpha():
                return False
    return True


 #Regra 5, número ao final:
  def correct_number(z):
    for i in range(len(z)):
        if z[i].isnumeric():
            if not z[i:].isnumeric():
                return False
    return True

if __name__ == '__main__':
    main()
