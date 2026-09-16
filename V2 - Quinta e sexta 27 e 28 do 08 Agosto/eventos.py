import random
from inimigos import boss_caverna, boss_montanhasgeladas, boss_floresta 
from combate import combatesys
from combate import ativar_acampamento
evento1_concluido = False
evento2_concluido = False
evento3_concluido = False
evento4_concluido = False

def acampamento(heroi):
    print("Você monta um acampamento...")
    input("Pressione ENTER para continuar...")
    cura = heroi.vidamax * 0.30
    heroi.vida = int(min(heroi.vidamax, heroi.vida + cura))
    mana = heroi.manamax * 0.30
    heroi.mana = int(min(heroi.manamax, heroi.mana * mana))
    print(f"Você recuperou HP {int(cura)} e MP {int(mana)}")
    heroi.mostrar_status()
    input("Pressione ENTER para continuar...")
    teste = random.randint(1,10)
    if teste >= 3: # 70% de Chance de evento
        eventoaleatorio = random.choice([evento_bau, evento_erva, evento_erva, evento_fada])
        eventoaleatorio(heroi) 

def evento_erva(heroi): # Evento dentro do acampamento
    print("\n[EVENTO] Você encontra uma planta de aparência estranha perto do acampamento.")
    escolha = input("Deseja comê-la? (1 - Sim / 2 - Não): ")
    
    if escolha == "1":
        efeito = random.choice(["cura", "veneno"])
        if efeito == "cura":
            heroi.vida = min(heroi.vidamax, heroi.vida + 20)
            print("A erva tinha propriedades curativas! Você recuperou 20 de HP.")
            input("Pressione ENTER para continuar...")
        else:
            heroi.vida -= 10
            print("A erva era venenosa! Você perdeu 10 de HP.")
            input("Pressione ENTER para continuar...")
    else:
        print("Você prefere não arriscar.")

def evento_fada(heroi): # Evento dentro do acampamento
    print("\n[EVENTO] Uma luz brilhante surge em volta... É uma fada?!")
    print("Você tem a escolha de se aproximar...")
    while True:
        escolha = input("Oque fazer? \n1 - Aproximar \n2 - Não fazer nada")
        if escolha == "1":
            teste = random.randint(1,10)
            if teste > 5:
                print("A fada sorriu...")
                input("Pressione ENTER para continuar...")
                print("Ela canaliza uma energia mágica em você antes de desaparecer.")
                heroi.manamax += 10
                print("Seu MP aumentou permanentemente em +10!")
                input("Pressione ENTER para continuar...")
                return
            else:
                print("Não era uma fada...")
                input("Pressione ENTER para continuar...")
                print("Era uma armadilha de algum monstro inimigo, você teve que gastar energia para não ser pego")
                heroi.mana -= 10
                print("Perdeu -10 de MP...")
                input("Pressione ENTER para continuar...")
                return

        elif escolha == "2":
            print("Você resolveu apenas ignorar e ir embora...")
            input("Pressione ENTER para continuar...")
            return

        else:
            print("Opção invalida")
        
def evento_bau(heroi): # Evento dentro do acampamento
    print("\n[EVENTO] Você encontra um baú velho enterrado perto da sua barraca!")
    escolha = input("Deseja abrir? (1 - Sim / 2 - Não): ")
    
    if escolha == "1":
        sorte = random.randint(1, 10)
        if sorte > 4:  # 60% de chance de recompensa
            ganho = random.randint(9, 20)
            heroi.ouro += ganho
            print(f"Sucesso! Você encontrou {ganho} de ouro dentro do baú!")
            input("Pressione ENTER para continuar...")
        else:          # 40% de chance de armadilha
            dano = random.randint(5, 10)
            heroi.vida -= dano
            print(f"Era uma armadilha de agulhas! Você tomou {dano} de dano.")
            input("Pressione ENTER para continuar...")
    else:
        print("Você decide não arriscar e ignora o baú.")
        input("Pressione ENTER para continuar...")

def evento_mercador(heroi):
    print("\n[EVENTO] Um mercador ambulante senta ao lado da sua fogueira!")
    print(f"Ele oferece uma Poção Especial que faz (decidir ainda quanto cura, ou oque faz) e custa {custo}.") # Modificar
    custo = 15
    escolha = input("Deseja comprar? (1 - Sim / 2 - Não): ")
    if escolha == "1":
        if heroi.ouro >= custo: # Preço do item
            heroi.ouro -= custo     # Quanto tira
            heroi.vida = min(heroi.vidamax, heroi.vida + 50)
            print("Você comprou e tomou a poção! E ")       # modificar
            input("Pressione ENTER para continuar...")
        else:
            print("Você não tem ouro suficiente...")
            input("Pressione ENTER para continuar...")
    else:
        print("O mercador deseja boa sorte e vai embora.")
        input("Pressione ENTER para continuar...")

def evento_vila_inical(heroi): 
    global evento1_concluido
    while evento1_concluido == False:
        print("[EVENTO] Você vê que a guilda de aventureiros está reunindo caçadores para participar de uma caça aos monstros...")
        escolha = input("Você pode: \n1 - Participar\n2 - Não Participar") 
    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return
    
def evento_pesca_vila(heroi):        # Fazer ainda / Talvez ter a chance de lutar contra boss peixe que da algo muito foda 
    global evento2_concluido
    while evento2_concluido == False:
        print("[EVENTO] Você vê que a guilda de aventureiros está reunindo caçadores para participar de uma caça aos monstros...")
        escolha = input("Você pode: \n1 - Participar\n 2 - Não Participar") 
    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return

def evento_festival_da_neve(heroi):      # Fazer ainda / TALVEZ colocar chance de lutar contra boss yeti que da algo top
    global evento3_concluido
    while evento3_concluido == False:
        print("[EVENTO] Você vê que a guilda de aventureiros está reunindo caçadores para participar de uma caça aos monstros...")
        escolha = input("Você pode: \n1 - Participar\n 2 - Não Participar") 
    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return

def evento_raid_vila_destruida(heroi):
    global evento2_concluido
    while evento2_concluido == False:
        from vilas import item_raid_vila
        print("[EVENTO][PERIGO!] Você escuta alguns aldeões aflitos, parece que alguns monstros MUITO fortes estão prestes a tentar invadir a vila...")
        escolha = input("Oque fazer?\n1 - Lutar\n2 - Ignorar\n")
        if escolha == "1":
            global ativar_acampamento
            item_raid_vila
            ativar_acampamento = False

            print("Você fica para lutar...")
            input("Pressione ENTER para continuar...")
            chefe = boss_floresta
            combatesys(heroi, chefe)        # Já inicia sistema de luta, evitando poder fugir da luta e evitando re-ligar o acampamento 
            chefe = boss_caverna
            combatesys(heroi, chefe)
            chefe = boss_montanhasgeladas
            combatesys(heroi, chefe)
            # Recompensa do jogador é ativada dentro da verificação do ferreiro
            print("Parabéns você venceu a RAID!\nUm dos inimigos deixaram um material SUPER RARO, tente falar com o ferreiro!")
            item_raid_vila = True

        elif escolha == "2":
            print("Você decide ir embora sem fazer nada...")

        else:
            print("Escolha invalida...")

    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return