# Crie uma lista apenas com elementos numéricos
números = [1, 3.14, 17, 89, 0, 105]
print(números)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['ABC', 1, 55.5, False, [1,2,3,4], 100]
print(mista)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista[:6])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mista[0:6:2])
print(mista[0:-1:2])
# Remova da lista o último item
mista.pop()
print(mista)
# Insira na lista um novo item
mista.append(2025)
print(mista)
# Remova da lista um item específico
mista.remove([1,2,3,4])
print(mista)