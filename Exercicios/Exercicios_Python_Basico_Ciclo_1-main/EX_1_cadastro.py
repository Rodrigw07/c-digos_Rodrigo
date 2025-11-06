# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))
email = input("digite seu imail:")
senha = int(input("digite sua senha:"))

print(f"| ------------------------------ |")
print(f"| ---------- CADASTRO ---------- |")
print(f"| ------------------------------ |")
print(f"| Nome: {nome}")
print(f"| Idade: {idade}")
print(f"| Email: {email}")
print(f"| Senha: {senha}")

print("| ------------------------------ |")
print("| ----- USUÁRIO CADASTRADO ----- |")
print(f"| Seja bem vindo(a): {nome}!")
print(f"| Email: {email}")
print("| ------------------------------ |")