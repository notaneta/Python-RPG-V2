# Poção de Cura
class Pocao:
    def __init__(self, id, nome, cura, custo, quantidade, descricao):
        self.id = id
        self.nome = nome
        self.cura = cura
        self.custo = custo
        self.quantidade = quantidade
        self.descricao = descricao

    def mostraritens(self):
        print(f"Item: {self.nome} N* {self.id}")
        print(f"Cura: {self.cura}")
        print(f"Custo: {self.custo}")
        print(f"Descrição: {self.descricao}")

poçoes = [
    Pocao("1", "Poção Pequena", 20, 15, 1, "Cura uma pequena parte da vida"),
    Pocao("2","Poção Média", 45, 30, 1, "Cura media da sua vida"),
    Pocao("3", "Poção Grande", 75, 50, 1, "Cura grande parte da sua vida"),
]

def usaritem(heroi):
    print("Qual item do seu inventário usar?")
    heroi.mostrarinventario()
    escolha = input("Digite o número do item que deseja usar ou digite 0 para sair...")
    for item in heroi.inventario:
        if escolha == item.id:
            escolha = item
            heroi.removeritem(escolha)
            heroi.vida += min(heroi.vidamax, heroi.vida + item.cura)
            print(f"O item {item.nome} foi usado e curou {item.cura} da sua vida")
             


# Mana irá recuperar ao subir de nível