### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 45
email = "josé@gmail.com"

email_rost = email.split("@")[1]
rost_validos = ['gmail.com','outlook.com','yahoo.com','gmail.com.br','outlook.com.br','yahoo.com.br']


if email_rost in rost_validos:
    validacao_email = "email validado"
else:
    validacao_email = "email incorreto"

if idade >= 18 and idade <= 65:
    validacao_idade = "idade validada"
else:
    validacao_idade = "idade incorreta"

if validacao_idade and validacao_email:
    print("Dados validados")
else:
    print("Error: Dados incorretos")
