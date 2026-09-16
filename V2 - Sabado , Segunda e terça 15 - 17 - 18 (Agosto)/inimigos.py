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
        



class Inimigo(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herou os parametros de personagem

        # self.skill = skill  # Pensar em como vou fazer para chamar a skill

class Boss(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp, progresso) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herou os parametros de personagem
        self.progresso = progresso

        # self.skill = skill  # Pensar em como vou fazer para chamar a skill


inimigos_floresta = [           # Nome, Vida, Ataque, Ouro ,XP
Inimigo("Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime Marrom", random.randint(39,50), random.randint(7, 13), random.randint(16, 24), random.randint(17,21)),
]

inimigos_caverna = [
Inimigo("Goblin", random.randint(29,41), random.randint(17, 26), random.randint(16, 24), random.randint(17,21)), 
Inimigo("Slime Marrom", random.randint(39,50), random.randint(7, 13), random.randint(16, 24), random.randint(17,21)),
]

inimigoacampamento = [
Inimigo("Ladrão", random.randint(43, 49), random.randint(23, 29), random.randint(25, 30), random.randint(24,28)),
Inimigo("Slime Azul", 42, 9, 13, 14)
]

boss_floresta = [
Boss("Slime Rei", 39, 17, 15, 17),
Boss("Slime Marrom", 42, 9, 13, 14),
]
