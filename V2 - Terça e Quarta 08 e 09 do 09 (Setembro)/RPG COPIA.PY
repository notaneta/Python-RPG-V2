# Bibliotecas
import os
import random
import sys

# Parametros básicos do codigo
vidamax = 80
vida = 80
magia = 27
magiamax = 27
valor_ataque = 4
ouro = 20
xp = 0
xp_prox_nv = 20
nivelheroi = 1

magias_aprendidas = {  # Armazena as magias do heroi
    "1": {"Nome": "Chamas de Fogo", "Dano": 8, "Customagia": 17},
    "2": {"Nome": "Golpe da Espada Flamejante", "Dano": 17, "Customagia": 50},}

contarlutas = 0  # contará quantas lutas foram feitas até agora, chegando em 3 o chefe aparece
lutafinal = 0  # Caso chegue em 5 será ativado luta final do jogo (após 5 chefes)
Endgame = 1  # Servira para caso o jogo seja zerado e o jogador queira continuar, os inimigos começaram a ser bufados
luta_do_acampamento = False  # Flag para não deixar subir contador de lutas com os eventos de acampar
Boss = False  # Flag para luta de chefe
final_boss = False  # Flag para luta final

inventario = {  # Armazena itens obtidos
    "1": {"Item": "Poção", "Quantidade": 1, "Cura": 30, "Magia": 10},
    "2": {"Item": "Super Poção", "Quantidade": 0, "Cura": 50, "Magia": 22},}

itens_loja = {  # Armazena itens vendidos pela Loja
    "1": {"Item": "Poção", "Preço": 6, "Cura": 40, "Magia": 10},
    "2": {"Item": "Super Poção", "Preço": 10, "Cura": 60, "Magia": 22},}

itens_ferreiro = {  # Armazena ações vendidos pela Loja
    "1": {
        "Ação": "Afiar Espada",
        "Preço": 23,
        "Descrição": "Aumenta o Dano permanentemente em +2",
    },
    "2": {
        "Ação": "Melhorar Pedra de Magia",
        "Preço": 30,
        "Descrição": "Aumenta a magia limite permanentemente em +15 recuperando +15 também da magia atual",
    },
}

monstros = {  # Dicionário de monstros simples
    "Slime Azul": {"Vida": 20, "Ataque": 12, "Ouro": 8, "XP": 10},
    "Pequeno Orc": {"Vida": 32, "Ataque": 16, "Ouro": 15, "XP": 16},
    "Goblin": {"Vida": 48, "Ataque": 22, "Ouro": 23, "XP": 25},}

chefe = {  # Dicionário de chefes
    "Grande Orc": {"Vida": 120, "Ataque": 26, "Ouro": 60, "XP": 60},
    "Líder Goblin": {"Vida": 105, "Ataque": 30, "Ouro": 65, "XP": 65},
    "Rei Slime": {"Vida": 150, "Ataque": 19, "Ouro": 70, "XP": 70},}

