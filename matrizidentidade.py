n = int(input('Qual a ordem da matriz? '))
matriz = [0]*n
for i in range(n):
    matriz[i] = [0]*n

for i in range(n):
    for j in range(n):
        if i == j:
            matriz[i][j] = 1

print(*matriz, sep='\n')
