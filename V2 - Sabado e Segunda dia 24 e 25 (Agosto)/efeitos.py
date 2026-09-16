import random

# Tentativa de fazer efeitos
class Efeitos:
    def __init__(self, nome, dano, atordoar, esquivar, turnos):
        self.nome = nome
        self.dano = dano
        self.atordoar = atordoar
        self.esquivar = esquivar
        self.turnos = turnos

    def pular_turno(self, heroi):
        if self.atordoar > 1:
            heroi.ataque # Pode ser reduzido a zero, ou crio um novo IF durante a LUTA e caso o atordoamento seja TRUE ele previne o jogador de fazer algo, pulando o turno automaticamente.


lista_efeitos = [
    Efeitos("Veneno", random.randint(6, 12), 0, 0, random.randint(3,5)),
    Efeitos("Roubo de Vida", random.randint(8, 16), 0, 0, 40),
    Efeitos("Atordoar", 0, 1, 0, random.randint(2, 3)),
    Efeitos("Sangramento", random.randint(10,20), 0, 0, random.randint(3, 5)),
    Efeitos("Esquiva", 0, 0 , 1, 1)
]

# Verificação de efeitos
for item in lista_efeitos:
    print(f" Efeito: Nome: {item.nome}, Dano: {item.dano}, Atordoar: {item.atordoar}, Esquiva: {item.esquivar}, Turno: {item.turnos}):")
            