import random, copy
from inimigos import boss_caverna, boss_montanhasgeladas, boss_floresta, inimigos_floresta, inimigos_caverna, boss_yeti
from itens import poçoes
from combate import combatesys
from combate import ativar_acampamento
from lore import dialogo, copia_heroi_dialogo, copia_heroi_dialogo2
evento1_concluido = False
evento2_concluido = False
evento3_concluido = False
evento4_concluido = False
evento5_concluido = False
participou = False
participou1 = False
final_verdadeiro = False

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
        eventoaleatorio = random.choice([evento_bau, evento_erva, evento_emboscada, evento_fada, evento_fogueira, evento_tempestade, evento_livro, evento_pedagio_forcado, evento_assalto_noturno])
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

def evento_livro(heroi):
    print(
        "\n[EVENTO] Escondido entre as raízes de uma árvore próxima, você acha um livro antigo."
    )
    escolha = input(
        "Deseja folhear as páginas empoeiradas? (1 - Sim / 2 - Não): "
    )

    if escolha == "1":
        sorte = random.randint(1, 10)
        if sorte >= 4:  # 70% de chance de benefício
            heroi.ataque += 2
            print(
                "Você leu técnicas antigas de combate! Seu ATAQUE aumentou permanentemente em +2."
            )
        else:  # 30% de chance de maldição
            dano = 12
            heroi.vida -= dano
            print(
                f"Ao abrir o livro, uma névoa sombria emerge e atinge você! Perdeu {dano} de HP."
            )
    else:
        print("Você deixa o livro quieto na natureza.")
    input("Pressione ENTER para continuar...")

def evento_fogueira(heroi):
    print(
        "\n[EVENTO] A noite está tranquila. O som da fogueira acalma sua mente."
    )
    print("Você aproveita o tempo para afiar suas armas e refletir.")

    heroi.xp += 10
    print("Você ganhou +10 de XP pela meditação!")

    # Se o herói usa Foco, recupera Foco também
    if hasattr(heroi, "foco"):
        heroi.foco = min(heroi.focomax, heroi.foco + 20)
        print("Sua barra de FOCO irá começar com 20 pontos na proxima luta!")

    input("Pressione ENTER para continuar...")

def evento_emboscada(heroi):
    print(
        "\n[EVENTO] Barulhos no mato! Um monstro emboscou seu acampamento!")
    escolha = input("O que fazer? (1 - Pegar a espada e lutar / 2 - Apagar a fogueira e se esconder): ")

    if escolha == "1":
        print("Você se levanta rapidamente a tempo de repelir o ataque inicial!")
        input("Pressione ENTER para continuar...")
        # Importa a função de combate e um inimigo fraco/medio
        from combate import combateini
        from mundo import zona_atual

        inimigo = copy.deepcopy(random.choice(zona_atual.lista_inimigos))
        combateini(heroi, inimigo)

    elif escolha == "2":
        teste = random.randint(1, 10)
        if teste > 4:
            print("Você apagou o fogo a tempo e o monstro passou direto!")
            input("Pressione ENTER para continuar...")
        else:
            dano = 15
            heroi.vida -= dano
            print(f"Você tropeçou no escuro ao se esconder e tomou {dano} de dano!")
            input("Pressione ENTER para continuar...")

def evento_assalto_noturno(heroi):
    print(
        "\n[EVENTO OBRIGATÓRIO] Você acorda assustado com um barulho ao lado do seu saco de dormir!"
    )
    print("Um ladrão sorrateiro aproveitou seu sono profundo para cortar sua bolsa de moedas!")

    if heroi.ouro > 0:
        # Rouba entre 10 e 25 moedas (ou todo o ouro se tiver menos)
        perda = random.randint(10, 25)
        ouro_roubado = min(heroi.ouro, perda)
        heroi.ouro -= ouro_roubado
        print(f"O ladrão foge rapidamente para a escuridão da noite gargalhando!")
        print(f"Você perdeu {ouro_roubado} de ouro!")
    else:
        print("O ladrão mexeu nos seus bolsos, mas como você não tinha ouro, ele só te deu um chute e fugiu!")
        heroi.vida -= 10

    input("Pressione ENTER para continuar...")

