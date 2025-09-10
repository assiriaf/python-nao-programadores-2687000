# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input('Digite seu nome: ')
ano_linkedin = int(input('Insira o ano em que conheceu o LinkedIn: '))
ano_atual = int(input('Insira em que ano estamos: '))
cursos_linkedin = input('Quais cursos você já fez através do LinkedIn Learning (insira em ordem cronológica e separados por vírgula)?: ')

# 2. Armazene esses dados em um dicionário
pessoa = {'nome': nome, 'ano_linkedin': ano_linkedin, 'ano_atual': ano_atual, 'cursos_linkedin': cursos_linkedin}
lista_cursos = cursos_linkedin.split(',')

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f'{nome} conheceu o LinkedIn em {ano_linkedin}, isto é, há {ano_atual - ano_linkedin} ano(s). Desde então já realizou {len(lista_cursos)} cursos, que vão de {lista_cursos[0]} a{lista_cursos[len(lista_cursos) - 1]}.')