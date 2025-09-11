# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos_linkedin = ['Python para não programadores', 'Linguagem de Programação R para Ciência de Dados: Formação Básica', 
'Introdução às Funções Lógicas no Excel', 'Fundamentos da Comunicação Inclusiva', 'Aprendendo Programação SQL']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_python = 'Python para não programadores'
curso_r = 'Linguagem de Programação R para Ciência de Dados: Formação Básica'
curso_sql = 'Aprendendo Programação SQL'
# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliacoes = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista 
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
if curso_python in cursos_linkedin:
  print(f'O curso {curso_python} está no catálogo. Por favor, avalie o curso.')
  avaliacoes[curso_python] = int(input('De 0 a 10, que nota você dá para este curso: '))

if curso_r in cursos_linkedin:
  print(f'O curso {curso_r} está no catálogo. Por favor, avalie o curso.')
  avaliacoes[curso_r] = int(input('De 0 a 10, que nota você dá para este curso: '))

if curso_sql in cursos_linkedin:
  print(f'O curso {curso_sql} está no catálogo. Por favor, avalie o curso.')
  avaliacoes[curso_sql] = int(input('De 0 a 10, que nota você dá para este curso: '))

else:
  print('O curso não faz parte do catálogo.')

print(avaliacoes)