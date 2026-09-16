import random, copy
from combate import combateini, combatesys
from inimigos import boss_floresta, boss_caverna, inimigos_caverna, inimigos_floresta
from util import limpar_tela
lutaboss = False

class Progressao:

    def __init__(self, nome, lista_inimigos, boss, proximo_cenario):
        self.nome = nome
        self.lista_inimigos = lista_inimigos  # Lista de objetos Inimigos
        self.boss = boss  # Objeto Inimigo (Boss da zona)
        self.bossderrotado = False
        self.progresso = 0  # Lutas concluídas no cenário
        self.lutas_para_boss = 5
        self.boss_especial_derrotado = False
        self.proximo_cenario = proximo_cenario

    def explorar(self, heroi):
        inimigoaleatório = copy.deepcopy(random.choice(self.lista_inimigos))
        combateini(heroi, inimigoaleatório)
        return
            
    def chamarboss(self, heroi):
        global lutaboss
        if not self.bossderrotado and self.progresso >= self.lutas_para_boss:
            inimigo = copy.deepcopy(self.boss[0])
            lutaboss = True
            combatesys(heroi, inimigo)
            lutaboss = False

    def chamar_boss_especial(self, heroi):
            inimigo = copy.deepcopy(self.boss[1])
            combatesys(heroi, inimigo)
            if inimigo.vida <= 0:
                limpar_tela()
                print("Parabéns! Você venceu a luta e sua geração de Fúria aumentou em +10")
                input("Pressione ENTER para continuar...")

    def avançarjogo(self):
        self.progresso +=1


# 1. Zonas
zona4_castelo_do_caos = Progressao("TESTE", 1 , 1 ,1)   # Cavaleiros sombrios, etc /  final boss
zona3_montanhagelada = Progressao("TESTE", 1 , 1, 1)   
zona2_caverna = Progressao("Caverna Sombria", inimigos_caverna, boss_caverna, proximo_cenario=zona3_montanhagelada)
zona1_floresta = Progressao("Floresta Verde", inimigos_floresta, boss_floresta, proximo_cenario=zona2_caverna)


zona_atual = zona1_floresta # nome, lista_inimigos, boss, proximo_cenario):
inimigos_acampamento = zona_atual.lista_inimigos  # Faz os inimigos do acampamento serem sempre baseados no local ondem você está, porém vou pensar ainda se eixo essa opção, pois pode ser chato ficar lutando toda hora
# Pensar se vai ter luta ou não no acampamento, para deixar mais dificil, ou não ter para ser menos repetitivo

def menumundo(heroi):   
    while True:
        global zona_atual
        limpar_tela()
        if zona_atual.progresso >= 5 and zona_atual.bossderrotado == False:
            print("Cuidado, a proxima luta será contra o CHEFE da área!")
            input("Pressione ENTER para continuar...")
            limpar_tela()

        print(f"Local Atual: {zona_atual.nome} Inimigos derrotados: {zona_atual.progresso}")
        opcao = input("1 - Explorar Zona\n2 - Ir para Próxima Zona (Avançar Jogo)\n0 - Voltar Menu\n")

        if opcao == "1":
            if zona_atual.bossderrotado == False:
                if zona_atual.progresso >= 5:
                    zona_atual.chamarboss(heroi)
                    zona_atual.bossderrotado = True
                    return
                else:
                    zona_atual.explorar(heroi)

            elif zona_atual.bossderrotado == True and zona_atual.progresso == 6 and zona_atual.boss_especial_derrotado == False:
                while True:
                    escolha = input("Você sente uma sensação estranha....\n[ALERTA] Algo MUITO PODEROSO parece estar vindo para lutar contra você!\n1 - Lutar\n2 - Sair\n")
                    if escolha == "1":
                        zona_atual.chamar_boss_especial(heroi)
                        zona_atual.boss_especial_derrotado = True

                    elif escolha == "2":
                        return

                    else:
                        print("Comando não existe...")
                        input("Pressione ENTER para continuar...")
                    
                    
            else:
                print("Você já explorou a área e pode seguir em frente!")
                input("Pressione ENTER para continuar...")
            

        elif opcao == "2":
            if zona_atual.bossderrotado and zona_atual.proximo_cenario:
                while True:
                    escolha = input("Após sair da Área não poderá voltar...\n1 - Mudar de Área\n2 - Voltar\n")
                    if escolha == "1":
                        zona_atual = zona_atual.proximo_cenario
                        print(f"Você viajou para {zona_atual.nome}!")
                        input("Pressione ENTER para continuar...")

                    elif escolha == "2":
                        return

                    else:
                        print("Comando não existe...")
                        input("Pressione ENTER para continuar...")
            else:
                print("Explore a Zona primeiro")
                print("Você precisa derrotar o Boss desta zona para avançar!")
                input("Pressione ENTER para continuar...")

        elif opcao == "0":
            return