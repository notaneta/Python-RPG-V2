class foco:
    def __init__(self,id, nome, dano, custo, requisito):
        self.id = id
        self.nome = nome
        self.dano = dano
        self.custo = custo
        self.requisito = requisito

    def mostrarskill(self):
        print(f"Habilidade: {self.nome}")
        print(f"Dano: {self.dano}")
        print(f"Uso de Foco: {self.custo}")
        print(f"Requisito: {self.requisito}")

def usarfoco(heroi, inimigo):
        heroi.mostrarSkill()
        escolha = input("Digite o N(ID) da magia que deseja usar, ou 0 para não fazer nada\n")
        print("============ Habilidades ============")
        for habilidade in heroi.habilidadesaprendidas:
            if habilidade.id == escolha:
                heroi.foco = 0
                ataquefinal = max(1, habilidade.dano - inimigo.defesa)
                inimigo.vida -= ataquefinal
                print(f"Você causou {ataquefinal} no {inimigo.nome}")
                return  True
                
            elif escolha == 0:
                print("Você não faz nada...")
                input("Pressione ENTER para continuar...")

            else:
                print("ID da Magia invalida")
                input("Pressione ENTER para continuar...")

listahabilidades = [
    # Id, Nome, Dano, Custo Foco, Nível
    foco("1", "Golpe Flamejante", 30, 25, 1),
    foco("2", "Corte Vorpal", 60, 40, 3),
    foco("3", "Lâmina do Dragão", 105, 60, 6),
    foco("4", "Impacto Símico", 150, 80, 8),
    foco("5", "Execução Divina", 210, 100, 10),
]

lista_habilidades_exclusivas = [
foco("3", "Corte Dimensional", 99, 100,"Após Derrotar um boss"),           # Será recebida após lutar contra 1 boss 
foco("9", "Multiplos Golpes", 10000, 100,"Oculto"),   # Magia secreta, comprada ou adquirida depois de certo requisito
]