lista_numeros = list(range(15, 31))
print(lista_numeros)

indice = 0 

for numero in lista_numeros:
  if numero % 3 == 0 and numero % 5 == 0:
    lista_numeros[indice] = 'FizzBuzz'
  elif numero % 3 == 0:
    lista_numeros[indice] = 'Fizz'
  elif numero % 5 == 0:
    lista_numeros[indice] = 'Buzz'
  else:
    lista_numeros[indice] = numero
  indice = indice + 1

print(lista_numeros)