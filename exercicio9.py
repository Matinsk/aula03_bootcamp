### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_categoria = {}

for item in vendas:
    valor = item['valor']
    categoria = item['categoria']
    if categoria in total_categoria:
        total_categoria[categoria] += valor
    else:
        total_categoria[categoria] = valor

print(total_categoria)