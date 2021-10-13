import math
x = int(input('Введите x : '))
n = int(input('Введите  (0<=n<5) : '))
e = 0.0004
k = 1

T_k = ((x / 2) * n ) / math.factorial( n )
T_k2 = ((-1) ** k) * ((x / 2)**(n + 2*k)) / (math.factorial(k) * math.factorial(k + n))
Sum = 0

while abs(T_k - T_k2) > e :
    print(k)
    k = k + 1
    Sum = Sum + T_k
    T_k = T_k2
    T_k2 = (((-1) ** k) * ((x / 2)**(n + 2*k))) / (math.factorial(k) * math.factorial(k + n))
else:
    print(Sum)