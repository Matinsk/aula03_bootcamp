### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

text = "Eu sou o caminho a verdade e a vida"

list_text = text.split()
colecao = {}

for palavra in  list_text:
    if palavra in colecao:
        colecao[palavra] += 1
    else:
        colecao[palavra] = 1
print(colecao)