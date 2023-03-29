def get_graph():
    (n,m)=tuple(map(int,input().split()))
    graph=[]
    for _ in range(m):
        (a,b)=tuple(map(int,input().split()))
        graph.append((a,b))
    return graph    
 
def dfs_loops(graph):
    
    stack=[1]
    chk=[1]
    
    while True:
    
        if len(stack)==0:
            print("OK")
            return
        
        v=stack[-1]
        
        for (a,b) in graph:
            
            if (a==v) and not (b in chk):
                stack.append(b)
                chk.append(b)
                # Проверка цикла
                sz=len(stack)
                print(stack)
                for i in range(sz-1):
                    if (b,stack[i]) in graph:
                        print("Loop:",end=' ')
                        for j in range(i,sz):
                            print(stack[j],end=' ')
                        print()
                break
        
        else:
            stack.pop()
n = int(input())
g=get_graph()
 
dfs_loops(g)