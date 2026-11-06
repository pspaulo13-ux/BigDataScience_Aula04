vendas = float(input('Qual o valor da venda?'))
salario = float(input('Qual o valor do seu salário?'))

if vendas >= 1000:
    salario = salario + 150.00
    print(f'Parabéns pelo seu desempenho!\n O valor do seu salário foi acrescido de um bonus de  R$150,00 e agora é R${salario}')

elif vendas >= 500.00:
    salario = salario + 75
    print(f'Boas vendas, continue assim!\n O valor do seu salário foi acrescido de um bonus de  R$75,00 e agora é R${salario}')

else:
    print(f'Sem bonus aplicável.\n O valor do seu salário é de R${salario}')

