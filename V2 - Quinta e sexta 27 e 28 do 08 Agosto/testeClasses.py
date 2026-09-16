class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.venda = 0

    def Vendeu(self, venda):
        self.venda = venda

    def Batermeta(self, meta):
        if self.venda >= meta:
            print(f"{self.nome} Bateu a meta")
        else:
            print(f"{self.nome} Falhou miseravel")

Vendedor1 = Vendedor("Lucas")
Vendedor1.Vendeu = 100
Vendedor1.Batermeta = 50
Vendedor2 = Vendedor("Marcos")
Vendedor2.venda = 49
Vendedor2.Batermeta = 50

        


#class Heroi:

#    def __init__(self, nome, vida):

 #       self.nome = nome
  #      self.vida = vida
   #     self.ouro = 20
    #    self.nivel = 1
#
 #   def mostrar_status(self):
#
 #       print(f"Nome: {self.nome}")
  #      print(f"Vida: {self.vida}")
   #     print(f"Ouro: {self.ouro}")

# jogador = Heroi("Lucas", 80)

# jogador.mostrar_status()


# class Monstro:
#    def __init__(self, nome, vida, ataque, ouro, xp):
 #       self.nome = nome
  #      self.vida = vida
   #     self.ataque = ataque
    #    self.ouro = ouro
     #   self.xp = xp

# goblin = Monstro(
#    "Goblin",
#    48,
 #   22,
  ## 15
# )

# Porém existe como usar Herança, assim as classes que eu quiser sempre herdaram caracteristicas e outras classes


from combate import combateini


class Personagem:

    def __init__(self, nome, vida, ataque, mana, ouro, nivel, xp):

        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.mana = mana
        self.manamax = mana
        self.ouro = ouro
        self.nivel = nivel
        self.xp = xp

    def mostrar_status(self):
        print("============STATUS============")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}/{self.vidamax}")
        print(f"Mana: {self.mana}/{self.manamax}")
        print(f"Ataque: {self.ataque}")
        print(f"Ouro: {self.ouro}")    
        print(f"Nível: {self.nivel}")

    def inventario(self):
        print()

class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 100, 10, 40, 20, 1, 0) # Herdou os parametros de personagem

class Monstro:  # Pode ser removido e o inimigo ganhar apenas a class herdada de personagem com arguemtos necessários

    def __init__(self, nome, vida, ataque, ouro, xp):

        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.ouro = ouro
        self.xp = xp

class Inimigo(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp) : 
        super().__init__(nome, vida, ataque, ouro, xp) # Herou os parametros de personagem

        # self.skill = skill  # Pensar em como vou fazer para chamar a skill

listainimigos = [ 
Inimigo("Goblin", 39, 17, 15, 17), # Nome, Vida, Ataque, Ouro ,XP
Inimigo("Slime Marrom", 42, 9, 13, 14),
]
inimigoacampamento = [
Inimigo("Ladrão", 43, 23, 30, 24),
Inimigo("Slime Azul", 42, 9, 13, 14)
]



import random
import sys


inimigoaleatório = random.choice(list(listainimigos))

# "Agora tudo precisa virar classe?"
# A resposta é: não
# O objetivo não é transformar tudo em classe. O objetivo é colocar em classes aquilo que representa um objeto do jogo.
 # Por que função?
# Porque o combate é um evento.
# Não é uma coisa.

# Main

input("Bem vindo a RPG OVERWORLD 2 \nPressione ENTER para continuar...")
jogador = Heroi(input("Digite o nome do seu personagem: "))
jogador.mostrar_status()
print("As regras do jogo são simples, veja: ")


#Funções

def combateini():   # Não funciona
    escolha = input("1 -lutar/2 - fugir")
    if escolha == "1":
        while jogador.vida > 0 or inimigoaleatório.vida > 0:
            jogador.mostrar_status()
            print("A luta começa")
            combatesys()
            return
    elif escolha == "2":
        testefugir = random.randint(1, 10) 
        if testefugir >= 5:
            print("Você fugiu com sucesso")
        else:
            print("Você não conseguiu fugir e terá que lutar")
            print("A luta começa")
            combatesys()
            return

def combatesys():
    while jogador.vida > 0 or inimigoaleatório.vida > 0:

        jogador.mostrar_status()
        print("Sua opções são:")
        lutar = input("1 -Atacar\n2 - Lançar Magia\n3 - Usar Item\nQual sua decisão?")

        turnojogador = True

        if lutar == '1':
            turnojogador = True



        elif lutar == "2":
            turnojogador = usarmagia()
            usarmagia()


        elif lutar == '3':
            usaritem()

    if turnojogador and inimigoaleatório > 0:
        print(f"O {inimigoaleatório.vida} te ataca causando {inimigoaleatório.ataque} de dano")   


    else:
        if jogador.vida <= 0:
            print("Seu HP foi reduzido a 0, Você perdeu...")
            sys.exit()
        elif inimigoaleatório.vida <=0:
            print("Você derrotou o inimigo")
            jogador.ouro += inimigoaleatório.ouro

def usarmagia():
    print

def usaritem():
    print

combateini(jogador, inimigoaleatório)
combatesys(jogador, inimigoaleatório)

# Colocando os comandos dentro dos modulos corretos e criando as funçoes necessárias para o game
# Problema era o recompiler do pc da empresa mesmo, modulos funcionam normal aqui