Chefe_Final = {  # Dicionário do Chefe Final
    "Dragão Ancião": {"Vida": 340, "Ataque": 45, "Ouro": 250, "XP": 200}}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[H\033[J", end="")

def iniciar():  # Base de tudo, menu principal do jogo
    while True:
        limpar_tela()
        print("========== MENU PRINCIPAL ==========")
        print("1 - Ir para uma vila")
        print("2 - Adentrar a floresta")
        print("3 - Informações do Jogador")
        print("4 - Sair do jogo")

        decisao = input("\nO que fazer? ")
        if decisao == "1":
            vila()
        elif decisao == "2":
            floresta()
        elif decisao == "3":
            limpar_tela()
            mostrar_informacoes()
            input("\nPressione ENTER para voltar ao menu...")
        elif decisao == "4":
            print("Ok, até mais!")
            sys.exit()
        else:
            input("Opção inválida! Pressione ENTER...")

def vila():  # Junta lojas / ferreiro / hospedagem / acampamento
    while True:
        limpar_tela()
        print("========== VILA ==========")
        print(f"Ouro atual: {ouro}")
        print("1 - Visitar a Loja de itens")
        print("2 - Visitar o Ferreiro")
        print("3 - Procurar lugar para acampar (Cura parcial grátis - Risco de evento/Sem fuga)")
        print("4 - Ir a uma Estalagem (Cura total - Pago)")
        print("5 - Voltar ao Menu Principal")
        escolha = input("\nEscolha uma ação: ").lower()
        if escolha == "1":
            loja()
        elif escolha == "2":
            ferreiro()
        elif escolha == "3":
            acampar()
        elif escolha == "4":
            hospedagem()
        elif escolha == "5":
            return
        else:
            input("Escolha inválida! Pressione ENTER...")

def acampar(): # Acampar, opcão de descanso com 60% de chance de acontecer algo
    global vida, vidamax, magia, magiamax
    limpar_tela()
    print("========== ACAMPAMENTO ==========")
    print("Você acampa em uma planície por perto...")

    cura = vidamax * 0.30
    vida = min(vidamax, vida + cura)
    recuperarmagia = magiamax * 0.30
    magia = min(magiamax, magia + recuperarmagia)
    numero = random.randint(1, 10)
    print("Você descansa e recupera 30% das suas forças.")
    status()
    input("\nPressione ENTER para continuar...")
    if numero >= 6:
        print("Nada aconteceu durante a noite...")
    else:
        eventos = [evento_bau, evento_emboscada]
        evento_sorteado = random.choice(eventos)
        evento_sorteado()

def evento_bau(): # Uma das possibilidades de evento para acampamento
    global ouro, vida
    print("\n[EVENTO] Você encontra um baú velho enterrado perto da sua barraca!")
    escolha = input("Deseja abrir? (1 - Sim / 2 - Não): ")

    if escolha == "1":
        sorte = random.randint(1, 10)
        if sorte > 3:
            ganho = random.randint(10, 25)
            ouro += ganho
            print(f"Sucesso! Você encontrou {ganho} de ouro dentro do baú!")
        else:
            dano = random.randint(5, 10)
            vida -= dano
            print(f"Era uma armadilha de agulhas! Você tomou {dano} de dano.")
    else:
        print("Você decide não arriscar e ignora o baú.")

    input("\nPressione ENTER para continuar...")

def evento_emboscada(): # Uma das possibilidades de evento para acampamento
    global luta_do_acampamento
    print(
        "\n[EVENTO] BARULHO NAS MOITAS! Você é atacado de surpresa enquanto dormia!")
    input("Pressione ENTER para entrar em combate...")
    randomizar_inimigo()
    luta_do_acampamento = True
    combate()

def hospedagem(): # Estalagem, opcão de descanso mais segura
    global vida, vidamax, ouro, magia, magiamax
    custo = 25

    while True:
        limpar_tela()
        print("========== ESTALAGEM ==========")
        print(
            f"Diária: {custo} de ouro | Ouro atual: {ouro}\nRecupera toda a Vida e Magia.")
        print("1 - Pagar e Descansar")
        print("2 - Voltar")

        escolha = input("\nOpção: ")
        if escolha == "1":
            if ouro >= custo:
                ouro -= custo
                vida = vidamax
                magia = magiamax
                print("\nVocê teve uma excelente noite de sono! Status totalmente restaurados.")
                status()
                input("Pressione ENTER para continuar...")
                return
            else:
                input("\nOuro insuficiente! Pressione ENTER...")
        elif escolha == "2":
            return

def loja(): # Menu de itens da Loja
    global inventario, ouro
    while True:
        limpar_tela()
        print("========== LOJA DE ITENS ==========")
        for codigo, item in itens_loja.items():
            print(
                f"{codigo} - {item['Item']:<15} | Preço: {item['Preço']:<3} Ouro | Cura: {item['Cura']} HP | Magia: {item['Magia']} MP"
            )
        print("3 - Sair")
        print(f"\nOuro atual: {ouro}")

        escolha = input("\nQual item deseja comprar? ")
        if escolha == "3":
            return
        elif escolha in itens_loja:
            valor_item = itens_loja[escolha]["Preço"]
            if ouro >= valor_item:
                ouro -= valor_item
                inventario[escolha]["Quantidade"] += 1
                print(f"\nVocê comprou {itens_loja[escolha]['Item']}!")
                mostrarinventario()
                input("Pressione ENTER para continuar...")
            else:
                input("\nOuro insuficiente! Pressione ENTER...")
        else:
            input("\nOpção inválida! Pressione ENTER...")

def ferreiro(): # Menu de compra do ferreiro 
    global ouro, valor_ataque, magia, magiamax
    while True:
        limpar_tela()
        print("========== FERREIRO ==========")
        for codigo, acao in itens_ferreiro.items():
            print(
                f"{codigo} - {acao['Ação']:<25} | Preço: {acao['Preço']:<3} Ouro | {acao['Descrição']}")
        print("3 - Sair")
        print(f"\nOuro atual: {ouro}")

        escolha = input("\nO que deseja fazer? ")
        if escolha == "3":
            return
        elif escolha == "1":
            valor_item = itens_ferreiro["1"]["Preço"]
            if ouro >= valor_item:
                ouro -= valor_item
                valor_ataque += 2
                itens_ferreiro["1"]["Preço"] = int(itens_ferreiro["1"]["Preço"] * 1.15)
                print(f"\nSua espada foi afiada! Novo Ataque Básico: {valor_ataque}")
                input("Pressione ENTER para continuar...")
            else:
                input("\nOuro insuficiente! Pressione ENTER...")
        elif escolha == "2":
            valor_item = itens_ferreiro["2"]["Preço"]
            if ouro >= valor_item:
                ouro -= valor_item
                magiamax += 15
                magia += 15
                itens_ferreiro["2"]["Preço"] = int(
                    itens_ferreiro["2"]["Preço"] * 1.10)
                print(f"\nSua pedra mágica foi aprimorada! Novo MP Máximo: {magiamax}")
                input("Pressione ENTER para continuar...")
            else:
                input("\nOuro insuficiente! Pressione ENTER...")
        else:
            input("\nOpção inválida! Pressione ENTER...")

def randomizar_inimigo(): # Aleatoriza o inimigo (simples) a ser enfrentado sempre que chamada
    global nome_monstro, dados_monstro, monstros
    nome_monstro = random.choice(list(monstros.keys()))
    dados_monstro = monstros[nome_monstro].copy()

def apresentar_inimigo(): # Tela para mostrar dados do inimigo, heroi decide se quer ou não arriscar lutar
    limpar_tela()
    print("=" * 40)
    print(f"   UM INIMIGO APARECEU: {nome_monstro.upper()}!")
    print("=" * 40)
    print(f"Vida: {dados_monstro['Vida']} HP")
    print(f"Ataque: {dados_monstro['Ataque']}")
    print(f"Recompensa: ~{dados_monstro['Ouro']} Ouro | {dados_monstro['XP']} XP")
    print("=" * 40)

def floresta(): # Tela de escolha lutar/fugir além de verificar se a batalha deve ser iniciada contra boss ou chefe final
    limpar_tela()
    if lutafinal >= 5 or contarlutas >= 3:
        print("========== ALERTA ==========")
        print("A atmosfera muda... A luta contra o CHEFE vai começar!")
        while True:
            decisao = input("\nSeguir em frente?\n1 - Sim\n2 - Dar meia volta\nOpção: ")
            if decisao == "1":
                combate()
                return
            elif decisao == "2":
                print("Você decide se preparar melhor antes do confronto.")
                input("Pressione ENTER para voltar...")
                return
            else:
                print("Escolha inválida!")

    randomizar_inimigo()
    if Endgame > 0:                                         # Primeiro verifica se precisa aumentar o status do inimigo 
        aumentar_status_inimigo_plus()

    apresentar_inimigo()                                # Depois apresenta inimigo com status real
    while True:
        escolha = input("\nQual sua decisão?\n1 - Lutar\n2 - Fugir\nOpção: ").lower()
        if escolha == "1":
            combate()
            return
        elif escolha == "2":
            print("\nVocê conseguiu fugir com segurança!")
            input("Pressione ENTER para continuar...")
            return
        else:
            print("Escolha inválida!")

def usaritem(): # Função de usar item, encadeada pelo combate
    global inventario, vida, vidamax, magiamax, magia
    mostrarinventario()
    
    possui = any(item["Quantidade"] > 0 for item in inventario.values())
    if not possui:
        input("\nPressione ENTER para voltar ao combate...")
        return False

    escolha = input("\nQual Item deseja usar? (Digite o número ou 0 para cancelar): ")
    if escolha == "0":
        return False

    if escolha in inventario:
        if inventario[escolha]["Quantidade"] > 0:
            item = inventario[escolha]
            item["Quantidade"] -= 1
            vida = min(vidamax, vida + item["Cura"])
            magia = min(magiamax, magia + item["Magia"])
            print(f"\nVocê usou {item['Item']}! Recuperou HP e MP.")
            input("Pressione ENTER para continuar...")
            return True
        else:
            print("\nVocê não tem esse item!")
            input("Pressione ENTER para continuar...")
            return False
    else:
        print("\nItem não existe!")
        input("Pressione ENTER para continuar...")
        return False

def usarmagia(): # Para a Magia usei a def de usar item
    global magias_aprendidas, nome_monstro, dados_monstro, magia, magiamax, vida
    mostrarmagias()
    print(f"Seu MP atual: {magia}/{magiamax}")

    escolha = input("\nQual Magia deseja usar? (Digite o número ou 0 para cancelar): ")
    if escolha == "0":
        return False

    if escolha in magias_aprendidas:
        custo = magias_aprendidas[escolha]["Customagia"]
        dano = magias_aprendidas[escolha]["Dano"]
        if magia >= custo:
            magia -= custo
            dados_monstro["Vida"] -= dano
            print(f"\nVocê lança {magias_aprendidas[escolha]['Nome']} e causa {dano} de dano!")
            input("Pressione ENTER para continuar...")
            return True
        else:
            print("\nMP insuficiente!")
            input("Pressione ENTER para continuar...")
            return False
    else:
        print("\nMagia inválida!")
        input("Pressione ENTER para continuar...")
        return False

def combate(): # Sistema central do combate, recebe dados do inimigo, verificando quem deve ser o inimigo e realizando o processo inteiro da luta e contagem de monstros/chefes enfrentados
    global ouro, vida, inventario, nome_monstro, dados_monstro, contarlutas, xp
    global lutafinal, Endgame, final_boss, Boss, luta_do_acampamento, vidamax


    if lutafinal >= 5 and luta_do_acampamento == False:
        iniciarfinalboss()
        final_boss = True
    elif contarlutas >= 3 and luta_do_acampamento == False:
        aleatorizarboss()
        Boss = True


    while True:
        limpar_tela()

        if vida <= 0:
            print(f"\nO monstro te derrotou, {heroi}...\n========== GAME OVER ==========")
            sys.exit()

        if dados_monstro["Vida"] <= 0:
            print("=" * 40)
            print(f"INIMIGO DERROTADO! Parabéns!")
            print(f"+{dados_monstro['Ouro']} Ouro | +{dados_monstro['XP']} XP")
            print("=" * 40)

            ouro += dados_monstro["Ouro"]
            xp += dados_monstro["XP"]
            subir_nivel()

            if Boss:
                contarlutas = 0
                lutafinal += 1
                Boss = False
                if lutafinal >= 5:
                    print("\nALERTA! O selo do Chefe Final foi quebrado! Esteja preparado...")
            elif not luta_do_acampamento:
                contarlutas += 1
                if contarlutas >= 3:
                    print(f"\nAtenção {heroi}! Um monstro forte te percebeu. A próxima batalha será contra um CHEFE!")
            else:
                luta_do_acampamento = False

            input("\nPressione ENTER para continuar...")

            if final_boss:
                limpar_tela()
                print("=" * 40)
                print("PARABÉNS! Você derrotou o Dragão Ancião e salvou o reino!")
                print("=" * 40)
                print("1 - Continuar jogando (Modo New Game+ com inimigos mais fortes)")
                print("2 - Encerrar o jogo")
                
                while True:
                    escolha = input("Opção: ")
                    if escolha == "1":
                        Endgame += 1
                        contarlutas = 0
                        lutafinal = 0
                        final_boss = False
                        print(f"\nDificuldade aumentada! Nível de NewGame+: {Endgame}")
                        input("Pressione ENTER para continuar a jornada...")
                        break
                    elif escolha == "2":
                        print("Obrigado por jogar RPG Overworld!")
                        sys.exit()
                    else:
                        print("Escolha inválida!")
            return

        # Interface do Turno do Jogador
        print(f"Heroi: {heroi} | Nível: {nivelheroi}")
        print(f"HP: {int(vida)}/{vidamax} | MP: {int(magia)}/{magiamax} | Dano Base: {valor_ataque}")
        print("-" * 35)
        print(f"Inimigo: {nome_monstro}")
        print(f"HP Inimigo: {dados_monstro['Vida']} | Ataque: {dados_monstro['Ataque']}")
        print("-" * 35)
        print("1 - Atacar com Espada")
        print("2 - Lançar Magia")
        print("3 - Usar Item")

        luta = input("\nO que deseja fazer? ").lower()
        turno_valido = False

        if luta == "1":
            print(f"\nVocê ataca o {nome_monstro} causando {valor_ataque} de dano!")
            dados_monstro["Vida"] -= valor_ataque
            turno_valido = True
            input("Pressione ENTER para continuar...")
        elif luta == "2":
            turno_valido = usarmagia()
        elif luta == "3":
            usaritem()   # Não gasta turno, pode usar item a vontade
        else:
            input("\nOpção inválida! Pressione ENTER...")

        # Turno do Inimigo (Só ataca se o jogador tiver feito uma ação válida e o monstro ainda estiver vivo)
        if turno_valido and dados_monstro["Vida"] > 0:
            print(f"\nO {nome_monstro} contra-ataca e causa {dados_monstro['Ataque']} de dano!")
            vida -= dados_monstro["Ataque"]
            input("Pressione ENTER para prosseguir...")

def aumentar_status_inimigo_plus(): # Aumenta o status inimigo baseado no nivel do heroi, e bonus de end game = Nivelheroi → força base dos inimigos / Endgame → dificuldade adicional
    global dados_monstro, nivelheroi, Endgame
    aumento_total = (0.05 * nivelheroi) + (0.10 * Endgame)
    dados_monstro["Vida"] = int(dados_monstro["Vida"] * (1 + aumento_total))
    dados_monstro["Ataque"] = int(dados_monstro["Ataque"] * (1 + aumento_total))
    dados_monstro["Ouro"] = int(dados_monstro["Ouro"] * (1 + 0.03 * nivelheroi))
    dados_monstro["XP"] = int(dados_monstro["XP"] * (1 + 0.05 * nivelheroi))

def subir_nivel(): # Verfica se você subiu de nivel
    global xp, xp_prox_nv, vida, valor_ataque, magia, vidamax, nivelheroi, magias_aprendidas, magiamax
    if xp >= xp_prox_nv:
        print("\n*** PARABÉNS! VOCÊ SUBIU DE NÍVEL! ***")
        nivelheroi += 1
        xp -= xp_prox_nv
        xp_prox_nv = int(xp_prox_nv * 1.30)
        vidamax = int(vidamax * 1.15)
        magiamax = int(magiamax * 1.15)
        valor_ataque += 3

        for chave in magias_aprendidas:
            magias_aprendidas[chave]["Dano"] += 6
            magias_aprendidas[chave]["Customagia"] += 4

        status()

def aleatorizarboss():  # Aleatoriza os bosses e substitui o inimigo simples
    global nome_monstro, dados_monstro, chefe
    nome_monstro = random.choice(list(chefe.keys()))
    dados_monstro = chefe[nome_monstro].copy()

def iniciarfinalboss(): # Substitui o boss pelo boss final
    global Chefe_Final, dados_monstro, nome_monstro
    print("\nVocê vê a sombra de asas gigantescas caindo sobre você...")
    nome_monstro = "Dragão Ancião"
    dados_monstro = Chefe_Final[nome_monstro].copy()

def mostrarinventario(): # Mostra a tela inventário
    print("========== INVENTÁRIO ==========")
    possui_item = False
    for codigo, item in inventario.items():
        if item["Quantidade"] > 0:
            print(
                f"{codigo} - {item['Item']:<15} x{item['Quantidade']} (Cura: {item['Cura']} HP | {item['Magia']} MP)"
            )
            possui_item = True
    if not possui_item:
        print("Seu inventário está vazio.")
    print("================================")

def mostrarmagias(): #Mostra a tela de magias
    print("========== MAGIAS ==========")
    if magias_aprendidas:
        for codigo, magia_dict in magias_aprendidas.items():
            print(
                f"{codigo} - {magia_dict['Nome']:<25} | Dano: {magia_dict['Dano']:<3} | Custo: {magia_dict['Customagia']} MP"
            )
    else:
        print("Você ainda não aprendeu nenhuma magia.")   # Futuramente na v2 terá uso
    print("============================")

def status(): #Mostra de status do jogador
    print("\n===== STATUS DO JOGADOR =====")
    print(f"Nome: {heroi} | Nível: {nivelheroi}")
    print(f"Vida: {int(vida)}/{vidamax} | Magia: {int(magia)}/{magiamax}")
    print(f"Ataque: {valor_ataque} | Ouro: {ouro}")
    print(f"XP: {xp}/{int(xp_prox_nv)}")
    print("=============================")

def mostrar_informacoes(): # Mostra todas as informações do heroi
    status()
    mostrarmagias()
    mostrarinventario()

# --- INÍCIO DO JOGO ---
limpar_tela()
heroi = input("Bem-vindo ao Overworld RPG!\nDigite o nome do seu personagem: ")
print(f"Olá {heroi}!")
print("As regras são simples:")
print("- Digite o número correspondente à ação desejada.")
print("- A cada 3 lutas na floresta, um CHEFE aparecerá.")
print("- Derrote 5 Chefes para acordar o Boss Final!\n")

mostrar_informacoes()

Escolha = input("\nDeseja prosseguir?\n1 - Sim\n2 - Não\nOpção: ")
if Escolha == "1":
    iniciar()
else:
    print("Jogo Encerrado.")
    sys.exit()

# Resolvido Bug dos bosses e final boss aparecer no acampamento
# Ferreiro afiar espada balanceado, ficava muito quebrado o dano basico
# magia balanceada, dá mais dano, magia custo aumenta conforme nivel sobe tbm
# Acampar aumentado em 10% chance de evento e cura apenas 30% era 40%
# Inicia com uma poção para ajudar