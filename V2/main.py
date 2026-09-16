from telas import menujogo
from heroi import Heroi
from database import menu_principal, criar_banco
from util import limpar_tela, Cores

criar_banco()               # <- chama AQUI, antes de tudo
limpar_tela()
heroi = menu_principal()
if heroi is None:
    limpar_tela()

LARGURA = 54


def _cabecalho(titulo):
    print(f"{Cores.CIANO}╔" + "═" * LARGURA + f"╗{Cores.RESET}")
    print(f"{Cores.CIANO}║{Cores.RESET}" + f"{titulo.center(LARGURA)}" + f"{Cores.CIANO}║{Cores.RESET}")
    print(f"{Cores.CIANO}╚" + "═" * LARGURA + f"╝{Cores.RESET}")

def intro(heroi):
    limpar_tela()
    _cabecalho("RPG OVERWORLD 2")
    print()
    print(f"  Bem-vindo, {Cores.VERDE}{heroi.nome}{Cores.RESET}.")
    print()
    print(f"  Você foi {Cores.AMARELO}invocado{Cores.RESET} para outro mundo com uma missão:")
    print(f"  {Cores.VERMELHO}salvar este mundo das forças do Rei do Caos.{Cores.RESET}")
    print()
    print("  Antes de começar sua jornada, leia atentamente")
    print("  as regras e informações abaixo.")
    print()

def mostrar_tutorial(heroi):
    # ---------- Tela 1: Objetivo ----------
    limpar_tela()
    _cabecalho("REGRAS E INFORMAÇÕES")
    print()
    print(f"  {Cores.AMARELO}Objetivo principal:{Cores.RESET}")
    print("  Avance pelas áreas do mundo, enfrente seus inimigos")
    print("  e derrote os chefes que bloqueiam seu progresso.")
    print()
    print(f"  {Cores.AMARELO}Total de áreas:{Cores.RESET} 4 áreas principais")
    print()
    print(f"  {Cores.AMARELO}Objetivo final:{Cores.RESET} Chegue até a 4ª área e enfrente o Boss Final.")
    print()
    input("  Pressione ENTER para continuar...")

    # ---------- Tela 2: Combate ----------
    limpar_tela()
    _cabecalho("SISTEMA DE COMBATE")
    print()
    print(f"  {Cores.VERDE}•{Cores.RESET} Derrote {Cores.AMARELO}5 inimigos{Cores.RESET} para liberar a batalha contra o chefe da área.")
    print(f"  {Cores.VERDE}•{Cores.RESET} Derrotar o chefe permite que você progrida para a próxima área.")
    print(f"  {Cores.VERDE}•{Cores.RESET} Chefes possuem habilidades especiais que podem mudar o rumo da batalha.")
    print(f"  {Cores.VERDE}•{Cores.RESET} {Cores.VERMELHO}Chefes Especiais{Cores.RESET} podem ser encontrados após derrotar o 1º chefe da área.")
    print(f"  {Cores.VERDE}•{Cores.RESET} Chefes Especiais são bem mais rigorosos, porém recompensam com algo valioso.")
    print()
    input("  Pressione ENTER para continuar...")

    # ---------- Tela 3: Status ----------
    limpar_tela()
    _cabecalho("SEUS STATUS")
    print()
    heroi.mostrar_status()
    print()
    input("  Pressione ENTER para continuar...")

    # ---------- Tela 4: Despedida ----------
    limpar_tela()
    _cabecalho("SUA JORNADA COMEÇA AGORA")
    print()
    print(f"  As forças do {Cores.VERMELHO}Rei do Caos{Cores.RESET} estão avançando,")
    print(f"  e somente {Cores.VERDE}você{Cores.RESET} poderá impedir que este mundo seja destruído.")
    print()
    print(f"  {Cores.AMARELO}Prepare-se. Explore. Evolua. Lute.{Cores.RESET}")
    print()
    print(f"  Boa sorte, herói.")
    print()
    input("  Pressione ENTER para iniciar sua jornada...")

def main():
    limpar_tela()

    # Cabeçalho inicial
    _cabecalho("RPG OVERWORLD 2")
    print()
    nome = input("  Digite seu nome: ").strip()
    if not nome:
        nome = "Herói"

    jogador = Heroi(nome)

    # Introdução
    intro(jogador)

    # Pergunta do tutorial
    while True:
        resposta = input("  Deseja ler o rápido tutorial? (s/n): ").strip().lower()
        if resposta == "s":
            mostrar_tutorial(jogador)
            break
        elif resposta == "n":
            print()
            print(f"  {Cores.CINZA}Sem problemas. Boa sorte, {jogador.nome}.{Cores.RESET}")
            input("  Pressione ENTER para continuar...")
            break
        else:
            print(f"  {Cores.VERMELHO}Comando inválido.{Cores.RESET} Digite 's' ou 'n'.")

    # Entra no jogo
    menujogo(jogador)

# Ponto de entrada
if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        input("\nPressione Enter para sair...")


# Posteriormente fazer um seletor de DIFICULDADE no V2.5 
# Quando for fazer o EQUIPAMENTO de armaduras e espadas no inventário, fazer a remoção do valor de ataque do item no jogador e somar pelo do novo
# Refatorando TODA a parte de itens, pois para usar pocoes, armaduras e armas no mesmo inventário, vou precisar criar uma classe somente para itens ele como modelo para outros
# Nova ideia de teste para INVENTÁRIO, criar um só porém nele usar filtros para pesquisa de itens no comando de exibição
# Acho que deixarei isso para o V2 
# E deixaria o Boss Rush para uma atualização futura, talvez: Arena dos Campeões ou Modo Desafio
# Fazer sistema em algumas batalhas opcionais o boss não te mata e só vai embora (sistema de game over que só funciona nas batalhas principais por exemplo)
# Poder voltar em vilas antigas



#                               FAZER EM CASA
# Ir colocando o LIMPAR TELA junto com o input("Pressione ENTER para continuar...") para deixar o jogo limpo e visivel sem pular qualquer info importante
# Fazer um ranking online de quem terminou mais forte / ou pontos acumulados e com os bosses derrotados 
# Logica (Evento da vila -> Luta contra sombra -> Se DERROTOU: Boss final VERDADEIRO é liberado , Else: Final falso é liberado # Boss secreto da zona não existe)
# Talvez criar mais poções uma para cada região e amuletos também
# # Dialogo do boss final é executado durante a verificação do mundo / NAO MOSTRA BUGADO



# Criado sistema de save de eventos realizados , resolvidos diversos bugs
# Criei final verdadeiro e final (TESTAR EM CASA SE FUNCIONOU)

# Criado todos os eventos de vila, falta apenas testar (TESTAR EM CASA SE FUNCIONOU)
# USAR POÇÃO agora é com enumerate (TESTAR EM CASA SE FUNCIONOU)
# Acho que com o IF na opção de TELAS, onde ele verifica a ultima vila ele provavelmente deve barra o jogador de acessar a vila (TESTAR EM CASA SE FUNCIONOU)
# TESTE DE VENENO na habilidade do boss especial aranha, e 2 habilidades em 1 boss (TESTAR EM CASA SE FUNCIONOU)
# TESTAR habilidade do boss de gelo    efeito STUN no combate  (TESTAR EM CASA SE FUNCIONOU)
# Testar contador de stun da HUD (TESTAR EM CASA SE FUNCIONOU)