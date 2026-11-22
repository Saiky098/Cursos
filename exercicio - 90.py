"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

list_shopping = []

while True:
    choices = input("Escolha uma das opções: Inserir[1]  Excluir[2]  Lista[3]  Sair[4]\n ")  
    # print(list_shopping)

    if choices == '1' or choices == "Inserir":
        add_product = input("Digite o produto que deseja adicionar: ")
        if add_product.isdigit() == True:
            print("Produto Invalido")
            continue
        list_shopping.append(add_product.upper())
    
    elif choices == "Excluir" or choices == '2':
        if list_shopping == []:
            print("Sua Lista esta vazia.")
            continue
        
        for ind , name in enumerate(list_shopping):
            print(ind, name)
        try:
            delet_choise = input("Digite o nome ou numero do produto que deseja remover: ").upper()
            if delet_choise.isdigit() == True:
                del list_shopping[int(delet_choise)]
                print("Produto Eliminado com sucesso")
                print(ind, name)
            else:
                if delet_choise in list_shopping:
                    del list_shopping[list_shopping.index(delet_choise)]
                    print("Produto Eliminado com sucesso")
                    print(ind, name)
                else:
                    print("Não foi possivel encontrar esse produto")
                    continue
                    
        except:
            print("Produto não encontrado!")

    elif choices == "3" or choices == "Lista":
        if list_shopping == []:
            print("Lista esta vazia.")
            continue
        
        for ind, name in enumerate(list_shopping):
            print(ind, name)
    
    elif choices == "4" or choices == "Sair":
        print("Saindo do Sistema")
        break

    else:
        print("Essa opção não foi encontrada.")
         
          
        
        


      
