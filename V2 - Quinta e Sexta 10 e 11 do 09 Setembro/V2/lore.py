import time
from eventos import evento4_concluido


def dialogo(texto):

    for letra in texto:

        print(letra, end="", flush=True)

        if letra in [".", "!", "?"]:
            time.sleep(0.3)     # Pausa automatica nos pontos.
        else:
            time.sleep(0.03)

    print()


def boss_final_dialogo():
    from combate import ativar_acampamento
    ativar_acampamento
    print("Você atravessa o salão do trono.")
    dialogo("O castelo está em silêncio.")
    print("Uma figura sentada em um trono negro observa sua chegada.\n")
    dialogo("??? Então você finalmente chegou...")
    dialogo("Derrotou meus generais.")
    dialogo("Sobreviveu às montanhas geladas.")
    dialogo("Mas ainda não compreendeu a verdade deste mundo.")
    escolha = input("\n1 - Quem é você? \n2 - Eu vim acabar com isso.\nOque fazer?\n")

    if escolha == "1":
        dialogo("Rei do Caos: Eu sou o último rei. O último governante. O último homem que acreditou que este mundo poderia ser salvo.")
        dialogo("Rei do Caos: Olhe ao seu redor.\nEsta destruição não foi causada por monstros.\nFoi causada por pessoas.\nGanância.\nMedo.\nTraição.")
        dialogo("Rei do Caos: Eu apenas aceitei aquilo que todos tentavam esconder.\nO caos é a verdadeira natureza deste mundo.")
        dialogo("Rei do Caos: E agora...\nMostre-me.\nVocê é diferente dos que vieram antes?\nOu apenas mais um herói fadado ao fracasso?")
    elif escolha == "2":
        dialogo("Mostre-me.\nVocê é diferente dos que vieram antes?\nOu apenas mais um herói fadado ao fracasso?")

    print("O Rei do Caos se levanta do trono.\nUma energia sombria preenche o salão.\nA batalha final começa!")
    input("Pressione ENTER para continuar...")
    ativar_acampamento = False

def boss_final_dialogo_2():
    if evento4_concluido:
        print("Vejo que enfrentou seu reflexo.\nPoucos conseguem derrotar a si mesmos.\nTalvez exista esperança para este reino...")
        print("A sombra derrotada anteriormente surge.\nO Rei do Caos começa a rir.")
        dialogo("Você ainda não entendeu.\nEu não sou o caos.\nEu sou apenas suas correntes.")
        print("A energia do castelo explode.\nO Rei do Caos e a Sombra somem, e derrepente um portal aparece...")
        print("Você deverá segui-los para acabar com tudo de uma vez por todas!")
        print("Nova área desbloqueada:")
    else:
        print("Você continua fugindo.\nAté de si mesmo.")
        print("O Rei do caos cai ao chão do castelo.\nVocê impediu que o mundo caisse em trevas, mas um dia o ciclo irá retornar... FIM?")

def copia_heroi_dialogo(heroi, boss):
    print("Um espelho quebrado chama sua atenção.\nVocê vê seu reflexo...\nMas ele não imita seus movimentos.")
    print("A imagem atravessa o espelho.\nUma versão distorcida de você surge diante de seus olhos.")
    dialogo(f"????: ????:Você realmente acredita que chegou até aqui por mérito próprio?\nDiga-me...\nQuantos monstros você matou para ser chamado de herói>")
    print("Uma cópia sua emerge das sombras...")
    input("Pressione ENTER para continuar...")

def copia_heroi_dialogo2(heroi, boss):
     print("A sombra começa a desaparecer...")
     dialogo('Você conseguiu superar a se mesmo...\nEntão, talvez você tenha chance contra "ele"...')
     print("A sombra sumiu")
