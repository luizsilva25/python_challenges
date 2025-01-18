import emoji

e = input('Input: ')
e = emoji.emojize(e, language='alias')
print(e)
