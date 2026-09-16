# criar_banco.py
import sqlite3, copy
from heroi import Heroi
import progresso
import vilas
from caminhos import CAMINHO_BANCO


# Tabela do herói   /   Caso adicionar mais coisas tenho que apagar o banco de dados anterior 
def criar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS heroi (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        nivel INTEGER,
        vida INTEGER,
        vidamax INTEGER,
        mana INTEGER,
        manamax INTEGER,
        ouro INTEGER,
        xp INTEGER,
        ataque INTEGER,
        defesa INTEGER,
        foco INTEGER,
        focogen INTEGER,
        vila_atual TEXT,
        zona_atual TEXT,
        zona_progresso INTEGER DEFAULT 0,
        zona_boss_derrotado INTEGER DEFAULT 0,
        zona_boss_especial INTEGER DEFAULT 0,
        final_verdadeiro INTEGER DEFAULT 0,
        item_raid_vila INTEGER DEFAULT 0,
        dialogo2_boss INTEGER DEFAULT 0
        
    )
""")

    # Tabela do inventário (poções)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heroi_id INTEGER,
            nome TEXT,
            quantidade INTEGER,
            FOREIGN KEY (heroi_id) REFERENCES heroi(id)
        )
    """)

    # Tabela de magias aprendidas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magias_heroi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heroi_id INTEGER,
            nome TEXT,
            FOREIGN KEY (heroi_id) REFERENCES heroi(id)
        )
    """)

    # Tabela de habilidades aprendidas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habilidades_heroi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heroi_id INTEGER,
            nome TEXT,
            FOREIGN KEY (heroi_id) REFERENCES heroi(id)
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos_heroi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heroi_id INTEGER,
        nome_evento TEXT,
        concluido INTEGER DEFAULT 0,
        FOREIGN KEY (heroi_id) REFERENCES heroi(id)
    )
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ferreiro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heroi_id INTEGER,
        nome TEXT,
        FOREIGN KEY (heroi_id) REFERENCES heroi(id)
    )
""")

    conexao.commit()
    conexao.close()

if __name__ == "__main__":      # O if __name__ == "__main__": faz o código rodar só quando você executa o arquivo diretamente (python criar_banco.py), e não quando ele é importado (from criar_banco import salvar_heroi)
    criar_banco()
    print("Banco criado!")      


