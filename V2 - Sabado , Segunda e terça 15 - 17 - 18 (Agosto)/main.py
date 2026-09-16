#Telas/Menus
from telas import menu
#Jogador
from heroi import Heroi
#Inimigo
from inimigos import listainimigos
from inimigos import Inimigo
# Combate
from combate import combateini
from combate import combatesys

# "Agora tudo precisa virar classe?"
# A resposta é: não
# O objetivo não é transformar tudo em classe. O objetivo é colocar em classes aquilo que representa um objeto do jogo.
 # Por que função?
# Porque o combate é um evento.
# Não é uma coisa.

# Main

input("Bem vindo a RPG OVERWORLD 2 \nPressione ENTER para continuar...")
jogador = Heroi(input("Digite o nome do seu personagem: "))
jogador.mostrar_status()
print("\nAs regras do jogo são simples, veja: ")
print
input("Pressione ENTER para continuar...")
menu(jogador)


# Combate ta indo bem rapido, porém, falta fazer magias e poçoes funcionar
# Fazer Lojas funcionarem