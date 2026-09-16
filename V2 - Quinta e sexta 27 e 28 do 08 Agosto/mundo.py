# Trilha de progressão será definida aqui

# O mundo é dividido em áreas (ex: Floresta Inicial - Caverna de Gelo - Castelo Sombrio). Cada cenário possui sua própria lista de inimigos, tabela de saques (loot) e Boss regional.
import random, copy
from combate import combateini
from inimigos import boss_floresta, boss_caverna, inimigos_caverna, inimigos_floresta

class Progressao:

    def __init__(self, nome, lista_inimigos, boss, proximo_cenario):
        self.nome = nome
        self.lista_inimigos = lista_inimigos  # Lista de objetos Inimigo
        self.boss = boss  # Objeto Inimigo (Boss da zona)
        self.bossderrotado = False
        self.progresso = 0  # Lutas concluídas no cenário
        self.lutas_para_boss = 5
        self.proximo_cenario = proximo_cenario

    def explorar(self, heroi):
            inimigoaleatório = copy.deepcopy(random.choice(self.lista_inimigos))
            combateini(heroi, inimigoaleatório)
            return
            
    def chamarboss(self, heroi):
        if not self.bossderrotado and self.progresso >= self.lutas_para_boss:
            if self.progresso == 5:

                inimigo = self.boss
                combateini(heroi, inimigo)

    def avançarjogo(self):
        self
        if self.progresso == 5:
            print

# 1. Zonas
zona4_castelo_do_caos = Progressao("TESTE", 1 , 1 ,1)   # Cavaleiros sombrios, etc /  final boss
zona3_montanhagelada = Progressao("TESTE", 1 , 1, 1)   
zona2_caverna = Progressao("Caverna Sombria", inimigos_caverna, boss_caverna, proximo_cenario=zona3_montanhagelada)
zona1_floresta = Progressao("Floresta Verde", inimigos_floresta, boss_floresta, proximo_cenario=zona2_caverna)


zona_atual = zona1_floresta
inimigos_acampamento = zona_atual.lista_inimigos  # Faz os inimigos do acampamento serem sempre baseados no local ondem você está, porém vou pensar ainda se eixo essa opção, pois pode ser chato ficar lutando toda hora
# Pensar se vai ter luta ou não no acampamento, para deixar mais dificil, ou não ter para ser menos repetitivo

def menumundo(heroi):   
    while True:
        global zona_atual
        print(f"Local Atual: {zona_atual.nome}")
        opcao = input("1 - Explorar Zona\n2 - Ir para Próxima Zona\n> 0 - Voltar Menu\n")

        if opcao == "1":
            zona_atual.explorar(heroi)
            break

        elif opcao == "2":
            if zona_atual.bossderrotado and zona_atual.proximo_cenario:
                zona_atual = zona_atual.proximo_cenario
                print(f"Você viajou para {zona_atual.nome}!")
                
            else:
                print("Você precisa derrotar o Boss desta zona para avançar!")

        elif opcao == "0":
            return