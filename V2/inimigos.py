import random
from lore import dialogo
from util import calcular_dano

# Variáveis antigas de aviso. Não são mais usadas (os avisos agora ficam guardados em boss.usadas),
# mas continuam aqui para não quebrar algum arquivo que ainda importe elas
texto_lobo = True
veneno = False
acabou_de_ativar = False
frase_golem = False
frase_sombra = False
frase_sombra2 = False

# ============================================================
# ARMADURA E RESISTÊNCIA MÁGICA DOS INIMIGOS
# defesa        = armadura (reduz dano de espada e habilidade)
# defesa_magica = resistência mágica (reduz dano de magia)
# Os dois são uma fração entre 0 e 1:  0.3 = leva 30% a menos / 1 = imune (dano mínimo 1)
# A conta fica em util.calcular_dano
# ============================================================

# ============================================================
# DEFESA DO HERÓI EM PORCENTAGEM
# Antes:  dano = ataque do inimigo - defesa do herói   (com amuletos, quase tudo virava 1 de dano)
# Agora:  redução = defesa / (defesa + DEFESA_K)
#         defesa  25 -> 20%     defesa 100 -> 50%     defesa 200 -> 67%     defesa 400 -> 80% (teto)
# Cada ponto de defesa continua valendo, mas vale um pouco menos que o anterior, e nunca chega em 100%
# Para deixar o jogo mais fácil DIMINUA o DEFESA_K, para deixar mais difícil AUMENTE
# ============================================================
DEFESA_K = 100
REDUCAO_MAXIMA = 0.8

def reducao_do_heroi(heroi):        # Devolve a fração de dano que a defesa do herói segura (0.5 = 50%)
    defesa = max(0, heroi.defesa)
    return min(REDUCAO_MAXIMA, defesa / (defesa + DEFESA_K))

def dano_no_heroi(heroi, dano_bruto, ignora_defesa=False):
    # TODO dano que o herói recebe de golpe passa por aqui: ataque normal e habilidade de boss
    # ignora_defesa=True é para magia e golpe especial: a defesa não segura, mas o Defender ainda corta pela metade
    from combate import levantou_defesa
    if ignora_defesa:
        dano = calcular_dano(dano_bruto, 0)
    else:
        dano = calcular_dano(dano_bruto, reducao_do_heroi(heroi))
    if levantou_defesa:
        dano = max(1, dano // 2)
    return dano


class Monstro:

    def __init__(self, nome, vida, ataque, ouro, xp, defesa=0, defesa_magica=0):

        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.ouro = ouro
        self.xp = xp
        self.defesa = defesa
        self.defesa_magica = defesa_magica
        self.skill_stun = False

    def texto_resistencias(self):       # Usado no mostrar_status e na HUD do combate
        return f"Armadura: {round(self.defesa * 100)}%   Res. Mágica: {round(self.defesa_magica * 100)}%"

    def mostrar_status(self):
        print(f"============ INIMIGO ============")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}/{self.vidamax}")
        print(f"Ataque: {self.ataque}")
        print(self.texto_resistencias())

    def atacar(self, heroi):            # Um atacar só: Inimigo e Boss herdam este (antes eram duas cópias iguais)
        from combate import levantou_defesa, usou_habilidade
        ataquefinal = dano_no_heroi(heroi, self.ataque)
        heroi.vida -= ataquefinal

        if levantou_defesa:
            print(f"\nVocê se defende! O {self.nome} te ataca causando apenas {ataquefinal} de dano")
        else:
            print(f"\nO {self.nome} te ataca causando {ataquefinal} de dano")

        if not usou_habilidade:         # Foco do heroi dentro do ataque do inimigo para garantir que seja gerado caso atacar 2 vezes
            heroi.foco = int(min(100, heroi.foco + (random.randint(10, 14) + heroi.focogen * 1.02)))

        input("\nPressione ENTER para continuar...")    # CORRIGIDO: a pausa ficava dentro do if e sumia quando o herói usava habilidade


