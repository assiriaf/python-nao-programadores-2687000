# Crie uma lista
frutas_pernambuco = ['Melancia', 'Maçã', 'Uva', 'Banana', 'Manga']
# Crie um for loop para imprimir cada elemento dessa lista
for frutas in frutas_pernambuco:
  print(frutas)
# Crie um objeto iterável utilizando a função range()
print(list(range(0, 100, 5)))
print(list(range(101)))
# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for item in range(4, 7):
  print(f'{item} - Estou aprendendo python')
else:
  print('Fim do loop')