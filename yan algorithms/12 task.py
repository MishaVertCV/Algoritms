s = str(input())
p = list()
right = True
if len(s) < 2:
    print('no')
else:
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            p.append(s[i])
        if len(p) == 0:
            print('no')
            right = False
            break
        else:
            if s[i] == ')' and p[-1] != '(':
                print('no')
                break
            if s[i] == ')' and p[-1] == '(':
                del(p[-1])
            if s[i] == ']' and p[-1] != '[':
                print('no')
                break
            if s[i] == ']' and p[-1] == '[':
                del(p[-1])
            if s[i] == '}' and p[-1] != '{':
                print('no')
                i = 0
                break
            if s[i] == '}' and p[-1] == '{':
                del(p[-1])
    if len(p) == 0 and right:
        print('yes')
    if len(p) != 0 and i == len(s) - 1:
        print('no')