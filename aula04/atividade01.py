compra = float(input('Qual o valor da compra? '))

if compra > 250:
    desconto = compra * 0.16
    valor_final = compra - desconto
    print(f'O valor da sua compra é R${compra}\n Desconto de 16%: R${desconto}\n O valor final da sua compra é de R${valor_final}')

else:
    print(f' Não há desconto para ser aplicado. O valor final é R${compra}') 