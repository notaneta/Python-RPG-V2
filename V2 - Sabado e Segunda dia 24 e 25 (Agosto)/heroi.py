from util import limpar_tela

class Personagem:

    def __init__(self, nome, vida, ataque, defesa, mana, ouro, nivel, xp, xplevel, foco):

        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.manamax = mana
        self.ouro = ouro
        self.nivel = nivel
        self.xp = xp
        self.xplevel = xplevel
        self.foco = foco
        self.focomax = 100
        self.focogen = 1        # Gerador de furia aumenta conforme derrota chefes ou eventos rolam, ou até mesmo lugar para aumentar
        # O inventário vazio, é uma lista de objetos
        self.inventario = []
        self.magiasaprendidas = []
        self.habilidadesaprendidas = []

    def mostrar_status(self):
        print(f"============ {self.nome.upper()} ============")
        print(f"Vida: {self.vida}/{self.vidamax}   Mana: {self.mana}/{self.manamax}")
        print(f"Ataque: {self.ataque}      Defesa: {self.defesa}")
        print(f"Ouro: {self.ouro}        Nível: {self.nivel}")    

    def subirnivel(self, listahabilidades, listamagias): 
        from habilidades import listahabilidades
        from magias import listamagias
        while self.xp >= self.xplevel:
            self.vidamax = int(self.vidamax * 1.15)
            self.vida = self.vidamax      # Recupera vida toda ao subir de level
            self.manamax = int(self.manamax * 1.15)
            self.mana = self.manamax      # Recupera mana toda ao subir de level
            self.ataque = int(self.ataque * 1.05)
            self.xp -= self.xplevel
            self.nivel += 1
            self.xplevel = int(self.xplevel * 1.5)

            limpar_tela()
            print(f"\nParabéns você subiu para o nivel {self.nivel}!")
            input("Pressione ENTER para continuar...")
            for skill in listahabilidades:
                if skill.requisito <= self.nivel and skill not in self.habilidadesaprendidas:   # Para cada SKILL que o requisito estiver acima ou igual o nivel do heroi, adicionar ela para o heroi
                    self.aprenderhabilidade(skill)        
                    print(f"Você aprendeu a habilidade {skill.nome}")
                    input("Pressione ENTER para continuar...")
            for magia in listamagias:
                if magia.requisito <= self.nivel and magia not in self.magiasaprendidas:  # Além disso verifica se a magia ou skill já não foi aprendida, para evitar duplicidade
                    self.aprendermagia(magia)
                    print(f"Você aprendeu a habilidade {magia.nome}")
                    input("Pressione ENTER para continuar...")
                                
            self.mostrar_status()
            input("Pressione ENTER para continuar...")
        
    def adicionar_pocoes(self, novo_item):
        # Verifica se o item já existe na lista pelo nome
        for item in self.inventario:
            if item.nome == novo_item.nome:
                item.quantidade += novo_item.quantidade
                print(f"O item {novo_item.nome} foi adicionado no seu inventário")
                return
        # Se for um item inédito, adiciona a instância na lista
        self.inventario.append(novo_item)
        print(f"\nNovo item obtido: {novo_item.nome}!")

    def removeritem(self, item_removido):
        for item in self.inventario:
            if item.nome == item_removido and item.quantidade > 0:
                item.quantidade -= 1
                if item.quantidade == 0:
                    self.inventario.remove(item)
                return

    def mostrar_inventario_pocoes(self):   
        """Exibe todos os itens que o personagem possui."""
        print(f"\n========== INVENTÁRIO DE {self.nome.upper()} ==========")
        if not self.inventario:
            print("Seu inventário está vazio.")
            print("==========================================")
            return
        for i, item in enumerate(self.inventario, start=1):
            print(
                f"{i} - {item.nome:<18} | Qtd: x{item.quantidade:<2} | {item.descricao}")

        print("==========================================")

    def aprendermagia(self, nova_magia):
        self.magiasaprendidas.append(nova_magia)
        print(f"\nNova Magia aprendida: {nova_magia.nome}!")

    def mostrarmagias(self):   
        """Exibe todas as magias que o personagem possui."""
        print(f"\n========== MAGIAS DE {self.nome.upper()} ==========")
        if not self.magiasaprendidas:
            print("Você não tem nenhuma magia.")
            print("==========================================")
            return
        for i, magia in enumerate(self.magiasaprendidas, start=1):
            print(
                f"{i} - {magia.nome:<18} | Dano: {magia.dano:<2} | MP {magia.custo}")

        print("==========================================")

    def aprenderhabilidade(self, nova_habilidade):
        self.habilidadesaprendidas.append(nova_habilidade)
        print(f"\nNova Magia aprendida: {nova_habilidade.nome}!")

    def mostrarSkill(self):   
        """Exibe todas as habilidade que o personagem possui."""
        print(f"\n========== HABILIDADES DE {self.nome.upper()} ==========")
        if not self.habilidadesaprendidas:
            print("Você não tem nenhuma habilidade.")
            print("==========================================")
            return
        for i, skill in enumerate(self.habilidadesaprendidas, start=1):
            print(
                f"{i} - {skill.nome:<18} | Dano: {skill.dano:<2} | MP {skill.custo}")

        print("==========================================")

    def equipar_nova_arma():
        print

    def atacar(self, inimigo):
        print(f"\nVoce ataca o {inimigo.nome} com sua espada e causa {self.ataque} de dano.")
        inimigo.vida -= self.ataque
        input("\nPressione ENTER para continuar...")

    

class Heroi(Personagem):
    def __init__(self, nome):   #  nome, vida, ataque, defesa, mana, ouro, nivel, xp, xplevel, foco):
        super().__init__(nome, 100, 50, 0, 40, 20, 1, 0, 40, 0) # Herdou os parametros de personagem / Aqui já configuro os status inicias também
