def one_from_list(l = list()):
    l = sorted(l)
    k = 0
    while l[k] == l[k+1]:
        k += 2
        if IndexError:
            break
    return l[k+1]
print(one_from_list(l = [7, 0, 0, 4, 7, 4, 8, 6, 8, 6, 9]))
                

