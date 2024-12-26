### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que: Temperatura < 18°C é 'Baixa' Temperatura >= 18°C e <= 26°C é 'Normal' Temperatura > 26°C é 'Alta'


temparatura = 30

try:
    temparatura = float(temparatura)
    if temparatura < 18:
       classificacao = "Baixa"
    elif temparatura <= 26:
        classificacao = "Normal"
    else:
        classificacao = "Alta"
    print(f'A Classificação da temperatura é: {classificacao}')
except:
    print("Error do tipo de dados")

