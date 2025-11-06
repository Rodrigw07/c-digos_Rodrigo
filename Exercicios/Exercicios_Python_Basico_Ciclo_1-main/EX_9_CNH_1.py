# Escreva um programa simples que pede a idade do usuário e 
# depois mostre na tela com valor BOOLEANO (True ou False) se o usuário pode tirar a CNH (Carteira Nacional de Habilitação) ou não.
# Para tirar carteira no Brasil, a idade mínima é 18 anos.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite sua idade: 19
# Pode tirar carteira de motorista? True

# Exemplo 2:
# Digite sua idade: 17
# Pode tirar carteira de motorista? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

idade = int(input("qual é a sua idade: "))
resultado_cnh = input("Você foi Aprovado ou Reprovado?")
resultado_esperado = "aprovado"


if idade >= 18 and resultado_cnh == resultado_esperado:
    print("Pode tirar a carteira de motorista")

else: 
    print("Não pode tirar carteira de motorista")