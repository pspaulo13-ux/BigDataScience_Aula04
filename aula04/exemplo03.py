pontuacao = int(input('Qual a sua pontuação:'))

#Bonus

if pontuacao >= 100:
   pontuacao = pontuacao + 10
   print(f'Excelente! Você tem {pontuacao} agora!')

elif pontuacao >= 50:
   pontuacao = pontuacao + 5
   print(f'Bom desempenho! Você tem {pontuacao} agora!')

else: 
   print(f'Não desanime, você está começando. Sua pontuação: {pontuacao}')


