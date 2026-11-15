# ============================================================
# SIMULADOR DE BALANCEAMENTO
# Não faz parte do jogo. Rode com:  python simulador.py   (dentro da pasta do jogo)
# Ele monta um herói "esperado" para cada zona e mostra, para cada inimigo:
#   - quantos turnos o herói leva para matar só na espada
#   - quanto dano uma magia causa
#   - quanto dano o herói leva por golpe e quantos golpes ele aguenta
# Mude os números do jogo, rode de novo e compare.
# ============================================================
import inimigos as I

# ---- Crescimento do herói (copie do heroi.py se mudar lá) ----
VIDA, ATAQUE, DEFESA, MANA = 170, 13, 7, 30
CRESCE_VIDA, CRESCE_MANA, CRESCE_ATAQUE, DEFESA_POR_NIVEL = 1.06, 1.10, 1.07, 1

# ---- Em que nível o jogador costuma comprar cada amuleto (nível: bônus) ----
# É um chute. Jogue, anote o que você realmente tinha em cada zona e ajuste aqui
AMULETOS_ATAQUE = {1: 4, 3: 8, 5: 14, 6: 12, 8: 20, 10: 28, 12: 24, 15: 38, 16: 42, 18: 50}
AMULETOS_DEFESA = {1: 3, 3: 5, 5: 9, 6: 12, 8: 14, 10: 20, 12: 24, 15: 28, 16: 42, 18: 38}

# ---- Magias: nível, dano base, custo (copie do magias.py) ----
MAGIAS = [(2, 22, 18), (4, 45, 30), (6, 75, 48), (10, 115, 68), (14, 160, 95)]
PROPORCAO_MP = 0.3

ZONAS = [   # nome, nível esperado do herói, inimigos
    ("Floresta", 3,  I.inimigos_floresta + I.boss_floresta),
    ("Caverna",  7,  I.inimigos_caverna + I.boss_caverna),
    ("Montanha", 12, I.inimigos_montanhasgeladas + I.boss_montanhasgeladas),
    ("Castelo",  17, I.inimigos_castelo + I.boss_castelo_do_caos),
    ("Abismo",   20, I.boss_abismo),
]

class HeroiSimulado:
    def __init__(self, nivel):
        self.vida, self.ataque, self.defesa, self.mana = VIDA, ATAQUE, DEFESA, MANA
        for n in range(1, nivel + 1):
            if n > 1:
                self.vida = int(self.vida * CRESCE_VIDA)
                self.mana = int(self.mana * CRESCE_MANA)
                self.ataque = int(self.ataque * CRESCE_ATAQUE)
                self.defesa += DEFESA_POR_NIVEL
            self.ataque += AMULETOS_ATAQUE.get(n, 0)
            self.defesa += AMULETOS_DEFESA.get(n, 0)

for nome, nivel, lista in ZONAS:
    h = HeroiSimulado(nivel)
    reducao = I.reducao_do_heroi(h)
    magia = [m for m in MAGIAS if m[0] <= nivel][-1]
    dano_magia = magia[1] + h.mana * PROPORCAO_MP

    print(f"\n=== {nome} | herói nível {nivel}: Vida {h.vida}  Ataque {h.ataque}  Defesa {h.defesa} (segura {reducao:.0%})  MP {h.mana} ===")
    print(f"    melhor magia: {dano_magia:.0f} de dano, custa {magia[2]} MP ({h.mana // magia[2]} uso(s) com a mana cheia)")
    print(f"    {'INIMIGO':30} {'VIDA':>5} | {'ESPADA':>6} {'TURNOS':>6} | {'MAGIA':>5} | {'LEVA':>5} {'AGUENTA':>8}")
    for e in lista:
        espada = max(1, h.ataque * (1 - e.defesa))
        magia_final = max(1, dano_magia * (1 - e.defesa_magica))
        leva = max(1, e.ataque * (1 - reducao))
        print(f"    {e.nome:30} {e.vida:>5} | {espada:>6.0f} {e.vida / espada:>6.1f} | {magia_final:>5.0f} | {leva:>5.0f} {h.vida / leva:>6.1f} golpes")
