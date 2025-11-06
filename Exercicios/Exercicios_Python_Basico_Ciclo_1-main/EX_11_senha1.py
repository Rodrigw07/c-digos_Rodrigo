# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

senha = int(input("digite sua senha: "))
senha_certa = 321321

if senha == senha_certa:
    print("senha correta")

else:
    print("senha incorreta")