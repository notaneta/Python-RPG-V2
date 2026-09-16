from util import limpar_tela
from itens import poçoes, ferreiro_Amuletos_Ataque, ferreiro_Amuletos_Defesa
from magias import listamagias
from magias import magias
from eventos import evento_vila_inical, evento_festival_da_neve, evento_pesca_vila, evento_raid_vila_destruida

item_raid_vila = False

class Vilas:
    def __init__(self, nome, descricao, bossnecessario, proximavila, eventos=[]):
        self.nome = nome
        self.descricao = descricao
        self.bossnecessario = bossnecessario
        self.proximavila = proximavila
        # itens ou eventos
        self.eventos = eventos

    def vilamenu(self, heroi):

        while True:
            limpar_tela()

            print(f"========== {Vila_atual.nome.upper()} ==========")
            print(f"Heroi: {heroi.nome} | Ouro: {heroi.ouro}")
            print("-------------------------------------")
            print("1 - Visitar Loja de Itens")
            print("2 - Visitar Ferreiro")
            print("3 - Procurar Estalagem (Restaurar HP/MP)")    # Custo/Efeito: Custa Ouro, mas recupera $100\%$ da Vida/Mana e cura todas as condições negativas (veneno, sangramento).           
            print("4 - Verificar Status / Inventário")
            print("5 - Iniciar Evento Exclusivo por Vila")
            print("0 - Sair da Vila (Explorar)")

            escolha = input("\nQual sua decisão?\n")

            if escolha == "1":
                menuloja(heroi)
            elif escolha == "2":
                ferreiro(heroi)
            elif escolha == "3":
                estalagem(heroi)
            elif escolha == "4":
                while True:
                    escolha2 = input("\n1 - Status Heroi\n2 - Inventário poções\n3 - Magias Aprendidas\n4 - Habilidades Aprendidas\n 0 - Voltar")
                    if escolha2 == "1":
                        heroi.mostrar_status()
                        input("Pressione ENTER para continuar...")
                        return

                    elif escolha2 == "2":
                        heroi.mostrar_inventario_pocoes()
                        input("Pressione ENTER para continuar...")
                        return

                    elif escolha2 == "3":
                        heroi.mostrarmagias()
                        input("Pressione ENTER para continuar...")
                        return

                    elif escolha2 == "4":
                        heroi.mostrarSkill()
                        input("Pressione ENTER para continuar...")
                        return

                    elif escolha2 == "0":
                        return

            elif escolha == "5":
                Vila_atual.eventos[0](heroi)
                input("Pressione ENTER para continuar...")
                return

            elif escolha == "0":
                print("\nSaindo da vila em direção à aventura...")
                break
            
# Vilas
vila4_destruida = Vilas("Aldeia Destruida", "Aldeia que foi destruida", bossnecessario=4 , proximavila=1, eventos = [evento_raid_vila_destruida])   # Tem um evento de raid de bosses caso o jogador passe, ele ganha um drop lendário
vila3_gelada = Vilas("Vila da Neve", "Uma humilde vila conhecida por usa temperatura gelada", bossnecessario=3, proximavila=vila4_destruida, eventos = [evento_festival_da_neve])
vila2_pescadores = Vilas("Porto Azul", "Vila de pescadores à beira do lago", bossnecessario=2, proximavila=vila3_gelada, eventos = [evento_pesca_vila])
vila_inicial = Vilas("Vila do vale verde", "Uma vila pacífica no bosque", bossnecessario=1, proximavila=vila2_pescadores, eventos = [evento_vila_inical])
Vila_atual = vila_inicial

# vila2_pescadores uma vila pacífica na beira da água, cercada por névoa e monstros aquáticos/anfíbios.
    #Tema: Uma vila a beira de um grande lago azulado e brilhante. 
    #Evento Exclusivo - Pescando Recompensas:
    # O jogador pode pagar uma pequena quantia para pescar. Ele pode pegar Peixes (recuperam vida/mana em combate) ou tesouros antigos (ouro, chaves, itens raros).
    # Itens Únicos:
    # Poção de Fôlego: Aumenta a chance de esquiva nas próximas 3 lutas.
    # Tridente / Rede de Pesca: Arma com chance de causar atordoamento (Stun).  

# cidade_anoes = Vila("Forjafria", "Fortaleza dos Anões", nivel_minimo=6)
    #Tema: Uma cidade encravada na rocha, fria, com grandes forjas e tavernas barulhentas.
    # Evento Exclusivo - Encantamento / Mini-game na Forja:
    # O Ferreiro Anão pode aplicar atributos extras permanentes nas armas do herói em troca de Ouro e Minérios achados na floresta/caverna (Ataque +5 ou Dano de Fogo).
    # Itens Únicos:
    # Cerveja Fortificada: Aumenta muito o ataque, mas reduz a precisão/defesa.
    # Armadura de Aço Negro: Altíssima defesa, ideal para se preparar para o Boss Final.

#   Campo de Treinamento Aprender habilidades que usam Foco de batalha.
#   chance de chegar na vila e a Feira Noturna poder estar diponivel
#   limitar opção acampamento para 1 vez somente depois de cada batalha / ou então deixar com muito maior chance de eventos

