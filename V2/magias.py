from util import calcular_dano

class magias:
    def __init__(self,id, nome, dano, custo, requisito):
        self.id = id
        self.nome = nome
        self.dano = dano
        self.custo = custo
        self.requisito = requisito

    def mostrarmagias(self, heroi):
        print(f"Dano: {int(self.dano + heroi.manamax * 0.3)}")
        print(f"Custo MP: {self.custo}")

def usarmagia(heroi, inimigo):
    if not heroi.magiasaprendidas:
        print("Você ainda não aprendeu nenhuma magia.")
        input("Pressione ENTER para continuar...")
        return False

    heroi.mostrarmagias()

    escolha = input("Digite o N* da magia que deseja usar, ou 0 para não fazer nada\n").strip()

    if escolha == "0":
        print("Você não faz nada...")
        input("Pressione ENTER para continuar...")
        return False

    if not escolha.isdigit():
        print("Digite um número válido.")
        input("Pressione ENTER para continuar...")
        return False

    indice = int(escolha) - 1

    if not (0 <= indice < len(heroi.magiasaprendidas)):
        print("ID da Magia inválida")
        input("Pressione ENTER para continuar...")
        return False

    magia = heroi.magiasaprendidas[indice]

    if heroi.mana < magia.custo:
        print("Você não tem MP suficiente.")
        input("Pressione ENTER para continuar...")
        return False

    heroi.mana -= magia.custo
    danobruto = magia.dano + heroi.manamax * 0.3
    ataquefinal = calcular_dano(danobruto, inimigo.defesa_magica)      #magia é reduzida pela resistência mágica
    inimigo.vida -= ataquefinal
    print(f"Você causou {ataquefinal} de dano em {inimigo.nome}")
    input("Pressione ENTER para continuar...")
    return True

listamagias = [
    # Nome, Dano, Custo MP, Nível Requisito
    magias("1", "Chamas de Fogo", 22, 18, 2),
    magias("2", "Espinho de Gelo", 45, 30, 4),
    magias("3", "Bola de fogo", 75, 48, 6),
    magias("4", "Relâmpago Arcano", 115, 68, 10),
    magias("5", "Cometa Sombrio", 160, 95, 14),
]

magia_boss = [
    magias("3", "Chamas do Dragão", 99, 70, "Após Derrotar um boss"),           # Será recebida após lutar contra 1 boss
    magias("9", "Forma do Caos", 10000, 1, "Oculto"),   # Magia secreta, comprada ou adquirida depois de certo requisito
]
