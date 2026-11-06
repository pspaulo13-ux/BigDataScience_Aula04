valor_compra = float(input('Qual o valor da compra ?'))
cliente_fidelidade = input('Programa fidelidade? [S/N]').lower()[0]#.Lower transforma qualqur letra mauisculo que a pessoas digitar em minusculo
print(cliente_fidelidade) # O [0] vai pegar a primeira letra do que a pessoa escreveu e usar na resposta,

if valor_compra > 100 or cliente_fidelidade == 's':
    print('Você ganhou um brinde')

else:
    print('Sem brinde')