class Inimigo(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp, defesa=0, defesa_magica=0) :
        super().__init__(nome, vida, ataque, ouro, xp, defesa, defesa_magica) # Herdou os parametros de monstro
        self.habilidade = None

    def usar_habilidade(self, heroi):
        pass

class Boss(Monstro):
    def __init__(self, nome, vida, ataque, ouro, xp, habilidade, defesa=0, defesa_magica=0) :
        super().__init__(nome, vida, ataque, ouro, xp, defesa, defesa_magica)
        self.habilidade = habilidade
        self.habilidade_usada = False
        self.skill_stun = False
        self.usadas = set()     # Guarda o NOME de cada habilidade/aviso que já aconteceu nessa luta.
                                # Com um habilidade_usada só, a primeira habilidade de um boss bloqueava a segunda

    def usar_habilidade(self, heroi):
        if self.habilidade_usada == False:
            self.habilidade(heroi,self)

def slime_absorção(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.50:
        cura = random.randint(99, 110)
        boss.vida = min(boss.vidamax, boss.vida + cura)
        print("O Rei Slime absorveu a massa de outros slimes ao redor de si!")
        print(f"Rei Slime recuperou {cura} de HP!")
        input("\nPressione ENTER para continuar...")
        boss.habilidade_usada = True

def frenesi_lobo(heroi, boss):
    if boss.vida <= boss.vidamax * 0.60:
        if "aviso_frenesi" not in boss.usadas:      # Antes era a variável global texto_lobo: o aviso só aparecia na primeira luta do jogo
            boss.usadas.add("aviso_frenesi")
            print(f"O {boss.nome} entrou em frenesi, e vai atacar 2 vezes por turno agora!")
            input("\nPressione ENTER para continuar...")
        if heroi.vida > 0:
            print(f"\n{boss.nome} está em frenesi")
            boss.atacar(heroi)

def golem_defesa_magica(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.40:
        print("O Golem se tornou ivulnerável a magias")
        print("Mas sua defesa física caiu o tornando vulnerável!")
        boss.defesa = 0             # Armadura 0%
        boss.defesa_magica = 1      # Res. Mágica 100%
        input("\nPressione ENTER para continuar...")
        boss.habilidade_usada = True

def golem_defesa(heroi, boss):
    if "aviso_golem" not in boss.usadas:
        boss.usadas.add("aviso_golem")
        print(f"O {boss.nome} parece ser muito resistente a golpes físicos!")
        print("Você terá que pensar em algum modo de causar dano!")
        input("\nPressione ENTER para continuar...")

def furia_dragão(heroi, boss):
    if boss.habilidade_usada == False and boss.vida <= boss.vidamax * 0.40: # Vida abaixo de 40%
        print("O Dragão de gelo entrou em Fúria!")
        boss.ataque = int(boss.ataque * 1.40)
        print(f"Ataque aumentou para {boss.ataque}")
        boss.habilidade_usada = True
        input("\nPressione ENTER para continuar...")

def casulo_sombrio(heroi, boss):
    if "casulo" not in boss.usadas and boss.vida <= boss.vidamax * 0.30: # Vida abaixo de 30%
        boss.usadas.add("casulo")
        print(f"A {boss.nome} se envolveu em uma teia gigante.\nA armadura dela aumentou em +40% mas o ataque dela diminuiu em -15")
        boss.ataque -= 15
        boss.defesa = min(0.9, boss.defesa + 0.4)       # Teto de 90% para não ficar imune
        input("\nPressione ENTER para continuar...")

def veneno_ancestral(heroi, boss):
    if boss.vida > boss.vidamax * 0.50:     # Só começa com a aranha abaixo de 50% de vida
        return

    if "aviso_veneno" not in boss.usadas:   # CORRIGIDO: o aviso repetia todo turno
        boss.usadas.add("aviso_veneno")
        print("A aranha se enfureceu e seus ataques causarão veneno agora!")
        input("\nPressione ENTER para continuar...\n")

    if heroi.turnos_veneno <= 0 and random.randint(1, 10) >= 5:
        heroi.turnos_veneno = 3
        print(f"{heroi.nome} foi envenenado por 3 turnos!")
        input("\nPressione ENTER para continuar...\n")

    if heroi.turnos_veneno > 0:             # CORRIGIDO: antes era a variável global veneno, que nunca voltava para False (veneno eterno)
        dano = random.randint(20, 30)       # Veneno ignora defesa e Defender
        heroi.vida -= dano
        heroi.turnos_veneno -= 1
        print(f"{heroi.nome} recebeu {dano} de dano do veneno...")
        print(f"Turnos restante até acabar veneno {heroi.turnos_veneno}")
        input("\nPressione ENTER para continuar...\n")

def tempestade_Glacial(heroi, boss):
    # Ativação
    if not boss.habilidade_usada and boss.vida <= boss.vidamax * 0.50:
        print("Ymir usou TEMPESTADE GLACIAL.")
        print("Ymir congela o campo de batalha.")
        input("\nPressione ENTER para continuar...\n")
        print("Ele irá te congelar de 3 em 3 turnos, causando dano e te deixando paralisado por 1 turno...")
        input("\nPressione ENTER para continuar...\n")
        heroi.contador_gelo = 3   # 3 turnos até o stun
        boss.habilidade_usada = True
        boss.skill_stun = True
        return

    if not boss.skill_stun:
        return

    # Turno do stun
    if heroi.contador_gelo == 0:
        dano = random.randint(10, 24)
        heroi.vida -= dano
        heroi.turnos_stun = 1
        heroi.contador_gelo = 3   # reinicia o ciclo
        print(f"{heroi.nome} recebeu {dano} e ficou paralisado devido ao frio...")
        input("\nPressione ENTER para continuar...\n")
        return

    # Contagem regressiva
    heroi.contador_gelo -= 1

def eco_dos_mortos(heroi, boss):
    # Ativação (mesma estrutura da tempestade_Glacial)
    if "eco" not in boss.usadas and boss.vida <= boss.vidamax * 0.50:
        boss.usadas.add("eco")
        dialogo(f"\n{boss.nome}: Interessante...\nHá séculos ninguém era capaz de me ferir.")
        input("\nPressione ENTER para continuar...\n")
        dialogo(f"\n{boss.nome}: Mas isso não muda nada! O mundo continuará apodrecendo!\n")
        print("Os espíritos invocados irão te atacar de 3 em 3 turnos causando dano adicional de 10% do ataque dele e te deixando paralisado por 1 turno.")
        input("\nPressione ENTER para continuar...\n")
        heroi.contador_gelo = 3
        boss.skill_stun = True      # Liga o aviso de paralisia da HUD
        return

    if "eco" not in boss.usadas:    # CORRIGIDO: os espíritos atacavam desde o turno 1, antes do boss invocar eles
        return

    # Turno do ataque dos espíritos
    if heroi.contador_gelo == 0:
        print("\nOs espiritos invocados atacam!")
        dano = dano_no_heroi(heroi, boss.ataque * 0.10, ignora_defesa=True)     # CORRIGIDO: o dano saía quebrado (30.200000000000003)
        heroi.vida -= dano
        heroi.turnos_stun = 1
        heroi.contador_gelo = 3
        print(f"Você recebeu {dano} de dano dos espiritos e ficou paralisado")
        input("\nPressione ENTER para continuar...\n")
        return

    # Contagem regressiva
    heroi.contador_gelo -= 1

def lamento_final(heroi, boss):
    if "lamento" not in boss.usadas and boss.vida <= boss.vidamax * 0.30:
        boss.usadas.add("lamento")      # CORRIGIDO: usava o habilidade_usada, que o eco_dos_mortos já tinha ligado aos 50%. Nunca acontecia
        print(f"\n{boss.nome}: Você não é nada")
        print(f"{boss.nome} usou Lamento Final .")
        cura = int(boss.vidamax * 0.40)
        boss.vida = cura
        print(f"\n{boss.nome} teve a vida recuperada para {cura}")
        boss.ataque += 30
        print(f"\n{boss.nome} teve o ataque aumentado em 30")
        input("\nPressione ENTER para continuar...\n")

def ultima_resistencia(heroi, boss):
    if "resistencia" not in boss.usadas and boss.vida <= boss.vidamax * 0.30:
        boss.usadas.add("resistencia")  # CORRIGIDO: sem isso ele voltava para 20% de vida TODO turno e ficava imortal
        print(f"\n{boss.nome}: Não!\nEu me recuso a desaparecer!\nSe o mundo deseja o caos...\nEntão eu me tornarei o próprio caos!")
        print(f"{boss.nome} usou ULTIMA RESISTENCIA.")
        cura = int(boss.vidamax * 0.20)
        boss.vida = boss.vida + cura    # Agora SOMA 20% (antes trocava a vida por 20%, e se ele estivesse com 29% a "cura" tirava vida)
        print(f"\n{boss.nome} recuperou {cura} de vida")
        input("\nPressione ENTER para continuar...\n")
    # Ideia original: "cura de emergência de 20% do HP total e dobra seu ataque". A parte de dobrar o ataque ainda não foi feita

magias_do_boss = [  # nome, dano
    ("BOLA DE FOGO", 75),
    ("RELAMPAGO ARCANO", 115),
    ("COMETA SOMBRIO", 160),
]

def copia_magias(heroi, boss):
    if random.randint(1, 10) >= 7:  # 40% de chance de não usar magia nesse turno
        print(f"\n{boss.nome} está carregando ataque mágico.")
        input("\nPressione ENTER para continuar...")
        return

    nome, danobruto = random.choice(magias_do_boss)
    dano = dano_no_heroi(heroi, danobruto, ignora_defesa=True)     # Magia ignora a defesa, mas o Defender corta pela metade
    print(f"\n{boss.nome} usou magia {nome}")
    input("\nPressione ENTER para continuar...")
    heroi.vida -= dano
    print(f"\nVocê recebeu {dano} de dano!")
    input("\nPressione ENTER para continuar...")

def execuçao_sombria(heroi, boss):
    if "execucao" in boss.usadas:       # Só acontece uma vez por luta
        return

    if boss.vida <= boss.vidamax * 0.65 and "aviso1" not in boss.usadas:
        boss.usadas.add("aviso1")
        dialogo(f"{boss.nome}: Você acha que chegou até aqui por mérito próprio?")
        print(f"\n[ALERTA] {boss.nome} está carregando sua fúria!")
        input("\nPressione ENTER para continuar...")

    if boss.vida <= boss.vidamax * 0.55 and "aviso2" not in boss.usadas:
        boss.usadas.add("aviso2")
        dialogo(f"{boss.nome}: Diga-me...\nQuantos monstros você matou para ser chamado de herói?")
        print(f"\n[ALERTA] {boss.nome} está com sua fúria completa!")
        input("\nPressione ENTER para continuar...")

    # O golpe agora leva 1 turno para sair: no turno em que a vida passa de 40% ele AVISA, no turno seguinte ele BATE
    # Antes ele batia no mesmo turno em que o herói atacou, então era impossível usar o Defender contra ele
    if "preparando" in boss.usadas:
        boss.usadas.add("execucao")
        dano = dano_no_heroi(heroi, 225, ignora_defesa=True)    # CORRIGIDO: a conta estava invertida (heroi.defesa - 225) e dava 1 de dano
        print(f"\n{boss.nome} usou Habilidade EXECUÇÃO SOMBRIA")
        input("\nPressione ENTER para continuar...")
        heroi.vida -= dano
        print(f"\nVocê recebeu {dano} de dano!")
        input("\nPressione ENTER para continuar...")

    elif boss.vida <= boss.vidamax * 0.40:
        boss.usadas.add("preparando")
        print(f"\n[ALERTA][CUIDADO] {boss.nome} ergue a lâmina!")
        print("A EXECUÇÃO SOMBRIA vem no próximo turno. Defenda-se!")
        input("\nPressione ENTER para continuar...")


# ============================================================
# ZONA 1 — FLORESTA (Nv 1-4)
# Resistências leves: a área ensina a mecânica
# ============================================================
inimigos_floresta = [
    # nome, vida, ataque, ouro, xp, defesa (armadura), defesa_magica
    Inimigo("Goblin",         random.randint(85, 100),  random.randint(15, 19), random.randint(24, 32),  random.randint(16, 24)),                                   # Sem resistência
    Inimigo("Slime",          random.randint(95, 115),  random.randint(13, 17), random.randint(20, 28),  random.randint(14, 20), defesa=0.3),                        # Corpo gelatinoso amortece a espada
    Inimigo("Aranha Gigante", random.randint(90, 110),  random.randint(17, 21), random.randint(28, 36),  random.randint(20, 28), defesa_magica=0.2),
    Inimigo("Lobo Selvagem",  random.randint(105, 125), random.randint(19, 23), random.randint(32, 42),  random.randint(22, 30)),                                   # Sem resistência
    Inimigo("Urso Ancião",    random.randint(150, 180), random.randint(24, 28), random.randint(50, 65),  random.randint(35, 48), defesa=0.2),                        # Couro grosso
]

boss_floresta = [
    Boss("Rei Slime",
         random.randint(370, 380),
         random.randint(34, 42),    # era 40-50. Com a defesa em porcentagem o herói do nível 3 leva mais dano
         random.randint(70, 80),
         random.randint(50, 60),
         [slime_absorção],
         defesa=0.2,
         defesa_magica=0),

    Boss("Lobo Superior",
         random.randint(460, 470),
         random.randint(36, 44),    # era 48-56. Ele ataca 2 vezes por turno em frenesi
         random.randint(70, 80),
         random.randint(45, 55),
         [frenesi_lobo],
         defesa=0,
         defesa_magica=0.2),
]


# ============================================================
# ZONA 2 — CAVERNA (Nv 5-9)
# Área das carapaças: quase tudo aqui pede magia
# ============================================================
inimigos_caverna = [
    Inimigo("Rato das Profundezas", random.randint(190, 230), random.randint(30, 36), random.randint(65, 85),  random.randint(45, 60)),                                         # Sem resistência
    Inimigo("Besouro Blindado",     random.randint(240, 290), random.randint(34, 42), random.randint(80, 100), random.randint(55, 72), defesa=0.5),                              # Carapaça
    Inimigo("Slime de Pedra",       random.randint(215, 260), random.randint(32, 38), random.randint(72, 92), random.randint(50, 66), defesa=0.4, defesa_magica=0.1),
    Inimigo("Escorpião Gigante",    random.randint(225, 275), random.randint(38, 46), random.randint(85, 108), random.randint(60, 78), defesa=0.3, defesa_magica=0.1),
    Inimigo("Orc",                  random.randint(290, 350), random.randint(42, 52), random.randint(105, 135), random.randint(75, 95), defesa=0.1, defesa_magica=0.3),         # Amuletos tribais: pede espada
]

boss_caverna = [
    Boss("Golem Ancestral",
         random.randint(560, 570),
         random.randint(72, 82),
         random.randint(150, 160),
         random.randint(110, 120),
         [golem_defesa, golem_defesa_magica],
         defesa=0.6,                # Era 0.8, a luta passava de 40 turnos na espada. Abaixo de 40% de vida inverte (golem_defesa_magica)
         defesa_magica=0),

    Boss("Aranha Rainha das Profundezas",
         random.randint(690, 700),
         random.randint(92, 102),
         random.randint(160, 170),
         random.randint(120, 130),
         [casulo_sombrio, veneno_ancestral],
         defesa=0.1,
         defesa_magica=0.3),
]


# ============================================================
# ZONA 3 — MONTANHAS GELADAS (Nv 10-14)
# ============================================================
inimigos_montanhasgeladas = [
    Inimigo("Águia Gigante",    random.randint(340, 410), random.randint(56, 68), random.randint(130, 165), random.randint(100, 130), defesa_magica=0.3),              # Rápida demais para magia
    Inimigo("Espírito do Gelo", random.randint(370, 450), random.randint(62, 76), random.randint(145, 185), random.randint(115, 150), defesa=0.5),                     # Sem corpo: a espada atravessa
    Inimigo("Slime de Gelo",    random.randint(420, 510), random.randint(60, 74), random.randint(165, 205), random.randint(130, 170), defesa=0.3, defesa_magica=0.2),
    Inimigo("Líder Goblin",     random.randint(470, 580), random.randint(70, 86), random.randint(185, 235), random.randint(150, 195), defesa=0.3, defesa_magica=0.1),
    Inimigo("Líder Orc",        random.randint(540, 660), random.randint(80, 98), random.randint(215, 270), random.randint(175, 230), defesa=0.2, defesa_magica=0.4),
]

boss_montanhasgeladas = [
    Boss("Dragão de Gelo",
         random.randint(800, 880),
         random.randint(140, 150),
         random.randint(290, 300),
         random.randint(240, 250),
         [furia_dragão],
         defesa=0.4,                # Escamas
         defesa_magica=0.2),

    Boss("Ymir, o Gigante de Gelo",
         random.randint(1220, 1230),
         random.randint(158, 168),
         random.randint(300, 310),
         random.randint(250, 260),
         [tempestade_Glacial],
         defesa=0.2,
         defesa_magica=0.5),
]


# ============================================================
# ZONA 4 — CASTELO DO CAOS (Nv 15-20)
# Extremos: errar o tipo de ataque aqui custa caro
# ============================================================
inimigos_castelo = [
    Inimigo("Espectro do Castelo",  random.randint(430, 530), random.randint(92, 112), random.randint(230, 290), random.randint(190, 240), defesa=0.6),                        # Fantasma: use magia
    Inimigo("Bruxo do Caos",        random.randint(455, 560), random.randint(100, 120), random.randint(245, 305), random.randint(200, 255), defesa_magica=0.6),                 # Mago: use espada
    Inimigo("Cavaleiro Corrompido", random.randint(500, 620), random.randint(85, 105),  random.randint(260, 320), random.randint(215, 270), defesa=0.5, defesa_magica=0.1),
    Inimigo("Executor das Ruínas",  random.randint(630, 770), random.randint(108, 132), random.randint(310, 380), random.randint(255, 325), defesa=0.35, defesa_magica=0.15),
    Inimigo("Guardião do Caos",     random.randint(700, 850), random.randint(120, 148), random.randint(360, 445), random.randint(295, 375), defesa=0.2, defesa_magica=0.5),
]

boss_castelo_do_caos = [
    Boss(
        "Rei do Caos",
        random.randint(1600, 1700),
        random.randint(220, 240),
        random.randint(550, 560),
        random.randint(270, 280),
        [ultima_resistencia],
        defesa=0.3,
        defesa_magica=0.3
    ),
    Boss(
        "???",                       # boss especial (raid)
        random.randint(1900, 2250),
        random.randint(175, 210),
        random.randint(1500, 1900),
        random.randint(1300, 1700),
        [execuçao_sombria, copia_magias],
        defesa=0.25,
        defesa_magica=0.4            # Ele copia suas magias, então resiste a elas
    ),
]


# ============================================================
# ZONA 5 — ABISMO (Nv 20+)
# ============================================================
boss_abismo = [
    Boss(
        "Ultimo Rei",
        random.randint(3000, 3100),
        random.randint(260, 310),
        random.randint(4000, 5000),
        random.randint(3500, 4500),
        [lamento_final, eco_dos_mortos],
        defesa=0.35,
        defesa_magica=0.35
    ),
]


# ============================================================
# EXTRAS
# ============================================================
Bandido = [
    Inimigo("Bandido",
            random.randint(38, 48),
            random.randint(32, 38),
            random.randint(22, 32),
            random.randint(22, 30))
]

boss_yeti = Boss(
    "Ymir, o Gigante de Gelo",
    random.randint(1680, 1920),
    random.randint(125, 148),
    random.randint(950, 1200),
    random.randint(850, 1100),
    [tempestade_Glacial],
    defesa=0.2,
    defesa_magica=0.5
)
