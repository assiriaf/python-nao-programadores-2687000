ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = ano_formatura - ano_nascimento
print(idade_formatura)
# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento > ano_formatura)
print(ano_nascimento <= ano_formatura)
print(ano_nascimento == ano_formatura)
# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(idade_formatura < ano_formatura and ano_nascimento > idade_formatura)
print(ano_formatura >= ano_nascimento or ano_nascimento >= idade_formatura)
print(not ano_nascimento == ano_formatura)