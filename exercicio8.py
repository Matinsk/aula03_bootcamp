### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.


lista_numeros = [numero for numero in range(200)]

lista_numeros_par = [numero for numero in lista_numeros if numero % 2 == 0]    

print(lista_numeros_par)