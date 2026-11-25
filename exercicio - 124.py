# Exercício - sistema de perguntas i + 1 respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

list_ = ["A","B","C","D"]

# print(perguntas[0].get('Opções'))
# for question in perguntas:
#     print(question['Pergunta'])  
# raise SystemExit

for i in range(len(perguntas)):
    print(f"{perguntas[i].get('Pergunta')}\n {list_[0]}){perguntas[i].get('Opções')[0]}\n {list_[1]}){perguntas[i].get('Opções')[1]}\n {list_[2]}){perguntas[i].get('Opções')[2]}\n {list_[3]}){perguntas[i].get('Opções')[3]}")
    while True:
        result = input("\nQual é a resposta correta?")

        if result.isnumeric() == False:
            match result.upper():
                case "A": result = 0
                case "B": result = 1
                case "C": result = 2
                case "D": result = 3
        else:
            if result not in perguntas[i].get('Opções'):
                print("Opção invalida!")
                continue

            for n , x in enumerate(perguntas[i].get('Opções')):
                if result == x: result = n; break
        break

    if perguntas[i].get('Resposta') == perguntas[i].get('Opções')[int(result)]:
        print("Resposta Correta!\n")
    else:
        print("Resposta Incorreta!\n")
        
