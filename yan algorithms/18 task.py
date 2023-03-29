l = list()
s = str()
while s != 'exit':
    s = str(input())
    if s[0:10] == 'push_front':
        l.insert(0, int(s[11:len(s)]))
        print('ok')
    if s[0:9] == 'push_back':
        l.append(int(s[10:len(s)]))
        print('ok')
    if s == 'pop_front':
        if l == list():
            print('error')
        else:
            print(l[0])
            del(l[0])
    if s == 'pop_back':
        if l == list():
            print('error')
        else:
            print(l[-1])
            del(l[-1])
    if s == 'back':
        if l == list():
            print('error')
        else:
            print(l[-1])
    if s == 'size':
        print(len(l))
    if s == 'clear':
        l = list()
        print('ok')
    if s == 'front':
        if l == list():
            print('error')
        else:
            print(l[0])
    if s == 'exit':
        print('bye')