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
print(f"{jogador.nome} você foi invocado para outro mundo com a missão de salva-lo, e para isso precisará derrotar as forças do Lorde Demoniaco")
print("\nREGRAS e INFORMAÇÕES:\n\nDificuldade Padrão: Dificil\nTotal de Áreas: 4\nChegue até a 4* Área do Jogo para Enfrentar o Boss Final\nDerrote 5 inimigos para iniciar a batalha contra o chefe e poder progredir para a próxima área\nItens Exclusivos podem ser desbloqueados a medida que o jogo passar")
print("Digite os números conforme as opções relacionadas para escolher suas ações")
input("\nPressione ENTER para continuar...")
menujogo(jogador)

# Posteriormente fazer um seletor de DIFICULDADE no V2.5 
# Quando for fazer o EQUIPAMENTO de armaduras e espadas no inventário, fazer a remoção do valor de ataque do item no jogador e somar pelo do novo
# Refatorando TODA a parte de itens, pois para usar pocoes, armaduras e armas no mesmo inventário, vou precisar criar uma classe somente para itens ele como modelo para outros
# Nova ideia de teste para INVENTÁRIO, criar um só porém nele usar filtros para pesquisa de itens no comando de exibição
# Acho que deixarei isso para o V2 
# E deixaria o Boss Rush para uma atualização futura, talvez: Arena dos Campeões ou Modo Desafio
# Fazer sistema em algumas batalhas opcionais o boss não te mata e só vai embora (sistema de game over que só funciona nas batalhas principais por exemplo)
# Poder voltar em vilas antigas



#                               FAZER EM CASA
# Ir colocando o LIMPAR TELA junto com o input("Pressione ENTER para continuar...") para deixar o jogo limpo e visivel sem pular qualquer info importante
# Terminar de fazer SAVE/LOAD parte do inventário de poções magias e skills 
# Fazer um ranking online de quem terminou mais forte / ou pontos acumulados e com os bosses derrotados 
# Logica (Evento da vila -> Luta contra sombra -> Se DERROTOU: Boss final VERDADEIRO é liberado , Else: Final falso é liberado # Boss secreto da zona não existe)
# Talvez criar mais poções uma para cada região e amuletos também



# Criei final verdadeiro e final (TESTAR EM CASA SE FUNCIONOU)
# Dialogo do boss final é executado durante a verificação do mundo (TESTAR EM CASA SE FUNCIONOU)
# Criado todos os eventos de vila, falta apenas testar (TESTAR EM CASA SE FUNCIONOU)
# USAR POÇÃO agora é com enumerate (TESTAR EM CASA SE FUNCIONOU)
# Acho que com o IF na opção de TELAS, onde ele verifica a ultima vila ele provavelmente deve barra o jogador de acessar a vila (TESTAR EM CASA SE FUNCIONOU)
# TESTE DE VENENO na habilidade do boss especial aranha, e 2 habilidades em 1 boss (TESTAR EM CASA SE FUNCIONOU)
# TESTAR habilidade do boss de gelo    efeito STUN no combate  (TESTAR EM CASA SE FUNCIONOU)
# Testar contador de stun da HUD (TESTAR EM CASA SE FUNCIONOU)