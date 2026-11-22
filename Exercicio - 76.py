import random 
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

list_word = ["perspectiva","piloto","aplaudir"]
random_list = random.choice(list_word)

new_lyrics = len(random_list) * "*"

sequency = 0
skip = False
while "*" in new_lyrics:
    if sequency < 1:
        question_word = input("Digite uma letra = ")
    else:
        question_word = input("Digite outra letra = ")
        
    while len(question_word) > 1 or question_word.isdigit() == True:
        print("Digite apenas uma letra!\nNumeros não são permitidos.")
        question_word = input("Digite uma letra = ")

    if question_word in random_list:
        
        for i, i_value in enumerate(random_list):
            print(f"{i=}, {i_value=}")
            if i_value == question_word:
                new_lyrics = new_lyrics[:i] + i_value + new_lyrics[i + 1:]
                skip = True
    
    elif skip != True:
            skip = ""
            print("Letra não encontrada") 
    skip = ""     

    sequency += 1

    print(new_lyrics)

print(f"Parabens a palavra foi descoberta!\nVocê tentou {sequency:.0f} vezes")
           