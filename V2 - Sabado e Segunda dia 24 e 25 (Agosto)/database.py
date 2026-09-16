import sqlite3
from heroi import Heroi

# conexao = sqlite3.connect("rpg.db")
# cursor = conexao.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS heroi (
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         nivel INTEGER,
#         vida INTEGER,
#         vidamax INTEGER,
#         mana INTEGER,
#         manamax INTEGER,
#         ouro INTEGER,
#         xp INTEGER,
#         ataque INTEGER,
#         defesa INTEGER,
#         foco INTEGER
#     )
# """)

# conexao.commit()
# conexao.close()


def salvar_heroi(heroi):

    conexao = sqlite3.connect("rpg.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM heroi WHERE id = ?",
        (1,)
    )

    save = cursor.fetchone()

    if save is None:            # verifica se já foi criado algum save, caso já, ele só atualiza em baixo

        cursor.execute("""
            INSERT INTO heroi (
                id,
                nome,
                nivel,
                vida,
                vidamax,
                mana,
                manamax,
                ouro,
                xp,
                ataque,
                defesa,
                foco
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            heroi.foco
        ))

    else:

        cursor.execute("""
            UPDATE heroi
            SET
                nome = ?,
                nivel = ?,
                vida = ?,
                vidamax = ?,
                mana = ?,
                manamax = ?,
                ouro = ?,
                xp = ?,
                ataque = ?,
                defesa = ?,
                foco = ?
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
            1
        ))

    conexao.commit()
    conexao.close()

def carregar_heroi():

    conexao = sqlite3.connect("rpg.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            nome,
            nivel,
            vida,
            vidamax,
            mana,
            manamax,
            ouro,
            xp,
            ataque,
            defesa,
            foco
        FROM heroi
        WHERE id = ?
    """, (1,))

    dados = cursor.fetchone()

    conexao.close()

    if dados is None:
        return None

    heroi = Heroi(dados[0])

    heroi.nivel = dados[1]
    heroi.vida = dados[2]
    heroi.vidamax = dados[3]
    heroi.mana = dados[4]
    heroi.manamax = dados[5]
    heroi.ouro = dados[6]
    heroi.xp = dados[7]
    heroi.ataque = dados[8]
    heroi.defesa = dados[9]
    heroi.foco = dados[10]

    return heroi