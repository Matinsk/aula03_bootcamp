### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

var = True

while var:
    num1 = input("Digite um número entre 1 e 10: ")
    try:
        num1 = float(num1)
        if num1 >= 1 and num1 <= 10:
            print("Número adicionado")
            var = False
    except:
        print("Digite um número correto")

