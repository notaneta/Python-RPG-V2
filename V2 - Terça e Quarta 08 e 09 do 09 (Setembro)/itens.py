# Poção de Cura
class Pocao:
    def __init__(self, id, nome, cura, custo, quantidade, descricao):
        self.id = id
        self.nome = nome
        self.cura = cura
        self.custo = custo
        self.quantidade = quantidade
        self.descricao = descricao

    def mostraritens(self):
        print(f"Item: {self.nome} N* {self.id}")
        print(f"Cura: {self.cura}")
        print(f"Custo: {self.custo}")
        print(f"Descrição: {self.descricao}")

poçoes = [
    Pocao("1", "Poção Pequena", 20, 15, 1, "Cura uma pequena parte da vida"),
    Pocao("2","Poção Média", 45, 30, 1, "Cura media da sua vida"),
    Pocao("3", "Poção Grande", 75, 50, 1, "Cura grande parte da sua vida"),
]

def usaritem(heroi):
    print("Qual item do seu inventário usar?")
    heroi.mostrar_inventario_pocoes()
    escolha = input("Digite o número do item que deseja usar ou digite 0 para sair...")
    for item in heroi.inventario:
        if escolha == item.id:
            escolha = item
            heroi.removeritem(escolha)
            heroi.vida = min(heroi.vidamax, heroi.vida + item.cura)
            print(f"O item {item.nome} foi usado e curou {item.cura} da sua vida")

class Espadas:
    def __init__(self, nome, descricao, dano, custo):
        self.nome = nome
        self.descricao = descricao
        self.dano = dano
        self.custo = custo

    def mostrar_item(self):
        print(f"Item: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Dano: {self.dano}")
        print(f"Preço: {self.custo}")

    def comprar_espada(self, heroi):
        heroi.ouro -= self.custo

    def equipar_espada(self, heroi):
        heroi.ataque += self.dano


ferreiro_espadas = [ # nome, descricao, dano, custo):           # Será usado para prox versão, onde terá menu de equipamento  
    Espadas("Espada de Ferro", "Espada Básica de Ferro, aumenta em +6 o ataque", 6, 40),
    Espadas("Espada de Aço", "Espada de Aço", 8, 40),
    Espadas("Espada Reforçada", "Espada Reforçada", 12, 40),
    Espadas("Espada do Cavaleiro", "Espada do Cavaleiro", 12, 40),    
]

class Armadura:
    def __init__(self, nome, descricao, defesa, custo):
        self.nome = nome
        self.descricao = descricao
        self.defesa = defesa
        self.custo = custo

    def mostrar_item(self):
        print(f"Item: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Defesa: {self.defesa}")
        print(f"Preço: {self.custo}")

    def comprar_armadura(self, heroi):
        heroi.ouro -= self.custo

    def equipar_armadura(self, heroi):
        heroi.defesa += self.defesa

ferreiro_armaduras = [ # nome, descricao, defesa, custo):
    Armadura("Armadura de aventureiro", "Armadura Básica, aumenta em +5 a defesa", 5, 40),
    Armadura("Armadura de Ferro", "Armadura de Ferro", 12, 40),
    Armadura("Armadura Reforçada", "Armadura Reforçada", 12, 40),
    Armadura("Armadura do Cavaleiro", "Armadura do Cavaleiro", 12, 40),    
]

class Amuletos_Ataque(Espadas):
    def __init__(self, nome, descricao, dano, custo):
        super().__init__(nome, descricao, dano, custo)

# ==========================================
# AMULETOS DE ATAQUE (BÔNUS DE DANO)
# ==========================================

ferreiro_Amuletos_Ataque = [
    # Nome, Descrição, Bônus de Ataque, Custo em Ouro
    # --- Bioma 1: Floresta ---
    Amuletos_Ataque(
        "Amuleto do Garra",
        "Pequeno talismã com dentes de fera que afia seus golpes.",
        4,
        25,
    ),
    Amuletos_Ataque(
        "Amuleto da Força",
        "Esculpido em pedra rúnica, canaliza poder físico ao usuário.",
        8,
        45,
    ),
    # --- Bioma 2: Caverna ---
    Amuletos_Ataque(
        "Amuleto do Guerreiro",
        "Carrega a fúria de antigos combatentes das profundezas.",
        14,
        75,
    ),
    Amuletos_Ataque(
        "Amuleto do Predador",
        "Aumenta a precisão e a força de impacto em cada ataque.",
        20,
        120,
    ),
    # --- Bioma 3: Montanhas Geladas ---
    Amuletos_Ataque(
        "Amuleto do Titã",
        "Relíquia lendária que concede força devastadora e inigualável.",
        28,
        180,
    ),
]

# ==========================================
# AMULETOS DE DEFESA (BÔNUS DE PROTEÇÃO)
# ==========================================
class Amuletos_Defesa(Armadura):
    def __init__(self, nome, descricao, defesa, custo):
        super().__init__(nome, descricao, defesa, custo)

ferreiro_Amuletos_Defesa = [
    # Nome, Descrição, Bônus de Defesa, Custo em Ouro
    # --- Bioma 1: Floresta ---
    Amuletos_Defesa(
        "Amuleto da Proteção",
        "Encantamento simples que repele pequenos impactos.",
        3,
        20,
    ),
    Amuletos_Defesa(
        "Amuleto da Casca",
        "Feito com madeira sagrada enrijecida contra impactos.",
        5,
        40,
    ),
    # --- Bioma 2: Caverna ---
    Amuletos_Defesa(
        "Amuleto do Bastião",
        "Cria uma barreira sutil que reduz o dano de acertos diretos.",
        9,
        70,
    ),
    Amuletos_Defesa(
        "Amuleto do Guardião",
        "Forjado com rocha subterrânea, fortifica o corpo do herói.",
        14,
        110,
    ),
    # --- Bioma 3: Montanhas Geladas ---
    Amuletos_Defesa(
        "Amuleto Inabalável",
        "Relíquia congelada que absorve os golpes mais violentos.",
        20,
        160,
    ),
]



