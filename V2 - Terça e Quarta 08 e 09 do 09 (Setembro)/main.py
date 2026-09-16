from telas import menujogo
from heroi import Heroi
from database import menu_principal
from util import limpar_tela
# Main

limpar_tela()
menu_principal()    # Tela de Carregamento do jogo antes do jogo iniciar.
limpar_tela()

jogador = Heroi(input("Bem vindo a RPG OVERWORLD 2\nDigite o nome do seu personagem.\n"))
jogador.mostrar_status()
print("\nREGRAS e INFORMAÇÕES:\n\nDificuldade Padrão: Dificil\nTotal de Áreas: 4\nChegue até a 4* Área do Jogo para Enfrentar o Boss Final\nDerrote 5 inimigos para iniciar a batalha contra o chefe e poder progredir para a próxima área\nItens Exclusivos podem ser desbloqueados a medida que o jogo passar")
print("Digite os números conforme as opções relacionadas para escolher suas ações")
input("\nPressione ENTER para continuar...")
menujogo(jogador)

# Posteriormente fazer um seletor de DIFICULDADE no V2.5 
# Quando for fazer o EQUIPAMENTO de armaduras e espadas no inventário, fazer a remoção do valor de ataque do item no jogador e somar pelo do novo
# Refatorando TODA a parte de itens, pois para usar pocoes, armaduras e armas no mesmo inventário, vou precisar criar uma classe somente para itens ele como modelo para outros
# Nova ideia de teste para INVENTÁRIO, criar um só porém nele usar filtros para pesquisa de itens no comando de exibição
# Acho que deixarei isso para o V2 


# Terminar de criar as outras Áreas , inimigos e bosses             (fazer no trampo)
# Criar logica de escolher pocão enumerate                          (fazer no trampo)
# Criar o evento de pesca , neve , e finalizar o inicial            (fazer no trampo)
# poção tem que ser trocada logica para escolha de enumerate que nem a do ferreiro      (fazer no trampo)


# Ir colocando o LIMPAR TELA junto com o input("Pressione ENTER para continuar...") para deixar o jogo limpo e visivel sem pular qualquer info importante
# Adicionado e substituido espadas e armaduras por amuletos, eles vão simplificaro ferreiro por hora, apenas aumentando o valor de ataque ou defesa, sem subtrair o anterior, ou sem menu de equipamento, faz mais sentido o amuleto estacar do que uma armadura ou espada estacar
# Foco Gen PODE SER upado ao derrotar boss, ou eventos especiais como bosses especias das áreas
# Terminar de fazer SAVE/LOAD parte do inventário de poções magias e skills







# Teste deu certo da logica id, item in enumerate(ferreiro_espadas) / Agora só aprender depois em como usar ela para seleção de escolha de itens tanto em inventários ou ações
        #while True:
            # print("============ FERREIRO ============")
            # print("Você pode comprar novas ESPADAS e novas ARMADURAS")
            # escolha = input("Qual sua decisão?\n1 - Comprar Espadas\n2 - Comprar Armaduras\n0 - Sair do Ferreiro")
            # if escolha == "1":
            #     for id, item in enumerate(ferreiro_espadas): # TESTE DE NUMERAR usando o comando (ENUMERATE) e er como fazer escolha com ele, caso der certo, poderei remover o ID dos itens na lista e na classe
            #         print(f"{id}, {item.nome}")