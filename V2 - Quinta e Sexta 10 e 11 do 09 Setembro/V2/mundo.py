import random, copy, sys
from combate import combateini, combatesys
from inimigos import boss_floresta, boss_caverna, inimigos_caverna, inimigos_floresta, inimigos_montanhasgeladas, boss_montanhasgeladas, inimigos_castelo, boss_castelo_do_caos, boss_abismo
from util import limpar_tela
from lore import boss_final_dialogo, boss_final_dialogo_2
from eventos import final_verdadeiro
lutaboss = False   # Parece ser inutil, dps testar, se for remover
dialogo2_boss = False

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
        global lutaboss, final_verdadeiro, dialogo2_boss
        if not self.bossderrotado and self.progresso >= self.lutas_para_boss:
            inimigo = copy.deepcopy(self.boss[0])

            if  zona_atual == zona4_castelo_do_caos:
                boss_final_dialogo(heroi, inimigo)
            
            lutaboss = True
            combatesys(heroi, inimigo)
            lutaboss = False

            if final_verdadeiro and dialogo2_boss == False:
                boss_final_dialogo_2(heroi, inimigo)
                dialogo2_boss == True


    def chamar_boss_especial(self, heroi):
        if zona_atual == zona4_castelo_do_caos:
            from eventos import evento_raid_vila_destruida
            evento_raid_vila_destruida(heroi)
            limpar_tela()
            heroi.furiagen += 30
            print("Parabéns! Você venceu a luta e sua geração de Fúria aumentou em +30")
            input("Pressione ENTER para continuar...")

            return

        inimigo = copy.deepcopy(self.boss[1])
        combatesys(heroi, inimigo)
        if inimigo.vida <= 0:
            limpar_tela()
            heroi.furiagen += 10
            print("Parabéns! Você venceu a luta e sua geração de Fúria aumentou em +10")
            input("Pressione ENTER para continuar...")

    def avançarjogo(self):
        self.progresso +=1


# 1. Zonas
zona5_abismo = Progressao("Abismo do Rei", None, boss_abismo, proximo_cenario=None, lutas_para_boss = 0)
zona4_castelo_do_caos = Progressao("Castelo do Caos", inimigos_castelo, boss_castelo_do_caos, proximo_cenario=zona5_abismo)   # Cavaleiros sombrios, etc /  final boss
zona3_montanhagelada = Progressao("Montanha Congelada", inimigos_montanhasgeladas, boss_montanhasgeladas, proximo_cenario=zona4_castelo_do_caos)   
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

            elif zona_atual.bossderrotado == True and zona_atual.progresso == 6 and not zona_atual.boss_especial_derrotado:
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

                        if zona_atual == zona5_abismo:
                            print("Você terminou o jogo e fez o final verdadeiro! Meus Parabéns!")
                            input("Pressione ENTER para continuar...\n")
                            print("Você terminou o jogo com esses Status:")
                            heroi.mostrar_status()
                            input("\nPressione ENTER para continuar...")

                            sys.exit()

                        if zona_atual == zona4_castelo_do_caos:
                            if not final_verdadeiro:

                                print("Você terminou o jogo! Parabéns!")
                                input("Pressione ENTER para continuar...\n")
                                print("Você terminou o jogo com esses Status:")
                                heroi.mostrar_status()
                                input("\nPressione ENTER para continuar...")

                                # Fazer um ranking online de quem terminou mais forte / ou pontos acumulados e com os bosses derrotados 
                                sys.exit()

                        else:

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