# pip install pillow
# Teste inicio para v3

import os
import tkinter as tk
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imagens")

class RPG:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu RPG")
        self.root.geometry("800x700")
        self.root.configure(bg="black")

        # ----- Cena (imagem) -----
        self.label_imagem = tk.Label(root, bg="black")
        self.label_imagem.pack(pady=10)

        # ----- Histórico de texto (tipo o console do terminal) -----
        self.historico = tk.Text(
            root, height=10, width=80,
            bg="black", fg="white",
            font=("Consolas", 11),
            state="disabled",     # começa só leitura
            wrap="word"
        )
        self.historico.pack(pady=5)

        # ----- Campo de entrada -----
        frame_input = tk.Frame(root, bg="black")
        frame_input.pack(pady=5)

        tk.Label(frame_input, text=">", fg="lime", bg="black",
                 font=("Consolas", 12, "bold")).pack(side="left")

        self.entrada = tk.Entry(
            frame_input, width=70,
            bg="black", fg="lime",
            insertbackground="lime",   # cor do cursor
            font=("Consolas", 12),
            relief="flat"
        )
        self.entrada.pack(side="left", padx=5)
        self.entrada.focus()  # já começa com foco

        # Enter dispara o comando
        self.entrada.bind("<Return>", self.processar_comando)

        # ----- Estado do jogo -----
        self.cena_atual = "vila"
        self.imagens = {
            "vila": "imagens/zona1_vilapixel.jpg",
            "vila2": "imagens/zona2_vilapixel.jpg",
            "vila3": "imagens/zona3_vilapixel.jpg",
            "vila4": "imagens/zona4_vilapixel.jpg",
            "loja": "imagens/zona1_loja.jpg",
            "loja2": "imagens/zona2_loja.jpg",
            "loja3": "imagens/zona3_loja.jpg",
            "loja4": "imagens/zona4_loja.jpg",
            "arena": "imagens/zona1_arena.jpg",
            "arena2": "imagens/zona2_arena.jpg",
            "arena3": "imagens/zona3_arena.jpg",
            "arena4": "imagens/zona4_arena.jpg",
            "arena5": "imagens/zona5_arena.jpg",
            "ferreiro": "imagens/zona1_ferreiro.jpg",
            "ferreiro2": "imagens/zona2_ferreiro.jpg",
            "ferreiro3": "imagens/zona3_ferreiro.jpg",
            "ferreiro4": "imagens/zona4_ferreiro.jpg",
            }

        # Começa o jogo
        self.escrever("=== Bem-vindo ao RPG ===")
        self.ir_para("vila")

    # ---------- Escrever no histórico ----------
    def escrever(self, texto):
        self.historico.configure(state="normal")
        self.historico.insert("end", texto + "\n")
        self.historico.see("end")   # rola automaticamente
        self.historico.configure(state="disabled")

    # ---------- Trocar cena ----------
    def ir_para(self, cena):
        self.cena_atual = cena
        try:
            img = Image.open(self.imagens[cena]).convert("RGB")
            img = img.resize((500, 300), Image.LANCZOS)
            foto = ImageTk.PhotoImage(img)
            self.label_imagem.configure(image=foto, text="")
            self.label_imagem.image = foto
        except Exception as e:
            print(f"[ERRO imagem {cena}]: {e}")
            self.label_imagem.configure(image="", text=f"[Falta: {cena}]", fg="red")
            self.label_imagem.image = None

        # Descrição + dicas
        descricoes = {
            "vila":     "Você está na vila. Comandos: 'loja', 'floresta'",
            "loja":     "Bem-vindo à loja! Comandos: 'comprar', 'voltar'",
            "floresta": "A floresta é perigosa. Comandos: 'lutar', 'voltar'",
        }
        self.escrever(descricoes.get(cena, ""))

    # ---------- Processar o que o jogador digitou ----------
    def processar_comando(self, event=None):
        comando = self.entrada.get().strip().lower()
        self.entrada.delete(0, "end")   # limpa o campo

        if not comando:
            return

        self.escrever(f"> {comando}")
        self.executar(comando)

    # ---------- Lógica dos comandos ----------
    def executar(self, comando):
        # Comandos globais
        if comando in ("ajuda", "help"):
            self.escrever("Comandos: loja - 1, floresta - 2, voltar - 0, comprar, lutar, sair")
            return

        if comando in ("sair", "exit"):
            self.escrever("Até a próxima aventura!")
            self.root.after(800, self.root.destroy)
            return

        # Comandos por cena
        if self.cena_atual == "vila":
            if comando in ("loja", "entrar loja"):
                self.ir_para("loja")
            elif comando in ("floresta", "ir floresta"):
                self.ir_para("floresta")
            else:
                self.escrever("Não entendi. Tente 'loja' ou 'floresta'.")

        elif self.cena_atual == "loja":
            if comando in ("comprar", "comprar pocao", "poção"):
                self.escrever("Você comprou uma poção! (-10 de ouro)")
            elif comando == "voltar":
                self.ir_para("vila")
            else:
                self.escrever("Comandos: 'comprar' ou 'voltar'.")

        elif self.cena_atual == "arena":
            if comando == "lutar":
                self.escrever("Você derrotou um goblin! (+20 XP)")
            elif comando == "voltar":
                self.ir_para("vila")
            else:
                self.escrever("Comandos: 'lutar' ou 'voltar'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPG(root)
    root.mainloop()
    