def menuloja(heroi):

    while True:
        limpar_tela()

        print(f"Heroi: {heroi.nome} | Ouro: {heroi.ouro}")
        print("============ LOJA DO MAGO ============")
        print("Você pode comprar poções ou verificar sua aptidão com magias")
        escolha = input("Qual sua decisão?\n1 - Comprar Poções\n2 - Verificar Aptidão com Magias\n0 - Sair da loja\n")
        if  escolha == "1":
            while True:
                print("============ LOJA DO MAGO ============")
                print("========== LISTA DE POÇÕES ==========")
                for Pocao in poçoes:
                    print("-" * 20)
                    Pocao.mostraritens()
                    print("-" * 20)

                escolha = input("Digite o N(ID) do item que deseja obter ou 0 para fechar a loja\n")
                for item in poçoes:
                    if item.id == escolha:
                        if heroi.ouro >= item.custo:        
                            nomeitem = item
                            heroi.adicionar_pocoes(nomeitem)
                            heroi.ouro -= item.custo
                            print(f"Seu novo ouro é {heroi.ouro}")        
                            input("Pressione ENTER para continuar...")
                            limpar_tela()

                        else:
                            print("Você não tem ouro suficiente...")
                            input("Pressione ENTER para continuar...")
                            
                    elif escolha == "0":
                        print("Você saiu da loja...")
                        input("Pressione ENTER para continuar...")
                        return
                    
        elif escolha == "2":
            print("O mago lê sua aptidão com magias...")
            for magia in listamagias:
                print(f"{magia.nome.upper()}")
                magia.mostrarmagias()

            input("Pressione ENTER para continuar...")

        elif escolha == "0":
            print("Você saiu da loja...")
            input("Pressione ENTER para continuar...")            
            return

def estalagem(heroi):
    while True:
        custo = 25
        while True:
            escolha = input(f"Ao chegar na estalagem, você tem a opção de:\n1 - Pagar {custo} para descansar(Curar tudo)\n0 - Sair\n")
            if escolha == "1":
                heroi.vida = heroi.max
                print("Você descansou na estalagem e se curou totalmente!")

            elif escolha == "0":
                return
            

def ferreiro(heroi):    # Testar depois se consigo criar IF para verificar em qual a vila que estou, e dependendo dela, aparece alguma opção ou item adicional / OPÇÃO CHAMADA item exclusivo da vila / verifica antes a vila atual e muda o catalogo referente a ela
    global item_raid_vila
    
    if item_raid_vila == True:
        print("============ FERREIRO ============")
        print("Você mostra o material da RAID ao ferreiro, ele faz uma nova ESPADA")
        print(f"Você equipou a ESPADA SUPREMA")
        heroi.ataque += 100
        input("Pressione ENTER para continuar...")

    while True:

        limpar_tela()
        print(f"Heroi: {heroi.nome} | Ouro: {heroi.ouro}")
        print("============ FERREIRO ============")
        print("Você pode comprar novas ESPADAS e novas ARMADURAS")
        escolha = input("Qual sua decisão?\n1 - Comprar Espadas\n2 - Comprar Armaduras\n0 - Sair do Ferreiro\n")
        if escolha == "1":
            for id, item in enumerate(ferreiro_Amuletos_Ataque): # TESTE DE NUMERAR usando o comando (ENUMERATE) e er como fazer escolha com ele, caso der certo, poderei remover o ID dos itens na lista e na classe
                print("-" * 20)
                print(f"ID: {id+1}")
                item.mostrar_item()
                print("-" * 20)

            escolha2 = input("Digite o ID do item que deseja comprar ou '0' para sair\n")
            if escolha2 == "0":
                return
            
            if not escolha2.isdigit():
                print("Digite apenas números!")
                continue

            indice = int(escolha2) - 1
            if 0 <= indice < len(ferreiro_Amuletos_Ataque):
                item_escolhido = ferreiro_Amuletos_Ataque[indice]
                if item_escolhido.custo <= heroi.ouro:
                    item_escolhido.comprar_espada(heroi)
                    item_escolhido.equipar_espada(heroi)
                    print(f"Seu novo ataque é {heroi.ataque}")
                    ferreiro_Amuletos_Ataque.remove(item_escolhido)   # Remove item da lista
                    input("Pressione ENTER para continuar...")
                    limpar_tela()

                else:
                    print("Você não tem dinheiro suficiente...")
                    input("Pressione ENTER para continuar...")
            else:
                print("Item não existente...")
                input("Pressione ENTER para continuar...")

        elif escolha == "2":
            for id, item in enumerate(ferreiro_Amuletos_Defesa): 
                print(f"ID: {id+1}")
                item.mostrar_item()

            escolha2 = input("Digite o ID do item que deseja comprar ou '0' para sair\n")
            if escolha2 == "0":
                return
            
            if not escolha2.isdigit():
                print("Digite apenas números!")
                continue

            indice = int(escolha2) - 1
            if 0 <= indice < len(ferreiro_Amuletos_Defesa):
                item_escolhido = ferreiro_Amuletos_Defesa[indice]
                if item_escolhido.custo <= heroi.ouro:
                    item_escolhido.comprar_armadura(heroi)
                    item_escolhido.equipar_armadura(heroi)
                    print(f"Sua nova defesa é {heroi.defesa}")
                    ferreiro_Amuletos_Defesa.remove(item_escolhido)   # Remove item da lista
                    input("Pressione ENTER para continuar...")
                    limpar_tela()

                else:
                    print("Você não tem dinheiro suficiente...")
                    input("Pressione ENTER para continuar...")
            else:
                print("Item não existente...")
                input("Pressione ENTER para continuar...")

        elif escolha == "0":
            return

        else:
            print("Comando não existente")
                
            