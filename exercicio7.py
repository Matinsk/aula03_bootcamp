usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]



usuarios_validos = [usuario for usuario in usuarios if usuario['email']]

print(usuarios_validos)