def evento_pedagio_forcado(heroi):
    print(
        "\n[EVENTO OBRIGATÓRIO] Três bandidos armados cercam a sua fogueira!"
    )
    print("Líder dos Bandidos: 'Acampando em nossas terras sem pagar a taxa?'")

    # O valor do pedágio também sobe com o nível do herói
    valor_pedagio = heroi.nivel * 15
    print(
        f"Eles exigem {valor_pedagio} moedas de ouro para deixar você passar a noite em paz."
    )
    print(f"Seu Ouro atual: {heroi.ouro}")

    print(f"\n1 - Pagar o pedágio ({valor_pedagio} Ouro)")
    print("2 - Recusar e LUTAR!")

    escolha = input("\nQual a sua escolha? ")

    if escolha == "1":
        if heroi.ouro >= valor_pedagio:
            heroi.ouro -= valor_pedagio
            print(
                "\nLíder dos Bandidos: 'Sábia escolha. Tenha uma boa noite de sono... enquanto pode.'"
            )
            print(f"💸 Você pagou {valor_pedagio} de ouro.")
        else:
            print(
                "\nLíder dos Bandidos: 'Você não tem ouro suficiente?! Então vai pagar com a própria VIDA!'"
            )
            input("Pressione ENTER para puxar sua arma...")
            _iniciar_luta_pedagio(heroi)
    else:
        print("\nVocê se recusa a pagar e desembainha sua arma!")
        input("Pressione ENTER para iniciar a batalha...")
        _iniciar_luta_pedagio(heroi)

    input("\nPressione ENTER para continuar...")

def _iniciar_luta_pedagio(heroi):
    from combate import combateini
    from inimigos import Bandido

    inimigo = copy.deepcopy(Bandido)

    # Multiplicadores de atributo baseados no Nível do Herói:
    # Ajuste os valores base (ex: 25 de HP e 4 de Dano por nível) conforme o balanceamento do seu jogo
    inimigo.vidamax = heroi.nivel * 25
    inimigo.vida = inimigo.vidamax
    inimigo.ataque = heroi.nivel * 4
    inimigo.defesa = heroi.nivel * 2

    # Ajusta o ganho de recompensa proporcional ao nível
    inimigo.ouro = heroi.nivel * 12
    inimigo.xp = heroi.nivel * 20

    print(f"\n O Líder Bandido (Nível {heroi.nivel}) se prepara para atacar!")
    print(f"Status do Inimigo -> HP: {inimigo.vida} | Ataque: {inimigo.ataque} | Defesa: {inimigo.defesa}")
    input("Pressione ENTER para começar o combate...")

    combateini(heroi, inimigo)
    
def evento_tempestade(heroi):
    print(
        "\n[EVENTO OBRIGATÓRIO] 🌩️ O tempo vira bruscamente e uma tempestade severa atinge seu acampamento!"
    )
    print(
        "Sua tenda é levada pelo vento e a chuva gelada destrói sua fogueira."
    )

    dano_tempestade = random.randint(8, 15)
    heroi.vida = max(1, heroi.vida - dano_tempestade)  # Evita matar instantaneamente

    print(f"🥶 Você passa a noite no frio extremo e perde {dano_tempestade} de HP.")

    # Perda de Mana pela exaustão
    heroi.mana = max(0, heroi.mana - 10)
    print("Sua energia mágica foi desgastada (-10 de MP).")

    input("Pressione ENTER para continuar...")

def evento_mercador(heroi): # AINDA N DECIDI O TANTO QUE CURA
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

