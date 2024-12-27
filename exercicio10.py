### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.


var = True

while var:
    texto = input ("Digite uma palavra : ")
    if texto == "sair":
        var = False
    else:
        pass