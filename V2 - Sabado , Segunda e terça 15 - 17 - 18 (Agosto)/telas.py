import random
import copy # Modulo de copia do python 
from combate import combateini
from inimigos import listainimigos
from vilas import vilamenu
from habilidades import listahabilidades
from magias import listamagias
from util import limpar_tela
from mundo import menumundo 

def menujogo(heroi):
    while True:
        limpar_tela()
        print(f"========== MENU PRINCIPAL ==========")
        escolha = input("1 - Vila\n2 - Seguir em frente\n3 - Exibir Status\n5 - Salvar jogo\n6 - Carregar Jogo\n0 - Sair do Jogo")
        if escolha == "1":
            input("Pressione ENTER para continuar...")
            vilamenu(heroi)

        elif escolha == "2":
            input("Pressione ENTER para continuar...")
            menumundo()

            #Inicia combate
            inimigoaleatório = copy.deepcopy(random.choice(listainimigos))
            combateini(heroi, inimigoaleatório)  # Os nomes dentro do parenteses da função, indicam quais valores/quem irá ser enviado para a função combate, lá na função, eu preciso definir no parenteses também, na mesma ordem, quem irá receber, e assim criar a logica usando o receptor

        elif escolha == "3":
            limpar_tela()
            heroi.mostrar_status()
            input("Pressione ENTER para continuar...")
