nome = input("nome do usuario: ")
senha = input("senha do usuario: ")

if nome == "admin" and senha == "1234":
    print("Acesso permitido!")
else:
    print("Acesso negado!")