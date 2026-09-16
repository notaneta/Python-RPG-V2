class foco:
    def __init__(self,id, nome, dano, requisito):
        self.id = id
        self.nome = nome
        self.dano = dano
        self.requisito = requisito

    def mostrarskill(self):
        print("============ Habilidades ============")
        print(f"Habilidade: {self.nome}")
        print(f"Dano: {self.dano}")
        print(f"Uso de Foco: {self.custo}")
        print(f"Requisitos: {self.requisito}")

def usarfoco(heroi, inimigo):
        heroi.mostrarskill()
        escolha = input("Digite o N(ID) da magia que deseja usar, ou 0 para não fazer nada: ")
        for habilidade in heroi.habilidadesaprendidas:
            if habilidade.id == escolha:
                heroi.foco = 0
                inimigo.vida -= habilidade.dano
                print(f"Você causou {habilidade.dano} no {inimigo.nome}")
                
            elif escolha == 0:
                print("Você não faz nada...")
                input("Pressione ENTER para continuar...")
                turnojogador = False                                # Tentativa do turno do jogador não ser pulado caso não faça nada por não ter MP, ou desistir de usar magia

            else:
                print("ID da Magia invalida")
                input("Pressione ENTER para continuar...")

listahabilidades = [ # Nome , Dano, Custo MP, requisito/nivel
foco("1", "Chamas de Fogo", 35, "Nivel 3"),       
foco("2", "Golpe da Espada Flamejante", 60, "Nivel 9"),   
foco("3", "Chamas do Dragão", 99, "Após Derrotar um boss"),           # Será recebida após lutar contra 1 boss
foco("9", "Forma do Caos", 10000, "Oculto"),   # Magia secreta, comprada ou adquirida depois de certo requisito
]
