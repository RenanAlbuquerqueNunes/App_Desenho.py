import tkinter as tk
from tkinter import ttk, colorchooser
import turtle

# ----------------------------- VARIÁVEIS GLOBAIS -----------------------------
modo_pincel = False
cor_atual = "black"
espessura = 5
tamanho_forma = 100

# ----------------------------- FUNÇÕES DO MODO FORMAS -----------------------------
def desenhar_forma():
    forma = forma_var.get()
    cor = cor_var.get()
    tamanho = tamanho_var.get()

    tela_turtle.clear()
    tela_turtle.color(cor)
    tela_turtle.begin_fill()

    if forma == "Quadrado":
        for _ in range(4):
            tela_turtle.forward(tamanho)
            tela_turtle.right(90)
    elif forma == "Triângulo":
        for _ in range(3):
            tela_turtle.forward(tamanho)
            tela_turtle.left(120)
    elif forma == "Círculo":
        tela_turtle.circle(tamanho / 2)
    elif forma == "Pentágono":
        for _ in range(5):
            tela_turtle.forward(tamanho)
            tela_turtle.right(72)
    elif forma == "Estrela":
        for _ in range(5):
            tela_turtle.forward(tamanho)
            tela_turtle.right(144)

    tela_turtle.end_fill()

def limpar_turtle():
    tela_turtle.clear()

# ----------------------------- FUNÇÕES DO MODO PINCEL -----------------------------
def escolher_cor():
    global cor_atual
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_atual = cor

def mudar_espessura(valor):
    global espessura
    espessura = int(valor)

def desenhar_com_pincel(event):
    x, y = event.x, event.y
    r = espessura // 2
    canvas_pincel.create_oval(x - r, y - r, x + r, y + r, fill=cor_atual, outline=cor_atual)

def limpar_canvas():
    canvas_pincel.delete("all")

# ----------------------------- FUNÇÃO PARA TROCAR MODOS -----------------------------
def alternar_modo():
    global modo_pincel
    modo_pincel = not modo_pincel

    if modo_pincel:
        frame_formas.pack_forget()
        canvas_pincel.pack(pady=10)
        frame_pincel.pack()
        btn_modo.config(text="Modo: Formas")
    else:
        canvas_pincel.pack_forget()
        frame_pincel.pack_forget()
        frame_formas.pack()
        btn_modo.config(text="Modo: Pincel")

# ----------------------------- INTERFACE GRÁFICA -----------------------------
janela = tk.Tk()
janela.title("Desenhar com Formas e Pincel")
janela.geometry("600x600")

# ----------------------------- FRAME FORMAS -----------------------------
frame_formas = tk.Frame(janela)
frame_formas.pack()

forma_var = tk.StringVar(value="Quadrado")
cor_var = tk.StringVar(value="black")
tamanho_var = tk.IntVar(value=100)

ttk.Label(frame_formas, text="Escolha uma forma:").pack(pady=5)
ttk.Combobox(frame_formas, textvariable=forma_var, values=["Quadrado", "Triângulo", "Círculo", "Pentágono", "Estrela"], state="readonly").pack()

ttk.Label(frame_formas, text="Escolha uma cor:").pack(pady=5)
ttk.Combobox(frame_formas, textvariable=cor_var, values=["black", "red", "blue", "green", "yellow", "purple"], state="readonly").pack()

ttk.Label(frame_formas, text="Tamanho da forma:").pack(pady=5)
ttk.Scale(frame_formas, from_=20, to=200, orient="horizontal", variable=tamanho_var).pack()

ttk.Button(frame_formas, text="Desenhar Forma", command=desenhar_forma).pack(pady=10)
ttk.Button(frame_formas, text="Limpar Tela", command=limpar_turtle).pack()

# ----------------------------- TELA TURTLE (MODO FORMAS) -----------------------------
tela = turtle.Screen()
tela.title("Tela de Formas")
tela.bgcolor("white")
tela.setup(width=500, height=500)
tela_turtle = turtle.Turtle()
tela_turtle.speed(3)

# ----------------------------- FRAME PINCEL -----------------------------
canvas_pincel = tk.Canvas(janela, width=500, height=400, bg="white")
canvas_pincel.bind("<B1-Motion>", desenhar_com_pincel)

frame_pincel = tk.Frame(janela)

btn_cor = tk.Button(frame_pincel, text="Escolher Cor", command=escolher_cor)
btn_cor.pack(side="left", padx=10)

tk.Label(frame_pincel, text="Espessura:").pack(side="left")
slider = tk.Scale(frame_pincel, from_=1, to=20, orient="horizontal", command=mudar_espessura)
slider.set(espessura)
slider.pack(side="left", padx=10)

btn_limpar = tk.Button(frame_pincel, text="Limpar Desenho", command=limpar_canvas)
btn_limpar.pack(side="left", padx=10)

# ----------------------------- BOTÃO DE MODO -----------------------------
btn_modo = tk.Button(janela, text="Modo: Pincel", command=alternar_modo)
btn_modo.pack(pady=10)

# ----------------------------- INICIA A JANELA -----------------------------
janela.mainloop()
