#Telas/Menus
from telas import menujogo
#Jogador
from heroi import Heroi


# Main
jogador = Heroi(input("Bem vindo a RPG OVERWORLD 2\nDigite o nome do seu personagem: "))
jogador.mostrar_status()
print("\nAs regras do jogo são simples, veja: ")
print("Digite os números conforme as opções relacionadas para fazer suas ações, ")
input("Pressione ENTER para continuar...")
menujogo(jogador)


# Refatorando TODA a parte de itens, pois para usar pocoes, armaduras e armas no mesmo inventário, vou precisar criar uma classe somente para itens ele como modelo para outros
# Acho que deixarei isso para o V2


# Criar modo na vila de impedir o farm na região que você está, usando uma flag 
# Terminar de configurar a chamar boss do mundo , Além disso colocar contador de monstros derrotados pela vila e depois fazer ele zerar quando finalizado
# Terminar de criar/alterar o ferreiro / Parte de alterar atributos / armas e defesa / Menu em looping
# Criar logica de escolher pocão enumerate
# Criar o evento de pesca , neve , e finalizar o inicial
# Ir colocando o LIMPAR TELA junto com o input("Pressione ENTER para continuar...") para deixar o jogo limpo e visivel sem pular qualquer info importante

# Terminar de fazer SAVE/LOAD parte do inventário de poções magias e skills


# Teste deu certo da logica id, item in enumerate(ferreiro_espadas) / Agora só aprender depois em como usar ela para seleção de escolha de itens tanto em inventários ou ações
        #while True:
            # print("============ FERREIRO ============")
            # print("Você pode comprar novas ESPADAS e novas ARMADURAS")
            # escolha = input("Qual sua decisão?\n1 - Comprar Espadas\n2 - Comprar Armaduras\n0 - Sair do Ferreiro")
            # if escolha == "1":
            #     for id, item in enumerate(ferreiro_espadas): # TESTE DE NUMERAR usando o comando (ENUMERATE) e er como fazer escolha com ele, caso der certo, poderei remover o ID dos itens na lista e na classe
            #         print(f"{id}, {item.nome}")