def salvar_heroi(heroi):
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    # --- 1) Salva os atributos do herói (INSERT ou UPDATE) ---
    cursor.execute("SELECT id FROM heroi WHERE id = ?", (1,))
    save = cursor.fetchone()

    if save is None:
        cursor.execute("""
            INSERT INTO heroi (
                id, nome, nivel, vida, vidamax, mana, manamax,
                ouro, xp, ataque, defesa, foco, focogen, vila_atual, zona_atual
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
                    1,
                    heroi.nome,
                    heroi.nivel,
                    heroi.vida,
                    heroi.vidamax,
                    heroi.mana,
                    heroi.manamax,
                    heroi.ouro,
                    heroi.xp,
                    heroi.ataque,
                    heroi.defesa,
                    heroi.foco,
                    heroi.focogen,
                    getattr(heroi.vila_atual, "nome", None),
                    getattr(heroi.zona_atual, "nome", None),        # getattr(objeto, "atributo", padrão) devolve None se o objeto for None ou não tiver o atributo. Sem quebrar.
                        ))
    else:
        cursor.execute("""
            UPDATE heroi
            SET nome = ?, nivel = ?, vida = ?, vidamax = ?,
                mana = ?, manamax = ?, ouro = ?, xp = ?,
                ataque = ?, defesa = ?, foco = ?, focogen = ?,
                vila_atual = ?, zona_atual = ?
            WHERE id = ?
        """, (
                    heroi.nome,
                    heroi.nivel,
                    heroi.vida,
                    heroi.vidamax,
                    heroi.mana,
                    heroi.manamax,
                    heroi.ouro,
                    heroi.xp,
                    heroi.ataque,
                    heroi.defesa,
                    heroi.foco,
                    heroi.focogen,
                    getattr(heroi.vila_atual, "nome", None),
                    getattr(heroi.zona_atual, "nome", None),
                    1
        ))

    # --- 2) Salva o inventário (limpa e recria — mais simples que comparar) ---
    cursor.execute("DELETE FROM inventario WHERE heroi_id = ?", (1,))
    for item in heroi.inventario:
        cursor.execute("""
            INSERT INTO inventario (heroi_id, nome, quantidade)
            VALUES (?, ?, ?)
        """, (1, item.nome, item.quantidade))

    # --- 3) Salva as magias ---
    cursor.execute("DELETE FROM magias_heroi WHERE heroi_id = ?", (1,))
    for magia in heroi.magiasaprendidas:
        cursor.execute("""
            INSERT INTO magias_heroi (heroi_id, nome)
            VALUES (?, ?)
        """, (1, magia.nome))

    # --- 4) Salva as habilidades ---
    cursor.execute("DELETE FROM habilidades_heroi WHERE heroi_id = ?", (1,))
    for skill in heroi.habilidadesaprendidas:
        cursor.execute("""
            INSERT INTO habilidades_heroi (heroi_id, nome)
            VALUES (?, ?)
        """, (1, skill.nome))
        
    # --- 5) Salva o progresso da zona ---
    zona = heroi.zona_atual
    cursor.execute("""
        UPDATE heroi
        SET zona_progresso = ?,
            zona_boss_derrotado = ?,
            zona_boss_especial = ?,
            final_verdadeiro = ?,
            item_raid_vila = ?,
            dialogo2_boss = ?
        WHERE id = ?
    """, (
        zona.progresso if zona else 0,
        int(zona.bossderrotado) if zona else 0,
        int(zona.boss_especial_derrotado) if zona else 0,
        int(progresso.final_verdadeiro),
        int(progresso.item_raid_vila),
        int(progresso.dialogo2_boss),
        1,
    ))

# --- 6) Salva as flags de eventos ---
    cursor.execute("DELETE FROM eventos_heroi WHERE heroi_id = ?", (1,))
    for nome, valor in progresso.flags_eventos.items():
        cursor.execute("""
            INSERT INTO eventos_heroi (heroi_id, nome_evento, concluido)
            VALUES (?, ?, ?)
        """, (1, nome, int(valor)))


    # Ferreiro
    cursor.execute("DELETE FROM ferreiro WHERE heroi_id = ?", (1,))
    todos_amuletos = (
        vilas.ferreiro_Amuletos_Ataque
        + vilas.ferreiro_Amuletos_Defesa
        + [a for lista in vilas.amuletos_ataque_exclusivos.values() for a in lista]
        + [a for lista in vilas.amuletos_defesa_exclusivos.values() for a in lista]
    )
    for item in todos_amuletos:
        cursor.execute("""
            INSERT INTO ferreiro (heroi_id, nome)
            VALUES (?, ?)
        """, (1, item.nome))

    conexao.commit()
    conexao.close()

def carregar_heroi():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT nome, nivel, vida, vidamax, mana, manamax,
           ouro, xp, ataque, defesa, foco, focogen,
           vila_atual, zona_atual
    FROM heroi
    WHERE id = ?
""", (1,))
    dados = cursor.fetchone()

    if dados is None:
        conexao.close()
        return None

    heroi = Heroi(dados[0])
    heroi.nivel    = dados[1]
    heroi.vida     = dados[2]
    heroi.vidamax  = dados[3]
    heroi.mana     = dados[4]
    heroi.manamax  = dados[5]
    heroi.ouro     = dados[6]
    heroi.xp       = dados[7]
    heroi.ataque   = dados[8]
    heroi.defesa   = dados[9]
    heroi.foco     = dados[10]
    heroi.focogen  = dados[11]

    nome_vila = dados[12]
    nome_zona = dados[13]

    # restaura vila
    if nome_vila:
        from vilas import vila_inicial, vila2_pescadores, vila3_gelada, vila4_destruida
        mapa_vilas = {
            vila_inicial.nome: vila_inicial,
            vila2_pescadores.nome: vila2_pescadores,
            vila3_gelada.nome: vila3_gelada,
            vila4_destruida.nome: vila4_destruida,
        }
        heroi.vila_atual = mapa_vilas.get(nome_vila, vila_inicial)

    # restaura zona
    if nome_zona:
        import mundo
        mapa_zonas = {
            mundo.zona1_floresta.nome: mundo.zona1_floresta,
            mundo.zona2_caverna.nome: mundo.zona2_caverna,
            mundo.zona3_montanhagelada.nome: mundo.zona3_montanhagelada,
            mundo.zona4_castelo_do_caos.nome: mundo.zona4_castelo_do_caos,
            mundo.zona5_abismo.nome: mundo.zona5_abismo,
        }
        # deepcopy pra não contaminar a instância global!
        heroi.zona_atual = copy.deepcopy(
            mapa_zonas.get(nome_zona, mundo.zona1_floresta))
    # --- 3) Restaura o inventário ---
    heroi.inventario = []                     # ← limpa antes
    cursor.execute("SELECT nome, quantidade FROM inventario WHERE heroi_id = ?", (1,))
    from itens import poçoes
    for nome_item, qtd in cursor.fetchall():
        for pocao in poçoes:
            if pocao.nome == nome_item:
                nova = copy.deepcopy(pocao)
                nova.quantidade = qtd
                heroi.inventario.append(nova)
                break

    # --- 4) Restaura as magias ---
    heroi.magiasaprendidas = []               # ← limpa antes
    cursor.execute("SELECT nome FROM magias_heroi WHERE heroi_id = ?", (1,))
    from magias import listamagias
    for (nome_magia,) in cursor.fetchall():
        for magia in listamagias:
            if magia.nome == nome_magia:
                heroi.magiasaprendidas.append(magia)
                break

    # --- 5) Restaura as habilidades ---
    heroi.habilidadesaprendidas = []          # ← limpa o que o __init__ pôs

    cursor.execute("SELECT nome FROM habilidades_heroi WHERE heroi_id = ?", (1,))
    from habilidades import listahabilidades
    for (nome_skill,) in cursor.fetchall():
        for skill in listahabilidades:
            if skill.nome == nome_skill:
                heroi.habilidadesaprendidas.append(skill)
                break
    
    # --- 5b) Restaura o progresso da zona ---
    cursor.execute("""
        SELECT zona_progresso, zona_boss_derrotado, zona_boss_especial,
            final_verdadeiro, item_raid_vila, dialogo2_boss
        FROM heroi
        WHERE id = ?
    """, (1,))
    prog = cursor.fetchone()

    if prog and heroi.zona_atual:
        heroi.zona_atual.progresso = prog[0] or 0
        heroi.zona_atual.bossderrotado = bool(prog[1])
        heroi.zona_atual.boss_especial_derrotado = bool(prog[2])
        progresso.final_verdadeiro = bool(prog[3])
        progresso.item_raid_vila = bool(prog[4])
        progresso.dialogo2_boss = bool(prog[5])

    # --- 6) Restaura as flags de eventos ---
    cursor.execute("""
        SELECT nome_evento, concluido FROM eventos_heroi WHERE heroi_id = ?
    """, (1,))
    for nome, valor in cursor.fetchall():
        if nome in progresso.flags_eventos:
            progresso.flags_eventos[nome] = bool(valor)


    # Ferreiro
    cursor.execute("SELECT nome FROM ferreiro WHERE heroi_id = ?", (1,))
    nomes_salvos = [linha[0] for linha in cursor.fetchall()]

    vilas.ferreiro_Amuletos_Ataque[:] = [i for i in vilas.ferreiro_Amuletos_Ataque if i.nome in nomes_salvos]
    vilas.ferreiro_Amuletos_Defesa[:] = [i for i in vilas.ferreiro_Amuletos_Defesa if i.nome in nomes_salvos]

    for chave, lista in vilas.amuletos_ataque_exclusivos.items():
        vilas.amuletos_ataque_exclusivos[chave] = [i for i in lista if i.nome in nomes_salvos]

    for chave, lista in vilas.amuletos_defesa_exclusivos.items():
        vilas.amuletos_defesa_exclusivos[chave] = [i for i in lista if i.nome in nomes_salvos]

    conexao.close()
    return heroi

