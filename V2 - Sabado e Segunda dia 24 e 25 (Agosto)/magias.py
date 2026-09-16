class magias:
    def __init__(self,id, nome, dano, custo, requisito):
        self.id = id
        self.nome = nome
        self.dano = dano
        self.custo = custo
        self.requisito = requisito

    def mostrarmagias(self):
        print("============ MAGIAS ============")
        print(f"Magia: {self.nome}")
        print(f"Dano: {self.dano}")
        print(f"Custo MP: {self.custo}")
        print(f"Requisitos: {self.requisito}")

def usarmagia(heroi, inimigo):
        heroi.mostrarmagias()
        escolha = input("Digite o N(ID) da magia que deseja usar, ou 0 para não fazer nada: ")
        for magia in heroi.magiasaprendidas:
            if magia.id == escolha:
                if heroi.mana >= magia.custo:
                    inimigo.vida -= magia.dano
                    print(f"Você causou {magia.dano} no {inimigo.nome}")
                else:
                    print("Você não tem MP suficiente...")
                    input("Pressione ENTER para continuar...")
                
            elif escolha == 0:
                print("Você não faz nada...")
                input("Pressione ENTER para continuar...")
                turnojogador = False                                # Tentativa do turno do jogador não ser pulado caso não faça nada por não ter MP, ou desistir de usar magia

            else:
                print("ID da Magia invalida")
                input("Pressione ENTER para continuar...")

listamagias = [ # Nome , Dano, Custo MP, requisito/nivel
    magias("1", "Chamas de Fogo", 35, 20, 2),       
    magias("2", "Golpe da Espada Flamejante", 60, 34, 6),   
]

magia_boss = [
    magias("3", "Chamas do Dragão", 99, 70, "Após Derrotar um boss"),           # Será recebida após lutar contra 1 boss
    magias("9", "Forma do Caos", 10000, 1, "Oculto"),   # Magia secreta, comprada ou adquirida depois de certo requisito
]
