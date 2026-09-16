import os
import shutil


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[H\033[J", end="")

# Descobrir e alinha HUD
largura = shutil.get_terminal_size().columns

# pip install colorama

from colorama import Fore, Style, init

init()

def barra_hp(valor, maximo):
    tamanho = 20
    preenchido = int((valor / maximo) * tamanho)
    vazio = tamanho - preenchido
    porcentagem = valor / maximo
    if porcentagem >= 0.7:
        cor = Fore.GREEN

    elif porcentagem >= 0.3:
        cor = Fore.YELLOW

    else:
        cor = Fore.RED

    return (cor +"█" * preenchido + Style.RESET_ALL + "-" * vazio)

def barra_mp(valor, maximo):
    tamanho = 20
    preenchido = int((valor / maximo) * tamanho)
    vazio = tamanho - preenchido
    return (Fore.BLUE +"█" * preenchido + Style.RESET_ALL +"-" * vazio)

def barra_furia(valor, maximo):
    tamanho = 20
    preenchido = int((valor / maximo) * tamanho)
    vazio = tamanho - preenchido
    return (Fore.MAGENTA + "█" * preenchido + Style.RESET_ALL + "-" * vazio)




# Depois Colocar SAVE E LOAD do jogo antes de entrar no jogo 

# Ideia possivel depois de colocar ELEMENTOS 
# Fogo -> Forte contra Terra
# Água -> Forte contra Fogo
# Terra -> Forte contra Raio

# Golpes ou especiais baseado em energia estilo FF 7

#Golpe Devastador
# cooldown = 3 turnos ou precisa de energia para usar

# Inimigo - pode se curar ou usar uma habildade dele 

# Buffs
# Força Heroica
# +50% ataque
# 3 turnos

# Efeito de sangramento, veneno, etc