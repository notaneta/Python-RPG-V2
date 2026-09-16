class Monstro:
    def __init__(self, nome, vida, ataque, ouro, xp):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.ouro = ouro
        self.xp = xp


goblin = Monstro(
    "Goblin",
    48,
    22,
    20,
    15
)