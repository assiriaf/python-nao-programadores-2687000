# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Digite um nome: ')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Insira o total de dias dedicados ao estudo: ')
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Insira a média de horas estuda por dia: ')
total_dias = int(total_dias)
total_horas = int(total_horas)
total = total_dias * total_horas
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Insira o nome do curso: ')
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'{nome} dedicou {total_dias} dias aos estudos de {curso}, numa média de {total_horas} por dia, totalizando uma média de {total} horas na semana.')