import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

print(sys.argv)

# Checar se o usuário não escolheu fonte:
if len(sys.argv) == 1:
        fonts = figlet.getFonts()
        chosen = random.choice(fonts)
        figlet.setFont(font=chosen)

# Checar se o usuário escolheu fonte:
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit('wrong arguments')

else:
    sys.exit('Wrong Number of arguments')

text = input('Input: ')

print(figlet.renderText(text))





