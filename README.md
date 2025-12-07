# Relogio
# um relogio simples que eu fiz como meu primeiro projeto
import tkinter as tk
from time import strftime

def atualizar_relogio():
    hora_atual = strftime('%H:%M:%S')
    label_hora.config(text=hora_atual)
    label_hora.after(1000, atualizar_relogio)

# Nome fixo
usuario = "Micael"

# Criação da janela
janela = tk.Tk()
janela.title("Relógio Digital")

janela.geometry("350x150")

# Frase de boas-vindas
label_bemvindo = tk.Label(
    janela,
    text=f"Bem-vindo, {usuario}",
    font=('Arial', 16),
    foreground='black'
)
label_bemvindo.pack(pady=5)

# Relógio
label_hora = tk.Label(
    janela,
    font=('Arial', 40),
    background='black',
    foreground='white'
)
label_hora.pack(anchor='center')

# Inicia atualização
atualizar_relogio()

# Roda a janela
janela.mainloop()
