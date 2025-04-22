import tkinter as tk
import random
from tkinter import messagebox

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Sorteio de Bingo")
        self.root.geometry("600x600")
        self.root.configure(bg="#F1F1F1")
        self.root.resizable(False, False)

        self.numeros = list(range(1, 76))
        random.shuffle(self.numeros)
        self.indice = 0

        self.letras = ['B', 'I', 'N', 'G', 'O']

        # Título
        self.titulo = tk.Label(root, text="🔔 Bingo Interativo!", font=("Arial", 18, "bold"),
                               bg="#F1F1F1", fg="#2D98DA")
        self.titulo.pack(pady=20)

        # Resultado sorteado
        self.resultado_label = tk.Label(root, text="Aperte o botão para sortear um número",
                                        font=("Helvetica", 14), fg="#2D98DA", bg="#F1F1F1")
        self.resultado_label.pack(pady=10)

        # Botão de sorteio
        self.sorteio_button = tk.Button(root, text="Sortear Número 🎱", font=("Helvetica", 12),
                                        bg="#2D98DA", fg="white", command=self.sortear_numero)
        self.sorteio_button.pack(pady=10)

        # Criação e exibição da tabela 5x5
        self.tabela_bingo = self.criar_tabela_bingo(root)
        self.tabela_bingo.pack(pady=20)

    def sortear_numero(self):
        if self.indice < len(self.numeros):
            numero = self.numeros[self.indice]
            self.indice += 1

            letra = self.letras[(numero - 1) // 15]
            resultado = f"🎱 {letra}-{numero}"

            self.resultado_label.config(text="Sorteando...")
            self.root.after(500, lambda: self.resultado_label.config(text=resultado))

            self.marcar_numero_na_tabela(numero)
        else:
            messagebox.showinfo("Fim", "Todos os números foram sorteados!")

    def criar_tabela_bingo(self, root):
        frame = tk.Frame(root, bg="#F1F1F1")
        self.bingo_buttons = {}

        colunas = {
            'B': random.sample(range(1, 16), 5),
            'I': random.sample(range(16, 31), 5),
            'N': random.sample(range(31, 46), 5),
            'G': random.sample(range(46, 61), 5),
            'O': random.sample(range(61, 76), 5),
        }

        for i, letra in enumerate(self.letras):
            label = tk.Label(frame, text=letra, font=("Arial", 14, "bold"),
                             bg="#2D98DA", fg="white", width=6, height=2, relief="solid")
            label.grid(row=0, column=i, padx=5, pady=5)

        for i, letra in enumerate(self.letras):
            for j in range(5):
                if letra == 'N' and j == 2:
                    button = tk.Button(frame, text="FREE", font=("Arial", 12),
                                       width=6, height=2, bg="#F1C40F", fg="white", relief="solid")
                    button.grid(row=j+1, column=i, padx=5, pady=5)
                    continue

                numero = colunas[letra][j]
                button = tk.Button(frame, text=str(numero), font=("Arial", 12), width=6,
                                   height=2, bg="#2D98DA", fg="white", relief="solid",
                                   command=lambda numero=numero: self.marcar_numero_na_tabela(numero))
                button.grid(row=j+1, column=i, padx=5, pady=5)
                self.bingo_buttons[numero] = button

        return frame

    def marcar_numero_na_tabela(self, numero):
        button = self.bingo_buttons.get(numero)
        if button:
            button.config(bg="#1ABC9C", fg="white", text=f"{button['text']} ✅")

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
