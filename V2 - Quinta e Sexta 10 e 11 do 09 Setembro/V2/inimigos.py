import random
from lore import dialogo
texto_lobo = True

class Monstro:

    def __init__(self, nome, vida, ataque, ouro, xp):

        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.ouro = ouro
        self.xp = xp

    def mostrar_status(self):
        print(f"============ INIMIGO ============")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}/{self.vidamax}")
        print(f"Ataque: {self.ataque}")

    def atacar(self, heroi):            # Foco do heroi dento do ataque do inimigo para poder garantir que seja gerado caso atacar 2 vezes
            ataquefinal = max(1, self.ataque - heroi.defesa)
            heroi.vida -= ataquefinal
            print(f"\nO {self.nome} te ataca causando {ataquefinal} de dano")
            heroi.foco = min(100, heroi.foco + (random.randint(10, 14) + heroi.focogen * 1.02))
            input("\nPressione ENTER para continuar...")
        
class Inimigo(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herdou os parametros de monstro
        self.defesa = 0
        self.defesa_magica = 0
        self.habilidade = None

    def usar_habilidade(self, heroi):
        pass

class Boss(Monstro):        # EXCLUSIVO DOS BOSSES POR HORA , defesa magica e defesa(ataque)
    def __init__(self, nome, vida, ataque, ouro, xp, habilidade, defesa, defesa_magica) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herdou os parametros de personagem
        self.habilidade = habilidade
        self.defesa = defesa
        self.defesa_magica = defesa_magica
        self.habilidade_usada = False

    def mostrar_status(self):
        print("============ INIMIGO ============")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}/{self.vidamax}")
        print(f"Ataque: {self.ataque}")

    def atacar(self, heroi):
            ataquefinal = max(1, self.ataque - heroi.defesa)            # Foco do heroi dento do ataque do inimigo para poder garantir que seja gerado caso atacar 2 vezes
            heroi.vida -= ataquefinal
            print(f"\nO {self.nome} te ataca causando {ataquefinal} de dano")
            heroi.foco = min(100, heroi.foco + (random.randint(10, 14) + heroi.focogen * 1.02))
            input("\nPressione ENTER para continuar...")
    
    def usar_habilidade(self, heroi):
        if self.habilidade_usada == False:
            self.habilidade(heroi,self)

