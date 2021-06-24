#####################################################################
#-------> EXERCICSE 01.1

#for i in range(3, 13):
#  print(i)
i = 3
while (i < 13):
    print(i)
    i += 1

#->01.2
for i in range(3, 9):
    print(i)

#--------------------------------------------------------> EXERCICSE 02.1

valor = int(input('Digite o valor em R$'))

if valor >= 100:
    cedulas100 = valor // 100
    valor -= cedulas100*100
    print('Cedulas de 100: {}'.format(cedulas100))
    if not valor:
        break

if valor >= 50:
    cedulas50 = valor // 50
    valor -= cedulas50*50
    print('Cedulas de 50: {}'.format(cedulas50))
    if not valor:
        break

if valor >= 20:
    cedulas20 = valor // 20
    valor -= cedulas20*20
    print('Cedulas de 20: {}'.format(cedulas20))
    if not valor:
        break

if valor >= 10:
    cedulas10 = valor // 10
    valor -= cedulas10*10
    print('Cedulas de 10: {}'.format(cedulas10))
    if not valor:
        break

if valor >= 5:
    cedulas5 = valor // 5
    valor -= cedulas5*5
    print('Cedulas de 5: {}'.format(cedulas5))
    if not valor:
        break

if valor:
    cedulas1 = valor
    print('Cedulas de 1: {}'.format(cedulas1))


#-------------------------------------------------------> EXERCICSE 03.1
total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
         if idade > 12:
             ingresso = 15
         else:
             ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format_map(total))
print('Total de pessoas: {}'.format_map(dinheiro))
print('Total de pessoas: {}'.format_map(media))