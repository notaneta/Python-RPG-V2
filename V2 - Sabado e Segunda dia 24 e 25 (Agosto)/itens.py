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
    heroi.mostrar_inventario_pocoes()
    escolha = input("Digite o número do item que deseja usar ou digite 0 para sair...")
    for item in heroi.inventario:
        if escolha == item.id:
            escolha = item
            heroi.removeritem(escolha)
            heroi.vida += min(heroi.vidamax, heroi.vida + item.cura)
            print(f"O item {item.nome} foi usado e curou {item.cura} da sua vida")

class Espadas:
    def __init__(self, id, nome, descricao, dano, custo):
        self.id = id
        self.nome = nome
        self.descrição = descricao
        self.dano = dano
        self.custo = custo

    def equipar_espada(self, heroi):
        item = item
        heroi.ataque += item

    def mostraritens(self):
        print(f"Item: {self.nome} N* {self.id}")
        print(f"descrição: {self.descricao}")
        print(f"dano: {self.dano}")
        print(f"custo: {self.custo}")



ferreiro_espadas = [ # id, nome, descricao, dano, custo):
    Espadas("1", "Espada de Ferro", "Espada Básica de Ferro, muito útil na maioria dos casos", 12, 40),
    Espadas("2", "Espada de Aço", "Espada de Aço", 12, 40),
    Espadas("3", "Espada Reforçada", "Espada Reforçada", 12, 40),
    Espadas("4", "Espada do Cavaleiro", "Espada do Cavaleiro", 12, 40),
    
]


# Mana irá recuperar ao subir de nível