def evento_vila_inical(heroi): # Competição de Lenhadores Provavelmente 2* evento da vila / Se o ataque do jogador for maior que X ele ganha a disputa, ganhando ouro e XP 
    global evento1_concluido
    while evento1_concluido == False:
        print("[EVENTO] Você vê que a guilda de aventureiros está reunindo caçadores para participar de uma caça aos monstros...")
        escolha = input("Você pode: \n1 - Participar\n 2 - Não Participar") 

        if escolha == "1":
            global ativar_acampamento
            ativar_acampamento = False
            print("Você terá que lutar contra 3 inimigos seguidos")
            inimigo = copy.deepcopy(inimigos_floresta[0])
            combatesys(heroi, inimigo)
            print("Um dos aventureiros te entrega um item.")
            input("Pressione ENTER para continuar...")
            heroi.adicionar_pocoes(poçoes[1])
            input("Pressione ENTER para continuar...")
            combatesys(heroi, inimigo)
            print("Um dos aventureiros te entrega um item.")
            input("Pressione ENTER para continuar...")
            heroi.adicionar_pocoes(poçoes[1])
            input("Pressione ENTER para continuar...")
            inimigo = copy.deepcopy(inimigos_floresta[1])
            combatesys(heroi, inimigo)
            inimigo = copy.deepcopy(inimigos_floresta[3])
            combatesys(heroi, inimigo)
            print("Parabéns você derrotou todos os inimigos, a guilda te recompensou com 30 de ouro!")
            input("Pressione ENTER para continuar...")
            evento1_concluido = True
            return


        elif escolha == "2":
            return
            
    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return
    
def evento_pesca_vila(heroi):        # Fazer ainda / Baseado em randomizador, pode ganhar coisas aleatórias ou nada / Talvez ter a chance de lutar contra boss peixe que da algo muito foda 
    global evento2_concluido
    while evento2_concluido == False:
        print("[EVENTO] Você ficou sabendo que a vila tem um local famoso de pesca por perto...")
        escolha = input("Você pode: \n1 - Pescar\n 2 - Não Pescar") 
        if escolha == "1":
            print("Você resolveu pescar.")
            dialogo("...")
            dialogo("...")
            sorte = random.randint(0,10)

            if sorte == 10:
                print(f"De 0 a 10, sua sorte foi {sorte}, parabéns!")
                input("Pressione ENTER para continuar...")
                print("Você encontrou uma poção GRANDE e mais 30 ouros!")
                input("Pressione ENTER para continuar...")
                print("Com isso se sentiu muito animado e devido a isso ganhou mais 10+ XP")
                input("Pressione ENTER para continuar...")
                heroi.xp += 10
                heroi.ouro += 30
                heroi.adicionar_pocoes(poçoes[2])
                evento2_concluido = True
                return
            
            if sorte >= 7:
                print(f"De 0 a 10, sua sorte foi {sorte}!")
                input("Pressione ENTER para continuar...")
                print("Você encontrou 15 ouros!")
                input("Pressione ENTER para continuar...")
                print("Com isso se sentiu muito animado e devido a isso ganhou +5 XP")
                input("Pressione ENTER para continuar...")
                heroi.xp += 5
                heroi.ouro += 30
                evento2_concluido = True
                return

            if sorte >= 4:
                print(f"De 0 a 10, sua sorte foi {sorte}!")
                input("Pressione ENTER para continuar...")
                print("Você não conseguiu pescar nada.")
                print("Você se motiva a pensar que a proxima vez será melhor, e recebe +5 de XP! ")
                input("Pressione ENTER para continuar...")
                heroi.xp += 5
                evento2_concluido = True
                return


            if sorte >= 1:
                print(f"De 0 a 10, sua sorte foi {sorte}!")
                input("Pressione ENTER para continuar...")
                print("Durante a pesca, um inimigo tenta te atacar, você desvia e não tem escolha a não ser lutar!")
                inimigoaleatório = copy.deepcopy(random.choice(inimigos_caverna))
                combatesys(heroi, inimigoaleatório)
                evento2_concluido = True
                return

            if sorte == 0:
                print(f"De 0 a 10, sua sorte foi {sorte}, que azar!")
                print("Enquanto pescava, você se distraiu e tentaram te roubar!")
                if heroi.ouro > 10:
                    heroi.ouro -= 10
                    print("Você perdeu 10 de ouro.")
                    input("Pressione ENTER para continuar...")
                    

                else:
                    print("Como você não tinha ouro, nada aconteceu.")
                    input("Pressione ENTER para continuar...")

                evento2_concluido = True
                return





        elif escolha == "2":
            return
            
    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return

