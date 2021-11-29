temp =[]
princ = []
treze = 13
soma = 0
media = 0

for i  in range(30):
    temp.append(input())
    idade = int(input())
    altura = float(input())
    temp.append(idade)
    temp.append(altura)
    soma+=altura
    princ.append(temp[:])
    temp.clear()
media  = soma / 30

print(f'MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for p in princ:
    if p[2] < media:
        if p[1] > 13:
            print(f'{p[0]}')   
