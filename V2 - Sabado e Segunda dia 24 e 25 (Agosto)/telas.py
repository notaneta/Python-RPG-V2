from combate import combateini
from util import limpar_tela
from mundo import menumundo 
from vilas import Vila_atual
from database import salvar_heroi
from database import carregar_heroi


def menujogo(heroi):
    while True:
        
        limpar_tela()
        print(f"========== MENU PRINCIPAL ==========")
        escolha = input(f"1 - {Vila_atual.nome}\n2 - Seguir em frente\n3 - Exibir Status\n4 - Salvar jogo\n5 - Carregar Jogo\n0 - Sair do Jogo")
        if escolha == "1":
            
            Vila_atual.vilamenu(heroi)

        elif escolha == "2":            
            menumundo(heroi)

        elif escolha == "3":
            limpar_tela()
            heroi.mostrar_status()
            input("Pressione ENTER para continuar...")

        elif escolha == "4":
            print("Jogo salvo!")
            salvar_heroi(heroi)
            input("Pressione ENTER para continuar...")

        elif escolha == "5":        
            heroi = carregar_heroi()
            heroi.mostrar_status()
            input("Continuar carregando esse save? \n1 - Sim\n2 - Não")