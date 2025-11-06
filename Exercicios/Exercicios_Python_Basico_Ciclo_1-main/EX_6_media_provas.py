# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

aluno = input("qual o nome do aluno: ")
nota1 = float(input("qual a sua nota da primira_prova: "))
nota2 = float(input("qual a nota da segunda_prova: "))
nota3 = float(input("qual a nota da terceira_prova: "))

media = (nota1+nota2+nota3)/3

if media >= 5.0 and media <=10.0:
    print("Aprovado")

elif media <= 4.9 and media >= 3.0:
    print("recuperação")

elif media <=2.9:
    print("reprovado")  

else:
    print()