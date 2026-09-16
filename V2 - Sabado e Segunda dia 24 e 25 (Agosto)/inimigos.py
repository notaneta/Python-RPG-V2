import random
class Monstro:

    def __init__(self, nome, vida, ataque, ouro, xp):

        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.ouro = ouro
        self.xp = xp

    def mostrar_status(self):
        print("============ INIMIGO ============")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}/{self.vidamax}")
        print(f"Ataque: {self.ataque}")

    def atacar(self, heroi):
            ataquefinal = max(1, self.ataque - heroi.defesa)
            heroi.vida -= ataquefinal
            print(f"\nO {self.nome} te ataca causando {ataquefinal} de dano")
        



class Inimigo(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herou os parametros de personagem

        # self.skill = skill  # Pensar em como vou fazer para chamar a skill

class Boss(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herou os parametros de personagem
        

        # self.skill = skill  # Pensar em como vou fazer para chamar a skill


inimigos_floresta = [           # Nome, Vida, Ataque, Ouro ,XP
Inimigo("Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), # Rouba dinheiro
Inimigo("Slime", random.randint(39,50), random.randint(7, 13), random.randint(16, 24), random.randint(17,21)), # Dividir-se em dois (Ver se é possivel dois inimigos ao mesmo tempo)
Inimigo("Aranha Gigante", random.randint(29,38), random.randint(15, 21), random.randint(16, 24), random.randint(17,21)), # Teia atrasar turno jogador
Inimigo("Urso Ancião", random.randint(40,50), random.randint(20, 26), random.randint(21, 29), random.randint(17,21)), # Deixa sangramento
Inimigo("Lobo Selvagem", random.randint(29,36), random.randint(25, 29), random.randint(16, 24), random.randint(17,21)), # Chance de esquivar ataques
]

boss_floresta = [
Boss("Slime", random.randint(300, 329), random.randint(24, 33), random.randint(36, 44), random.randint(37,41)),
]

inimigos_caverna = [
Inimigo("Rato das Profundezas", random.randint(72,81), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Besouro Blindado", random.randint(79,80), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime de Pedra", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Orc", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Escorpião Gigante", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
]

boss_caverna = [
Boss("Golem Ancestral", random.randint(540,650), random.randint(46, 55), random.randint(48,67), random.randint(48,59)),
]

inimigos_montanhasgeladas = [
Inimigo("Espírito do Gelo", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Águia Gigante", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime de Gelo", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Líder Orc", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Líder Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
]

boss_montanhasgeladas = [
Boss("Dragão de Gelo", random.randint(720,840), random.randint(60, 79), random.randint(68, 74), random.randint(67,73)),
]

