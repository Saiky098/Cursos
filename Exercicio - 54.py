"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


# x = input("Digite um numero inteiro= ")
# while x.isdigit() == False:
#     print("Esse numero não é inteiro")
#     x = input("Digite um numero inteiro= ")

# x = int(x)
# if x %2 == 0:
#     print("O numero {} é Par".format(x))
# else:
#     print("O numero {} é Impar".format(x))

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# h = input("Quantas horas?").split(":")[0].strip()
# h = float(h)
# l = [float(i) for i in list(range(0,25))]
# # print(l[0:13])


# if h in l[0:13]:
#     print("Bom dia")
# elif h in l[13:18]:
#     print("Boa tarde")
# elif h in l[18:25]:
#     print("Boa noite")
# else:
#     print("hora não encontrada",f"{h=}" , f"{l=}")

# print(f"{h=}" , f"{l=}")


"""

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# n = input("Escreva seu primeiro nome= ")

# if len(n) <= 4:
#     print("Seu nome é curto")
# elif len(n) in (5,6):
#     print("Seu nome é normal")
# elif len(n) > 6:
#     print("Seu nome é muito grande")