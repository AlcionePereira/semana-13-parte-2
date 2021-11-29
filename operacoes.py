inverter = []
maximo = 0
minimo = 9999999
soma = 0
comprimento = []
cont = -1
mostrar = []

while True:
    n = int(input().strip())
    cont+=1
    mostrar.append(n)
    inverter.insert(0, n)
    soma = soma + n
    if n != 0 and n < minimo:
        minimo = n
    if n > maximo:
        maximo = n
    if n == 0:break
    
# Mostrar os números digitados    
print(mostrar[:-1])

# Quantidade de elementos de cada lista    
comprimento = cont
if comprimento != 0:
    print(comprimento)
    
# Inverter os números      
del inverter[0]
print(inverter)

# Menor número
print(minimo)

# O maior número    
print(maximo)

# A soma de todos os números
print(soma)



    



