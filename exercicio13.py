### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0

while i <= len(itens):
    if itens[i] == "parar":
        print("final encontrado")
        break
    else:
        print(i)
        i += 1
