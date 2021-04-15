m = int(input('Digite o valor de M:'))
inicio = 1
n = 1
while (n <= m):
    print("{} {} {} = {}".format(n, n, n, inicio))
    n = n + 1
    
    i = 1
    while (i < n ):
        i = i  + 1
        print("+{}".format(inicio + 2 * i))
        
    
inicio = inicio + 2 * n


print("\n")
 




