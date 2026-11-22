""" Calculadora com while """


while True:
    first_number = int(input("Digite o primeiro numero = "))
    second_number = int(input("Digite o segundo numero = "))
    Operation = input("Qual operação deseja realizar? ")
    
    if Operation == "+":
        result = first_number + second_number
    if Operation == "-":
       result = first_number - second_number
    if Operation == "*":
        result = first_number * second_number
    if Operation == "/":
        result = first_number / second_number
    

    print("O resultado da sua operação sera {:.2f}".format(float(result)))
    ########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair == True:
        break

print("Calculadora encerrada")