import tkinter as tk
import random

def fugir(event):
    # botao do nao fugindo
    novo_x = random.randint(0, 300)
    novo_y = random.randint(0, 250)
    btn_nao.place(x=novo_x, y=novo_y)

def aceitar():
    # desaparece os botoes e aparece a msg
    texto_principal.config(text="Sabia que você era beijoqueiro")
    btn_sim.place_forget()
    btn_nao.place_forget()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Proposta O.O")
janela.geometry("500x300")
janela.configure(bg="#ff85a2") # Um tom de rosa parecido com o do vídeo

# Texto da pergunta
texto_principal = tk.Label(
    janela, 
    text="Quer me dar um beijinho?", 
    font=("Arial", 16, "bold"), 
    bg="#ff85a2", 
    fg="white"
)
texto_principal.pack(pady=50)

# Botão Sim
btn_sim = tk.Button(
    janela, 
    text="Sim", 
    font=("Arial", 12, "bold"), 
    command=aceitar, 
    bg="white", 
    relief="raised"
)
btn_sim.place(x=170, y=150)

# Botão Não
btn_nao = tk.Button(
    janela, 
    text="Não", 
    font=("Arial", 12, "bold"), 
    bg="white", 
    relief="raised"
)
btn_nao.place(x=280, y=150)

# O evento "<Enter>" detecta quando o ponteiro do mouse passa por cima do botão
btn_nao.bind("<Enter>", fugir)

janela.mainloop()