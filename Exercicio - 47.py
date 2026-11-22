"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

n = input("Digite seu nome= ").replace('.','').replace(',','')

while n.isnumeric() == True or n == '':
        print("Dígito Incorreto! Digite seu nome")
        n = input("Digite seu nome= ").replace('.','').replace(',','')
     
i = input("Digite sua Idade= ")
    
while i.isnumeric() == False :
    print("Dígito Incorreto! Digite sua idade")
    i = input("Digite sua Idade= ")

nl = str(len(n))
space = 0
for s in n:
    if s == " ":
        space += 1

print("Seu nome é {n}\nInvertido:{ni}\nEle contém {s} espaços\nSeu nome tem {nl} letras \nA primeira letra do seu nome é {n[0]} e a ultima é {n2}".format(nl=nl,n=n,s=space,ni=n[::-1], n2=n[-1]))


