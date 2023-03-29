l = list()
s = str()
while s != 'exit':
    s = str(input())
    if s[0:4] == 'push':
        l.append(int(s[5:len(s)]))
        print('ok')
    if s == 'pop':
        if l == list():
            print('error')
        else:
            print(l[0])
            del(l[0])
    if s == 'front':
        if l == list():
            print('error')
        else:
            print(l[0])
    if s == 'size':
        print(len(l))
    if s == 'clear':
        l = list()
        print('ok')
    if s == 'exit':
        print('bye')