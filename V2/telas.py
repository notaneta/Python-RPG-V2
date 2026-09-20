from util import limpar_tela, Cores
from mundo import menumundo 
from vilas import vila5_finalverdadeiro
from database import salvar_heroi
from database import carregar_heroi
import sys, atexit

def menujogo(heroi):
    while True:
        limpar_tela()

        print("╔" + "═" * 46 + "╗")
        print("║" + "MENU PRINCIPAL".center(46) + "║")
        print("║" + "─" * 46 + "║")
        print("║" + "Escolha uma opção".center(46) + "║")
        print("╚" + "═" * 46 + "╝")
        print()
        print(f"  Herói:  {heroi.nome}")
        print(f"  Ouro:   {heroi.ouro}")
        print()
        print("  " + "─" * 44)
        print(f"  [1]  {heroi.vila_atual.nome}")
        print("  [2]  Seguir em frente")
        print("  [3]  Status / Inventário")
        print("  [4]  Salvar jogo")
        print("  [5]  Carregar Jogo")
        print("  [9]  Sair do Jogo")
        print("  " + "─" * 44)
        print()
        escolha = input("  Qual sua decisão? ")
        


        if escolha == "1":
            from mundo import zona5_abismo
            if heroi.zona_atual == zona5_abismo:
                print("Você só tem a escolha de avançar...")
                input("Pressione ENTER para continuar...")

            else:
                 heroi.vila_atual.vilamenu(heroi)

        elif escolha == "2":            
            menumundo(heroi)

        elif escolha == "3":
                while True:
                    escolha2 = input("\n1 - Status Heroi\n2 - Inventário poções\n3 - Magias Aprendidas\n4 - Habilidades Aprendidas\n0 - Voltar\n")
                    if escolha2 == "1":
                        heroi.mostrar_status()
                        input("\nPressione ENTER para continuar...")
                        break

                    elif escolha2 == "2":
                        heroi.mostrar_inventario_pocoes()
                        input("\nPressione ENTER para continuar...")
                        break

                    elif escolha2 == "3":
                        heroi.mostrarmagias()
                        input("\nPressione ENTER para continuar...")
                        break

                    elif escolha2 == "4":
                        heroi.mostrarSkill()
                        input("\nPressione ENTER para continuar...")
                        break

                    elif escolha2 == "0":
                        break

        elif escolha == "4":
            print("Jogo salvo!")
            salvar_heroi(heroi)
            input("Pressione ENTER para continuar...")

        elif escolha == "5":        
            heroi = carregar_heroi()
            heroi.mostrar_status()
            print("Jogo carregado!")
            input("Pressione ENTER para continuar...")

        elif escolha == "9":
            print("Você saiu do jogo, até logo!")
            atexit.register(lambda: salvar_heroi(heroi))
            sys.exit()

        else:
            print("Comando não existe")


