import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox, simpledialog

# Criar a janela principal
janela = tk.Tk()
janela.title("CONTROLE DE ATIVIDADES")
janela.geometry("350x150")


mensagem_label = tk.Label(janela, text="CONTROLE DE ATIVIDADES", font=("Arial", 11), wraplength=300)
mensagem_label.pack(pady=20)

tk.Label(janela, text=f"atividade:", font=("Arial", 12, "bold")).pack(anchor="center", padx=18, pady=(18, 10))

atividade_entry = tk.Entry(janela, font=("Arial", 10), width=60)
atividade_entry.pack(anchor="center", padx=18, pady=(0, 10), ipady=5)



def editar_atividade():
    atividade_selecionada = lista_atividades.curselection()
    if atividade_selecionada:
        indice = atividade_selecionada[0]
        atividade_atual = lista_atividades.get(indice)
        nova_atividade = simpledialog.askstring("Editar Atividade", "Digite a nova atividade:", initialvalue=atividade_atual)
        if nova_atividade:
            lista_atividades.delete(indice)
            lista_atividades.insert(indice, nova_atividade)
    else:
        messagebox.showwarning("Aviso", "Selecione uma atividade para editar.")
    
def inserir_atividade():
    atividade = atividade_entry.get().strip()

    if atividade:
        numero_atividades = lista_atividades.size()
        lista_atividades.insert(tk.END, f"{numero_atividades + 1}. {atividade}")
        atividade_entry.delete(0, tk.END)

botao = tk.Button(janela, text="Inserir atividade",command=lambda: inserir_atividade())
botao.pack(pady=10)

lista_atividades = tk.Listbox(janela, font=("Arial", 10), width=60)
lista_atividades.pack(anchor="center", padx=18, pady=(0, 10))

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botaodelete= tk.Button(frame_botoes, text="Excluir atividade",command=lambda: lista_atividades.delete(tk.ACTIVE))
botaodelete.pack(side="left", padx=5, pady=10)

botaoeditar = tk.Button(frame_botoes, text="Editar atividade", command=lambda: editar_atividade())
botaoeditar.pack(side="left", padx=5, pady=10)































































































# Loop principal da janela
janela.mainloop()