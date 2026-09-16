from itens import poçoes
from util import limpar_tela
from magias import listamagias
from magias import magias

def menuloja(heroi):

    while True:
        limpar_tela()

        print("============ LOJA DO MAGO ============")
        print("Você pode comprar poções ou verificar sua aptidão com magias")
        escolha = input("Qual sua decisão?\n1 - Comprar poções\n2 - Verificar aptidão com magias\n0 - Sair da loja")
        if  escolha == "1":
            while True:
                print("============ LOJA DO MAGO ============")
                print("     ========== POÇÕES ==========     ")
                for Pocao in poçoes:
                    print("-" * 20)
                    Pocao.mostraritens()
                    print("-" * 20)

                escolha = input("Digite o N(ID) do item que deseja obter ou 0 para fechar a loja: ")
                for item in poçoes:
                    if item.id == escolha:
                        if heroi.ouro >= item.custo:        
                            nomeitem = item
                            heroi.adicionaritem(nomeitem)
                            heroi.ouro -= item.custo
                            print(f"Seu novo ouro é {heroi.ouro}")        
                            input("Pressione ENTER para continuar...")   

                        else:
                            print("Você não tem ouro suficiente...")
                            input("Pressione ENTER para continuar...")
                            
                    elif escolha == "0":
                        print("Você saiu da loja...")
                        input("Pressione ENTER para continuar...")
                        return
                    
        elif escolha == "2":
            print("O mago lê sua aptidão com magias...")
            for magia in listamagias:
                magia.mostrarmagias()

            input("Pressione ENTER para continuar...")

        elif escolha == "0":
            print("Você saiu da loja...")
            input("Pressione ENTER para continuar...")            
            return

            