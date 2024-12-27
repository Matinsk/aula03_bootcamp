### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_api = 1
pagina_total = 5

while pagina_api <= pagina_total:
      print(f'processando a página atual {pagina_api} de {pagina_total}')
      pagina_api +=1 
print("todos dados consumidos com sucesso!")