def deletar_save():
    with sqlite3.connect(CAMINHO_BANCO) as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM inventario WHERE heroi_id = ?", (1,))
        cursor.execute("DELETE FROM magias_heroi WHERE heroi_id = ?", (1,))
        cursor.execute("DELETE FROM habilidades_heroi WHERE heroi_id = ?", (1,))
        cursor.execute("DELETE FROM eventos_heroi WHERE heroi_id = ?", (1,))
        cursor.execute("DELETE FROM heroi WHERE id = ?", (1,))

def menu_deletar():
    confirmar = input("Tem certeza? Isso apaga TUDO! (s/n): ")
    if confirmar.lower() == "s":
        deletar_save()
        print("Save apagado com sucesso!")
    else:
        print("Cancelado.")
    input("Pressione ENTER para continuar...")

def menu_principal():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM heroi WHERE id = ?", (1,))
    save = cursor.fetchone()
    conexao.close()

    if save is None:
        return None

    while True:
        escolha = input("Digite:\n[1] - Novo Jogo\n[2] - Carregar Jogo\n[3] - Deletar Save Existente\n")
        if escolha == "1":
            return None
        elif escolha == "2":
            heroi = carregar_heroi()
            if heroi:
                heroi.mostrar_status()
                input("Jogo carregado! Pressione ENTER para continuar...")
                from telas import menujogo
                menujogo(heroi)
                return heroi
            else:
                print("Erro ao carregar. Voltando ao menu...")
                continue
        elif escolha == "3":
            menu_deletar()
            # depois de deletar, reinicia o menu (o save pode ter sumido)
            return menu_principal()   # recursão simples
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")
    