def evento_festival_da_neve(heroi):
    global evento3_concluido, participou, participou1
    from mundo import zona_atual

    while evento3_concluido == False or zona_atual.bossderrotado == False:

        print("[EVENTO ]FESTIVAL DA NEVE")
        print("As Montanhas Geladas estão em festa!")
        print("1 - Guerra de Bola de Neve")
        print("2 - Competição de Patinação")
        print("3 - Explorar a Floresta Congelada")
        print("4 - Sair")
        escolha = input("\nEscolha: ")
        # Guerra de Bola de Neve
        if escolha == "1" and participou == False:
            print("\nVocê participa da Guerra de Bola de Neve!")

            teste = random.randint(1, heroi.defesa)

            if teste >= 15:
                ouro = random.randint(40, 80)
                heroi.ouro += ouro

                print(f"Vitória! Você ganhou {ouro} de ouro.")
                input("Pressione ENTER para continuar...")
                participou = True
            else:
                print("Você foi atingido por várias bolas de neve e perdeu a competição!")
                input("Pressione ENTER para continuar...")

        # Patinação
        elif escolha == "2" and participou1 == False:

            print("\nVocê entra na competição de patinação!")
            teste = random.randint(1, heroi.sorte)

            if teste >= 10:
                xp = random.randint(30, 60)
                heroi.xp += xp

                print(f"Excelente apresentação! Você ganhou {xp} XP.")
                input("Pressione ENTER para continuar...")
            else:
                print("Você escorregou e caiu na neve.")
                input("Pressione ENTER para continuar...")
                participou1 = True

        # Área secreta com chance de boss
        elif escolha == "3":

            print("\nVocê segue uma trilha estranha na floresta congelada...")
            input("Pressione ENTER para continuar...")

            if random.randint(1, 100) <= 25:  # 25% de chance
                print("\nUm rugido ecoa pela montanha!")
                input("Pressione ENTER para continuar...")
                print("Um Yeti Lendário apareceu e vai lutar contra você!")
                input("Pressione ENTER para continuar...")

                boss = boss_yeti

                combatesys(heroi, boss)
                print("\nVocê derrotou o Yeti Lendário!")
                print("Você recebeu o artefato:")
                print("Coração de Gelo Ancestral")
                print("+15 Defesa")
                heroi.defesa += 15
                evento3_concluido = True
                dialogo("Moradores : Incrível!\nMoradores : O monstro das lendas foi derrotado!\nO Festival da Neve nunca mais será o mesmo...")
                input("Pressione ENTER para continuar...")

            else:
                print("Você encontra apenas uma bela paisagem congelada.")
                ouro = random.randint(20, 50)
                heroi.ouro += ouro
                print(f"Você encontrou {ouro} de ouro abandonado.")
                input("Pressione ENTER para continuar...")

        elif escolha == "4":
            break

        else:
            print("Escolha inválida.")
            input("Pressione ENTER para continuar...")

def evento_sombra(heroi):
    global evento4_concluido, final_verdadeiro

    print("Um espelho quebrado chama sua atenção...")

    escolha = input("\n1 - Aproximar-se\n2 - Sair\n")

    if escolha != "1":
            
        sombra = copy.deepcopy(heroi)
        sombra.nome = f"Sombra de {heroi.nome}"
        sombra.vida += 150
        sombra.vidamax += 150
        sombra.ataque = int(heroi.ataque * 1.10)

        copia_heroi_dialogo(heroi, sombra)

        combatesys(heroi, sombra)

        copia_heroi_dialogo2(heroi, sombra)
        evento4_concluido = True
        final_verdadeiro = True

    else:
        return


def evento_raid_vila_destruida(heroi):
    global evento5_concluido
    while evento5_concluido == False:
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
            evento5_concluido = True
        elif escolha == "2":
            print("Você decide ir embora sem fazer nada...")

        else:
            print("Escolha invalida...")

    else:
        print("O evento já foi concluido")
        input("Pressione ENTER para continuar...")
        return