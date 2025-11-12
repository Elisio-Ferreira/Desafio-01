
print('--- BANCO LILIZA ---\n')
print('--- SELECIONE UMA OPÇÃO ---\n')

print('[1] - Depositar')
print('[2] - Sacar')
print('[3] - Extrato \n')

valor_Total = []
valor_deposito = []
valor_saque = []

op = int(input('OPÇÃO DESEJADA:  \n'))

print('VOÇE ESCOLHEU A OPCAO:  ', op)


if op == 1:
    print('HORA DE DEPOSITAR \n')
    valor_deposito = int(input('QUAL VALOR DO DEPOSITO \n'))
    print('VOCE REALIZOU UM DEPOSITO DE: ', valor_deposito)
    valor_Total.append(valor_deposito)
    print(valor_Total)



