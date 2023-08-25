login = ''
senha = 0

while login != 'carlos' or senha != 12345:
    login = input("Digite seu login: ")
    senha = int(input("Digite sua senha: "))

print(f"Bem vindo, {login}!")