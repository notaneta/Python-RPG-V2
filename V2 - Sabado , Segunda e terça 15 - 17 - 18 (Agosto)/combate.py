import random
import sys
from util import limpar_tela
from itens import usaritem
from magias import usarmagia
from habilidades import usarfoco
from eventos import acampamento
from habilidades import listahabilidades
from magias import listamagias


def combateini(heroi, inimigo):   # Heroi e inimigo dentro do parenteses, recebem os dados que foram enviados em ordem no parenteses do main
    while True:
        limpar_tela()
        print("Um inimigo apareceu!")
        inimigo.mostrar_status()
        escolha = input("Qual sua decisão? \n1 - Lutar\n2 - fugir: ")
        if escolha == "1":
                print("A luta começa")
                combatesys(heroi, inimigo)          # Como o combateINI já recebeu os dados, aqui só peço para ele compartilhar os dados com a outra função
                return
        elif escolha == "2":
            testefugir = random.randint(1, 10) 
            if testefugir >= 5:
                print("Você fugiu com sucesso")
            else:
                print("Você não conseguiu fugir e terá que lutar")
                print("A luta começa")
                combatesys(heroi, inimigo)
                return

def combatehud(heroi, inimigo): 
    print(f"============ {heroi.nome.upper()} ============    ||    ============ {inimigo.nome.upper()} ============")                    
    print(f"Vida: {heroi.vida}/{heroi.vidamax}    Mana: {heroi.mana}/{heroi.manamax}       ||    Vida: {inimigo.vida}/{inimigo.vidamax}")       
    print(f"Ataque: {heroi.ataque}       Defesa: {heroi.defesa}         ||    Ataque: {inimigo.ataque}")
    print(f"Fúria: {int(heroi.foco)}%                          ||")   

def combatesys(heroi, inimigo):
    while heroi.vida > 0 and inimigo.vida > 0:
        limpar_tela()
        combatehud(heroi, inimigo)
        print("\nSua opções são:")
        lutar = input("1 - Atacar\n2 - Lançar Magia\n3 - Usar Item (Não passa o turno)\n4 - Usar Habilidade\nQual sua decisão? ")

        turnojogador = False

        if lutar == '1':
            turnojogador = True
            print(f"\nVoce ataca o {inimigo.nome} com sua espada e causa {heroi.ataque} de dano.")
            inimigo.vida -= heroi.ataque
            input("\nPressione ENTER para continuar...")
        

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

        if turnojogador and inimigo.vida > 0:
            ataquefinal = max(1, inimigo.ataque - heroi.defesa)
            heroi.vida -= ataquefinal
            print(f"\nO {inimigo.nome} te ataca causando {ataquefinal} de dano")
               
            heroi.foco = min(100, heroi.foco + (random.randint(10, 14) + heroi.nivel * 1.02))
            input("\nPressione ENTER para continuar...")

    else:
        if heroi.vida <= 0:
            print("\nSeu HP foi reduzido a 0, Você perdeu...")
            sys.exit()

        elif inimigo.vida <= 0:
            print(f"\nVocê derrotou o inimigo e Recebeu {inimigo.ouro} de OURO e {inimigo.xp} de XP")
            heroi.ouro += inimigo.ouro
            heroi.xp += inimigo.xp
            heroi.foco = 0
            input("\nPressione ENTER para continuar...")
            heroi.subirnivel(listahabilidades, listamagias)
            limpar_tela()

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
