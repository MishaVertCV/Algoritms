n = int(input())
lis = []
for i in range(n):
    lis.append(set([i+1]))
m = int(input())
for i in range(m):
    a,b = map( int, input('-> ').split() )
    a_set = None
    b_set = None
    for e in lis:
        if a in e:
            a_set = e
        if b in e:
            b_set = e
    if a_set != b_set:
        lis.remove( a_set )
        lis.remove( b_set )
        lis.append( a_set | b_set )
print( len(lis) )
for e in lis:
    print( len(e) )
    print( *e )