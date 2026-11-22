# Exercício - sistema de perguntas e respostas


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

print(f"{perguntas[0].get('Pergunta')}\n {list_[0]}){perguntas[0].get('Opções')[0]}\n {list_[1]}){perguntas[0].get('Opções')[1]}\n {list_[2]}){perguntas[0].get('Opções')[2]}\n {list_[3]}){perguntas[0].get('Opções')[3]}")
result = input("\nQual é a resposta correta?")

if result.isnumeric() == False:
    match result.upper():
        case "A": result = 0
        case "B": result = 1
        case "C": result = 2
        case "D": result = 3
else:
    match int(result):
        case 1: result = 0
        case 3: result = 1
        case 4: result = 2
        case 5: result = 3
        case _: result = 0
              
         
if perguntas[0].get('Resposta') == perguntas[0].get('Opções')[result]:
    print("Resposta Correta!")
else:
    print("Resposta Incorreta!")
