N = int(input())
x = list()
y = list()
high = list()
high_result = list()
lengh_result = list()
h = 0
s = 0
sym1 = 0
sym2 = 0
sym = 0
if N >= 1 and N <= 200000:
    for i in range(N):
      xi, yi = map(int, input().split())
      x.append(xi)
      y.append(yi)
    for i in range(len(y)):
        if h < y[i]:
            high.append(i)
            high_result.append(y[i]-h)
            h = y[i]
    for i in range(len(high)):
        lengh_result.append(x[high[i]] - s)
        s = x[high[i]]
        sym1 = sym1 + (high_result[i]**2 + lengh_result[i]**2)**0.5
    for i in range(len(x)-1):
        sym2 = sym2 + ((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2)**0.5
sym = sym1 + sym2
print(sym)

      
     
          
      
      
