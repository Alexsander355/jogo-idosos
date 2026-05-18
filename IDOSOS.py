from tkinter import *
from tkinter import messagebox
import banco

#SISTEMA
pontuacao = 0
texto_pontos = None

#FUNÇÕES
def atualizar_placar():
    global texto_pontos
    if texto_pontos:
        texto_pontos.config(text=f"Pontuação: {pontuacao}")

def conferir_resposta(valor_digitado, resposta_certa):
    global pontuacao
    if valor_digitado.strip().lower() == resposta_certa.lower():
        pontuacao += 1
        messagebox.showinfo("Resultado", "Resposta correta!")
    else:
        pontuacao -= 1
        messagebox.showwarning("Resultado", f"Resposta errada.\nCorreto seria: {resposta_certa}")
    
    banco.salvar_pontuacao(pontuacao)
    atualizar_placar()

def criar_tela(tipo, titulo, largura):
    pergunta, resposta = banco.buscar_atividade(tipo)
    tela = Toplevel()
    tela.title(titulo)
    tela.geometry("380x220")

    Label(tela, text=pergunta).pack(pady=10)
    caixa = Entry(tela, width=largura)
    caixa.pack(pady=10)

    Button(tela, text="Confirmar", command=lambda: conferir_resposta(caixa.get(), resposta)).pack(pady=10)

def atividade_email():
    criar_tela("email", "Atividade - Email", 30)

def atividade_atalho():
    criar_tela("atalho", "Atividade - Atalho", 10)

def atividade_google():
    criar_tela("google", "Atividade - Navegador", 25)

#INÍCIO DO PROGRAMA
def iniciar_programa():
    global texto_pontos, pontuacao
    banco.inicializar_banco()
    pontuacao = banco.carregar_pontuacao()

    janela_principal = Tk()
    janela_principal.title("Curso Básico de Informática")
    janela_principal.geometry("320x300")

    Label(janela_principal, text="Escolha uma atividade").pack(pady=10)
    texto_pontos = Label(janela_principal, text=f"Pontuação: {pontuacao}")
    texto_pontos.pack(pady=5)

    Button(janela_principal, text="Treino de Email", width=22, command=atividade_email).pack(pady=5)
    Button(janela_principal, text="Mover Arquivos", width=22, command=atividade_atalho).pack(pady=5)
    Button(janela_principal, text="Usar Google", width=22, command=atividade_google).pack(pady=5)
    Button(janela_principal, text="Fechar", width=22, command=janela_principal.destroy).pack(pady=15)

    janela_principal.mainloop()

    iniciar_programa()
