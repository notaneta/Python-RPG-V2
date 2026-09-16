# Trilha de progressão será definida aqui

# O mundo é dividido em áreas (ex: Floresta Inicial - Caverna de Gelo - Castelo Sombrio). Cada cenário possui sua própria lista de inimigos, tabela de saques (loot) e Boss regional.
from combate import combateini
from inimigos import boss_floresta, boss_caverna, inimigos_caverna, inimigos_floresta

class Progressao:

    def __init__(self, nome, nivel_recomendado, lista_inimigos, boss, proximo_cenario):
        self.nome = nome
        self.nivel_recomendado = nivel_recomendado
        self.lista_inimigos = lista_inimigos  # Lista de objetos Inimigo
        self.boss = boss  # Objeto Inimigo (Boss da zona)
        self.bossderrotado = False
        self.progresso = 0  # Lutas concluídas no cenário
        self.lutas_para_boss = 5
        self.proximo_cenario = proximo_cenario

        def chamarboss(self):
            if not self.bossderrotado and self.progresso >= self.lutas_para_boss:
                if self.progresso == 5:
                

                    combateini()

        def avançarjogo(self):
            self
            if self.progresso == 5:
                print

# 1. Cria as zonas
zona2_caverna = Progressao("Caverna Sombria", 5, inimigos_caverna, boss_caverna)
zona1_floresta = Progressao("Floresta Verde", 1, inimigos_floresta, boss_floresta, proximo_cenario=zona2_caverna)

zona_atual = zona1_floresta

def menumundo(heroi):   
    while True:
        print(f"Local Atual: {zona_atual.nome}")
        opcao = input("1 - Explorar Zona\n2 - Ir para Próxima Zona\n> ")

        if opcao == "1":
            zona_atual.explorar(heroi)

        elif opcao == "2":
            if zona_atual.bossderrotado and zona_atual.proximo_cenario:
                zona_atual = zona_atual.proximo_cenario
                print(f"Você viajou para {zona_atual.nome}!")
            else:
                print("Você precisa derrotar o Boss desta zona para avançar!")