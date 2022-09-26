# calculadora
print('qual operação você quer realizar?')
print('1- adição')
print('2- subtração')
print('3- multiplicação')
print('4- divisão')
op = input('Operação Escolhida ')
if op == '1':
    n1 = int(input('Digite o primeiro número '))
    n2 = int(input('Digite o segundo número '))
    som = n1 + n2
    print('=', + som)
if op == '2':
    n1 = int(input('Digite o primeiro número '))
    n2 = int(input('Digite o segundo número '))
    sub = n1 - n2
    print('=', + sub)
if op == '3':
    n1 = int(input('Digite o primeiro número '))
    n2 = int(input('Digite o segundo número '))
    mult = n1 * n2
    print('=', + mult)
if op == '4':
    n1 = float(input('Digite o primeiro número '))
    n2 = float(input('Digite o segundo número '))
    div = n1 / n2
    print('=', + div)
input('fim, execute de novo, caso queira fazer outra operação')
