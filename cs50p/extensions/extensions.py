f = input('File name: ').lower().strip()

if '.' in f:
    x = f.split('.')
    t = x[-1]
    if t == 'gif':
        print('image/gif')
    elif t == 'jpg' or t == 'jpeg':
        print('image/jpeg')
    elif t == 'png':
        print('image/png')
    elif t == 'pdf':
        print('application/pdf')
    elif t == 'txt':
        print('text/plain')
    elif t == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')


