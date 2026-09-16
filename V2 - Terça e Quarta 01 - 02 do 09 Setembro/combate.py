import random
import sys 
from util import limpar_tela, barra_hp, barra_mp, barra_furia, largura
from itens import usaritem
from magias import usarmagia, listamagias
from habilidades import usarfoco , listahabilidades

ativar_acampamento = True

def combateini(heroi, inimigo):   # Heroi e inimigo dentro do parenteses, recebem os dados que foram enviados em ordem no parenteses do main
    global ativar_acampamento
    ativar_acampamento = True   # Ativa o acampamento novamente
    while True:
        limpar_tela()
        print("Um inimigo apareceu!")
        inimigo.mostrar_status()
        escolha = input("Qual sua decisão? \n1 - Lutar\n2 - Fugir (Chance de 50%)\n")
        if escolha == "1":
                combatesys(heroi, inimigo)          # Como o combateINI já recebeu os dados, aqui só peço para ele compartilhar os dados com a outra função
                return
        elif escolha == "2":
            testefugir = random.randint(1, 10) 
            if testefugir >= 5:
                print("Você fugiu com sucesso")
                input("Pressione ENTER para continuar...")
                break
            else:
                print("Você não conseguiu fugir e terá que lutar")
                input("Pressione ENTER para continuar...")
                combatesys(heroi, inimigo)
                return

def combatehud(heroi, inimigo): 
    print(f"{heroi.nome}")
    print(f"HP [{barra_hp(heroi.vida, heroi.vidamax)}] "f"{heroi.vida}/{heroi.vidamax}")
    print(f"MP [{barra_mp(heroi.mana, heroi.manamax)}] "f"{heroi.mana}/{heroi.manamax}")
    print(f"Fúria [{barra_furia(heroi.foco, heroi.focomax)}] "f"{heroi.foco}/{heroi.focomax}")
    print(f"Ataque: {heroi.ataque}       Defesa: {heroi.defesa}")
    print("=" * largura)
    print(f"{inimigo.nome}")
    print(f"HP [{barra_hp(inimigo.vida, inimigo.vidamax)}] "f"{inimigo.vida}/{inimigo.vidamax}")
    print(f"Ataque: {inimigo.ataque}")      # Posteriormente na proxima versão colocar na HUD a defesa dos monstros de cada um, pois vai ajudar a deixar o combate mais complexo, alguns melhores contra espada e outros contra magia


def combatesys(heroi, inimigo):
    while heroi.vida > 0 and inimigo.vida > 0:
        limpar_tela()
        combatehud(heroi, inimigo)
        print("\nSua opções são:")
        lutar = input("1 - Atacar\n2 - Lançar Magia\n3 - Usar Item (Não passa o turno)\n4 - Usar Habilidade\n")

        turnojogador = False

        if lutar == '1':        # Comando de ataque jogador dentro da class dele
            turnojogador = True
            heroi.atacar(inimigo)

        elif lutar == "2":
            turnojogador = usarmagia(heroi, inimigo)

        elif lutar == '3':
            usaritem(heroi)

        elif lutar == "4":
            if heroi.foco == 100:
                turnojogador = usarfoco(heroi, inimigo)

            else:
                print("\nVocê ainda não tem fúria suficiente...")
                input("\nPressione ENTER para continuar...")

        if turnojogador and inimigo.vida > 0:           # Comando de ataque inimigo dentro da classe dele
            inimigo.atacar(heroi)     # Foco do heroi é gerado no comando de atacar do inimigo / Assim caso a ação se repita, o foco gera também
            if inimigo.habilidade is not None:
                inimigo.habilidade(heroi, inimigo)      # Habilidade só é executada caso a vida do boss esteja no nivel correto conforme ele mesmo dispor

    # Logica Game over

    else:
        if heroi.vida <= 0:
            print("\nSeu HP foi reduzido a 0, Você perdeu...")
            sys.exit()

        # Logica vecer batalha 

        elif inimigo.vida <= 0:
            print(f"\nVocê derrotou o inimigo e Recebeu {inimigo.ouro} de OURO e {inimigo.xp} de XP")
            heroi.ouro += inimigo.ouro
            heroi.xp += inimigo.xp
            heroi.foco = 0
            input("\nPressione ENTER para continuar...")
            heroi.subirnivel(listahabilidades, listamagias)
            limpar_tela()
            from mundo import zona_atual
            zona_atual.avançarjogo()          # Contabiliza a luta para a PROGRESSÃO do jogo

            # Evento acampamento
            
            if ativar_acampamento == True: # Verifica se acampamento é permitido, ele é desligado no evento da vila destruida, pois é uma RAID de inimigos sem descanso 
                from eventos import acampamento
                while True:
                    print("Depois da batalha, você encontra um local para acampar...")
                    print("1 - Acampar  (Restaura 30% HP/MP) Risco de evento")
                    print("2 - Voltar")
                    
                    escolha = input("\nOque fazer? ")
                    if escolha == "1":
                        acampamento(heroi)
                        return

                    elif escolha == "2":
                        return

                    else:
                        print("Opção invalida")
                        input("Pressione ENTER para continuar...")
