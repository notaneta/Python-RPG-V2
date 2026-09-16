import random
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
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.40:
        print("O Dragão de gelo entrou em Fúria!")
        boss.ataque = int(boss.ataque * 1.50)
        print(f"Ataque aumentou para {boss.ataque}")
        boss.habilidade_usada = True
        input("\nPressione ENTER para continuar...")
        

inimigos_floresta = [           # Nome, Vida, Ataque, Ouro ,XP
Inimigo("Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), # Rouba dinheiro
Inimigo("Slime", random.randint(39,50), random.randint(7, 13), random.randint(16, 24), random.randint(17,21)), # Dividir-se em dois (Ver se é possivel dois inimigos ao mesmo tempo)
Inimigo("Aranha Gigante", random.randint(29,38), random.randint(15, 21), random.randint(16, 24), random.randint(17,21)), # Teia atrasar turno jogador
Inimigo("Urso Ancião", random.randint(40,50), random.randint(20, 26), random.randint(21, 29), random.randint(17,21)), # Deixa sangramento
Inimigo("Lobo Selvagem", random.randint(29,36), random.randint(25, 29), random.randint(16, 24), random.randint(17,21)), # Chance de esquivar ataques
]

boss_floresta = [ # Nome, Vida, Ataque, Ouro ,XP , EXCLUSIVO DOS BOSSES POR HORA , defesa magica e defesa(ataque)
Boss("Rei Slime", random.randint(300, 329), random.randint(24, 33), random.randint(36, 44), random.randint(37,41), slime_absorção, 0, 0),
Boss("Lobo Superior", random.randint(470, 560), random.randint(40, 53), random.randint(36, 44), random.randint(37,41), frenesi_lobo, 0, 0),
]

inimigos_caverna = [
Inimigo("Rato das Profundezas", random.randint(72,81), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Besouro Blindado", random.randint(79,80), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime de Pedra", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Orc", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Escorpião Gigante", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
]

boss_caverna = [
Boss("Golem Ancestral", random.randint(540,650), random.randint(46, 55), random.randint(48,67), random.randint(48,59), golem_defesa, 0, 0),
]

inimigos_montanhasgeladas = [
Inimigo("Espírito do Gelo", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Águia Gigante", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime de Gelo", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Líder Orc", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Líder Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
]

boss_montanhasgeladas = [
Boss("Dragão de Gelo", random.randint(720,840), random.randint(60, 79), random.randint(68, 74), random.randint(67,73), furia_dragão, 0, 0),
]

boss_especial_floresta = [ # Nome, Vida, Ataque, Ouro ,XP
Boss("Rei Slime", random.randint(300, 329), random.randint(24, 33), random.randint(36, 44), random.randint(37,41), 0, 0, 0)
]
