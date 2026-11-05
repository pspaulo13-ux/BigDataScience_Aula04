pontuacao = int(input('Qual a sua pontuação:'))

#Bonus

if pontuacao >= 100:
   pontuacao = pontuacao + 10
   print(f'Excelente! Você tem {pontuacao} agora!')

if pontuacao >= 50:
   pontuacao = pontuacao + 5
   print(f'Bom desempenho! Você tem {pontuacao} agora!')

else: 
   print(f'Não desanime, você está começando. Sua pontuação: {pontuacao}')


#  O If ele sempre executa isoladamente, entao ele executou as duas linhas if e foi somando os valores, quando usamos o elif, ele so executa uma linha.