lista=[]
while True:
    val=int(input())
    if val==0:
        break
    lista.append(val)

quant=int(input())
soma=0
for x in lista:
    if quant==x:
        soma+=1

print(lista)
print(quant)
print(soma)
