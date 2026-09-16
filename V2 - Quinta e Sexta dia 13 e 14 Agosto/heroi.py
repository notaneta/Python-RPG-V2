class Heroi:

    def __init__(self, nome, vida):

        self.nome = nome
        self.vida = vida
        self.ataque = 7
        self.defesa = 5
        self.Mana = 40
        self.ouro = 20
        self.nivel = 1


    def mostrar_status(self):

        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ouro: {self.ouro}")