def slime_absorção(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.50:
        cura = random.randint(99, 110)
        boss.vida = min(boss.vidamax, boss.vida + cura)
        print("O Rei Slime absorver a massa que de outros slimes ao redor e se cura!")
        print(f"Rei Slime recuperou {cura}")
        input("\nPressione ENTER para continuar...")
        boss.habilidade_usada = True

def frenesi_lobo(heroi, boss):
    global texto_lobo
    if texto_lobo == True:
        texto_lobo = False
        print(f"O {boss.nome} entrou em frenesi, e vai atacar 2 vezes por turno agora!")
        input("\nPressione ENTER para continuar...")
    if boss.vida <= boss.vidamax * 0.50:
        print(f"O {boss.nome} te atacou mais uma vez")
        boss.atacar(heroi)

def golem_defesa(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.40:
        print("O Golem se tornou ivulnerável a magias")
        boss.defesa_magica += 500
        input("\nPressione ENTER para continuar...")
        boss.habilidade_usada = True
     
def furia_dragão(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.40: # Vida abaixo de 40%
        print("O Dragão de gelo entrou em Fúria!")
        boss.ataque = int(boss.ataque * 1.50)
        print(f"Ataque aumentou para {boss.ataque}")
        boss.habilidade_usada = True
        input("\nPressione ENTER para continuar...")

def casulo_sombrio(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.50: # Vida abaixo de 50%
        print(f"A {boss.nome} se envolveu em uma teia gigante.\nSua defesa aumentou em +15")
        boss.defesa += 15
        boss.habilidade_usada = True

def veneno_ancestral(heroi, boss):  # Teste de veneno 
    teste = random.randint(1, 10)

    if teste >= 5 and heroi.turnos_veneno == 0:
        heroi.turnos_veneno = 3
        print(f"{heroi.nome} foi envenenado por 3 turnos!")
        input("\nPressione ENTER para continuar...\n")
        veneno = True

    else:
        if heroi.turnos_veneno == 0:
            print("Você desviou do veneno da Aranha")

    if veneno == True:
        dano = random.randint(6, 14)
        heroi.vida -= dano
        print(f"{heroi.nome} recebeu {dano} do veneno...")
        input("\nPressione ENTER para continuar...\n")
        heroi.turnos_veneno -= 1
        print(f"Turnos restante até acabar veneno {heroi.turnos_veneno}")
        input("\nPressione ENTER para continuar...\n")

def tempestade_Glacial(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.30:
        print("Ymir usou TEMPESTADE GLACIAL.")
        print("Ymir congela o campo de batalha.")
        input("\nPressione ENTER para continuar...\n")
        print("Ele irá te congelar de 3 em 3 turnos, causando dano e te deixando paralisado por 1 turno...")
        input("\nPressione ENTER para continuar...\n")
        heroi.contador_gelo = 3
        boss.habilidade_usada = True

    if heroi.turnos_dano_gelo == 0:  # So stuna e causa dano no 3* turno
        dano = random.randint(10, 24)
        heroi.vida -= dano
        heroi.turnos_stun = 1
        heroi.contador_gelo  = 3
        acabou_de_ativar = True

        print(f"{heroi.nome} recebeu {dano} devido ao frio...")

    if heroi.turnos_dano_gelo > 0 and acabou_de_ativar == False:      # Abaixo de 3* turnos, sem stun e sem dano
        heroi.turnos_stun = 0
        heroi.contador_gelo  -= 1

    acabou_de_ativar = False

def eco_dos_mortos(heroi, boss):    # Termnar habilidade boss
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.50:
        dialogo("Rei do Caos: Interessante...\nHá séculos ninguém era capaz de me ferir.")
        input("Pressione ENTER para continuar...")
        dialogo("Rei do Caos: Mas isso não muda nada! O mundo continuará apodrecendo!")
        print("Os espíritos invocados irão te atacar de 3 em 3 turnos causando dano adicional de 10% do dano recebido e paralisado por 1 turno.")
        input("Pressione ENTER para continuar...")
        heroi.contador_gelo = 3
        boss.habilidade_usada = True


    if heroi.turnos_dano_gelo == 0:
        print("Os espiritos invocados atacam!")
        dano = boss.ataque * 0.10
        heroi.vida -= dano
        heroi.turnos_stun += 1
        print(f"Você recebeu {dano} de dano dos espiritos e ficou paralisado")
        acabou_de_ativar = True
        
    if heroi.turnos_dano_gelo > 0 and acabou_de_ativar == False:      # Abaixo de 3* turnos, sem stun e sem dano
        heroi.turnos_stun = 0
        heroi.contador_gelo  -= 1

    acabou_de_ativar = False

def ultima_resistencia(heroi, boss): 
    print("Rei do Caos: Não!\nEu me recuso a desaparecer!\nSe o mundo deseja o caos...\nEntão eu me tornarei o próprio caos!")
    print("Rei do Caos usou ULTIMA RESISTENCIA.")
    input("\nPressione ENTER para continuar...\n")
    "Recebe uma cura de emergência de 20% do HP total e dobra seu ataque"

def copia_magias(heroi, boss):
    
    magia = random.randint(1,10)
    if magia >= 7:  # Chance de 40 % de não usar magia
        print(f"{boss.nome} teve sua mana recuperada.")
        input("Pressione ENTER para continuar...")
        return

    if magia >= 5:
        print(f"{boss.nome} usou magia BOLA DE FOGO")
        input("Pressione ENTER para continuar...")
        heroi.vida -= 75
        print("Você recebeu 75 de dano!")
        input("Pressione ENTER para continuar...")

        return

    elif magia >= 3:
        print(f"{boss.nome} usou magia RELAMPAGO ARCANO")
        input("Pressione ENTER para continuar...")
        heroi.vida -= 115
        print("Você recebeu 115 de dano!")
        input("Pressione ENTER para continuar...")

        return

    elif magia >= 1:
        print(f"{boss.nome} usou magia COMETA SOMBRIO")
        input("Pressione ENTER para continuar...")
        heroi.vida -= 160
        print("Você recebeu 160 de dano!")
        input("Pressione ENTER para continuar...")

        return
    
def execuçao_sombria(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.65:
        print(f"[ALERTA] {boss.nome} está carregando sua fúria!")

    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.55:
        print(f"[ALERTA] {boss.nome} está quase com sua fúria completa!")
        print("[ALERTA] Um golpe muito forte está para vir!")

    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.45:
        print(f"{boss.nome} usou Habilidade EXECUÇÃO SOMBRIA")
        input("Pressione ENTER para continuar...")
        dano = max(1, heroi.defesa - 225) 
        heroi.vida -= dano
        print("Você recebeu 225 de dano!")
        input("Pressione ENTER para continuar...")
        boss.habilidade_usada = True
  
inimigos_floresta = [
    # Nome | Vida | Ataque | Ouro | XP
    Inimigo(
        "Goblin",
        random.randint(65, 85),
        random.randint(14, 20),
        random.randint(8, 14),
        random.randint(15, 20),
    ),
    Inimigo(
        "Slime",
        random.randint(90, 115),
        random.randint(10, 15),
        random.randint(6, 12),
        random.randint(12, 16),
    ),
    Inimigo(
        "Aranha Gigante",
        random.randint(75, 95),
        random.randint(16, 22),
        random.randint(10, 16),
        random.randint(18, 22),
    ),
    Inimigo(
        "Urso Ancião",
        random.randint(130, 160),
        random.randint(22, 28),
        random.randint(15, 22),
        random.randint(25, 30),
    ),
    Inimigo(
        "Lobo Selvagem",
        random.randint(70, 88),
        random.randint(18, 24),
        random.randint(8, 14),
        random.randint(15, 20),
    ),
]

boss_floresta = [
    # Nome | Vida | Ataque | Ouro | XP | Habilidade | Def.Mágica | Defesa Física
    Boss(
        "Rei Slime",
        random.randint(220, 240),
        random.randint(25, 32),
        random.randint(40, 60),
        random.randint(80, 100),
        slime_absorção,
        defesa_magica=0,
        defesa=0,
    ),
    Boss(
        "Lobo Superior",
        random.randint(300, 330),
        random.randint(32, 40),
        random.randint(50, 75),
        random.randint(110, 130),
        frenesi_lobo,
        defesa_magica=0,
        defesa=0,
    ),
]

inimigos_caverna = [
    Inimigo(
        "Rato das Profundezas",
        random.randint(140, 175),
        random.randint(25, 32),
        random.randint(15, 22),
        random.randint(30, 40),
    ),
    Inimigo(
        "Besouro Blindado",
        random.randint(220, 270),
        random.randint(20, 26),
        random.randint(20, 30),
        random.randint(35, 45),
    ),
    Inimigo(
        "Slime de Pedra",
        random.randint(180, 220),
        random.randint(22, 28),
        random.randint(18, 26),
        random.randint(32, 42),
    ),
    Inimigo(
        "Orc",
        random.randint(250, 310),
        random.randint(32, 40),
        random.randint(25, 35),
        random.randint(45, 55),
    ),
    Inimigo(
        "Escorpião Gigante",
        random.randint(160, 200),
        random.randint(35, 44),
        random.randint(22, 30),
        random.randint(40, 50),
    ),
]

boss_caverna = [
    Boss(
        "Golem Ancestral",
        random.randint(390, 440),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        golem_defesa,
        defesa_magica=0,
        defesa=0,
    ),
        Boss(
        "Aranha Rainha das Profundezas",
        random.randint(390, 440),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        [casulo_sombrio, veneno_ancestral],
        defesa_magica=0,
        defesa=0,
    )
]

inimigos_montanhasgeladas = [
    Inimigo(
        "Espírito do Gelo",
        random.randint(280, 340),
        random.randint(48, 58),
        random.randint(30, 42),
        random.randint(60, 75),
    ),
    Inimigo(
        "Águia Gigante",
        random.randint(250, 310),
        random.randint(52, 64),
        random.randint(28, 40),
        random.randint(55, 70),
    ),
    Inimigo(
        "Slime de Gelo",
        random.randint(320, 390),
        random.randint(42, 52),
        random.randint(32, 45),
        random.randint(65, 80),
    ),
    Inimigo(
        "Líder Orc",
        random.randint(420, 520),
        random.randint(58, 70),
        random.randint(40, 58),
        random.randint(80, 100),
    ),
    Inimigo(
        "Líder Goblin",
        random.randint(300, 370),
        random.randint(55, 66),
        random.randint(45, 60),
        random.randint(75, 90),
    ),
]

boss_montanhasgeladas = [
    Boss(
        "Dragão de Gelo",
        random.randint(550, 650),
        random.randint(75, 92),
        random.randint(280, 380),
        random.randint(450, 550),
        furia_dragão,
        defesa_magica=0,
        defesa=0,
    ),
    Boss(
        "Ymir, o Gigante de Gelo",
        random.randint(600, 640),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        tempestade_Glacial,
        defesa_magica=0,
        defesa=0,
    ),
]

inimigos_castelo = [
    Inimigo(
    "Guardião do Caos",
    random.randint(380, 450),
    random.randint(85, 98),
    random.randint(70, 95),
    random.randint(80, 100)
),
    Inimigo(
    "Espectro do Castelo",
    random.randint(250, 320),
    random.randint(80, 92),
    random.randint(45, 70),
    random.randint(60, 80)
),
    Inimigo(
    "Executor das Ruínas",
    random.randint(340, 430),
    random.randint(68, 85),
    random.randint(50, 75),
    random.randint(65, 85)
),
    Inimigo(
    "Bruxo do Caos",
    random.randint(220, 280),
    random.randint(75, 88),
    random.randint(45, 65),
    random.randint(60, 75)
),
    Inimigo(
    "Cavaleiro Corrompido",
    random.randint(260, 340),
    random.randint(60, 72),
    random.randint(40, 60),
    random.randint(55, 70)
)
]

boss_castelo_do_caos = [
    Boss(
        "Rei do Caos",
        random.randint(900, 1200),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        [ultima_resistencia, eco_dos_mortos],
        defesa=0,
        defesa_magica=0
    ),
    Boss(
    "???",
    0,
    0,
    400,
    400,
    [eco_dos_mortos, ultima_resistencia],

    )
]

boss_abismo = [
    Boss(
        "Ultimo Rei",
        random.randint(900, 1200),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        [ultima_resistencia, eco_dos_mortos],
        defesa=0,
        defesa_magica=0
    ),
]

Bandido = [
    Inimigo("Bandido", random.randint(29,36), random.randint(25, 29), random.randint(16, 24), random.randint(17,21))
]

boss_yeti = Boss(
        "Ymir, o Gigante de Gelo",
        random.randint(600, 640),
        random.randint(48, 58),
        random.randint(120, 160),
        random.randint(200, 250),
        tempestade_Glacial,
        defesa_magica=0,
        defesa=0,)
