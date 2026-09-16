from loja import menuloja
from util import limpar_tela

class Vilas:
    def __init__(self, nome, descricao, nivelminimo):
        self.nome = nome
        self.descricao = descricao
        self.nivelminimo = nivelminimo
        # itens ou eventos
        self.eventos = []

    def entrarvila(self, heroi):
        if heroi.nivel < self.nivelminimo:
            print(f"\n[!] A estrada para {self.nome} é perigosa demais! Requer Nível {self.nivel_minimo}.")
            

def vilamenu(heroi):

    while True:
        limpar_tela()

        print(f"========== VILA DE OAKVALE ==========")
        print(f"Heroi: {heroi.nome} | Ouro: {heroi.ouro}")
        print("-------------------------------------")
        print("1 - Loja de Itens")
        print("2 - Ferreiro")
        print("3 - Estalagem (Restaurar HP/MP)")    # Custo/Efeito: Custa Ouro, mas recupera $100\%$ da Vida/Mana e cura todas as condições negativas (veneno, sangramento).
        print("4 - Guilda de Aventureiros (Quests)")
        print("5 - Campo de Treinamento (Aprender Habilidades)")
        print("6 - Ver Status / Inventário")
        print("0 - Sair da Vila (Ir para a Floresta)")

        escolha = input("\nOnde deseja ir? ")

        if escolha == "1":
            menuloja(heroi)
        elif escolha == "2":
            ferreiro(heroi)
        elif escolha == "3":
            estalagem(heroi)
        elif escolha == "0":
            print("\nSaindo da vila em direção à aventura...")
            break
            
# vila_inicial = Vila("Vila de Oakvale", "Uma vila pacífica no bosque", nivel_minimo=1) # 

# vila_pescadores = Vila("Porto da Névoa", "Vila de pescadores à beira do lago", nivel_minimo=3) # ma vila pacífica na beira da água, cercada por névoa e monstros aquáticos/anfíbios.
    #Evento Exclusivo - Pescando Recompensas:
    # O jogador pode pagar uma pequena quantia para pescar. Ele pode pegar Peixes (recuperam vida/mana em combate) ou tesouros antigos (ouro, chaves, itens raros).
    # Itens Únicos:
    # Poção de Fôlego: Aumenta a chance de esquiva nas próximas 3 lutas.
    # Tridente / Rede de Pesca: Arma com chance de causar atordoamento (Stun).  

# cidade_anoes = Vila("Forjafria", "Fortaleza mineradora nas montanhas", nivel_minimo=6)
    #Tema: Uma cidade encravada na rocha, fria, com grandes forjas e tavernas barulhentas.
    # Evento Exclusivo - Encantamento / Mini-game na Forja:
    # O Ferreiro Anão pode aplicar atributos extras permanentes nas armas do herói em troca de Ouro e Minérios achados na floresta/caverna (Ataque +5 ou Dano de Fogo).
    # Itens Únicos:
    # Cerveja Fortificada: Aumenta muito o ataque, mas reduz a precisão/defesa.
    # Armadura de Aço Negro: Altíssima defesa, ideal para se preparar para o Boss Final.


# mapa_mundo = [vila_inicial, vila_pescadores, cidade_anoes]


#   Campo de Treinamento Aprender habilidades que usam Foco de batalha.
#   chance de chegar na vila e a Feira Noturna poder estar diponivel
#   limitar opção acampamento para 1 vez somente depois de cada batalha / ou então deixar com muito maior chance de eventos


def estalagem():
    while True:
        escolha = input("Ao chegar na estalagem...")

def ferreiro():
    print
    