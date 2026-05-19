# banco.py
import sqlite3
import random
BANCO = "curso_informatica.db"
ATIVIDADES = {
 "email": [
 ("Qual campo você preenche para enviar um e-mail para alguém?", "para"),
 ("Qual botão você clica para enviar um e-mail?", "enviar"),
 ("Como se chama a pasta onde ficam os e-mails recebidos?", "caixa de entrada"),
 ("Qual campo usamos para escrever o assunto do e-mail?", "assunto"),
 ("Onde ficam os e-mails que você enviou?", "enviados"),
 ("Como se chama a pasta de e-mails excluídos?", "lixeira"),
 ("Qual campo usamos para enviar cópia do e-mail?", "cc"),
 ],
 "atalho": [
 ("Qual atalho usamos para copiar um texto?", "ctrl+c"),
 ("Qual atalho usamos para colar um texto?", "ctrl+v"),
 ("Qual atalho usamos para desfazer uma ação?", "ctrl+z"),
 ("Qual atalho usamos para salvar um arquivo?", "ctrl+s"),
 ("Qual atalho usamos para selecionar tudo?", "ctrl+a"),
 ("Qual atalho usamos para recortar um texto?", "ctrl+x"),
 ("Qual atalho abre uma nova aba no navegador?", "ctrl+t"),
 ],
 "google": [
 ("Qual site usamos para fazer pesquisas na internet?", "google.com"),
 ("O que você digita na barra do navegador para acessar um site?", "o endereço do site"),
 ("Como se chama a barra onde digitamos o endereço de um site?", "barra de endereço"),
 ("O que significa www?", "world wide web"),
 ("Qual tecla pressionamos para pesquisar após digitar no Google?", "enter"),
 ("Como se chama o programa usado para navegar na internet?", "navegador"),
 ],
}
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
def inicializar_banco():
 conn = sqlite3.connect(BANCO)
 cursor = conn.cursor()
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS pontuacao (
 id INTEGER PRIMARY KEY,
 valor INTEGER NOT NULL DEFAULT 0
 )
 """)
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS atividades (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 tipo TEXT NOT NULL,
 pergunta TEXT NOT NULL,
 resposta TEXT NOT NULL
 )
 """)
 # Insere atividades apenas se a tabela estiver vazia
 cursor.execute("SELECT COUNT(*) FROM atividades")
 if cursor.fetchone()[0] == 0:
 for tipo, itens in ATIVIDADES.items():
 for pergunta, resposta in itens:
 cursor.execute(
 "INSERT INTO atividades (tipo, pergunta, resposta) VALUES (?, ?, ?)",
 (tipo, pergunta, resposta)
 )
 # Garante que existe uma linha de pontuação
 cursor.execute("SELECT COUNT(*) FROM pontuacao")
 if cursor.fetchone()[0] == 0:
 cursor.execute("INSERT INTO pontuacao (id, valor) VALUES (1, 0)")
 conn.commit()
 conn.close()
def carregar_pontuacao():
 conn = sqlite3.connect(BANCO)
 cursor = conn.cursor()
 cursor.execute("SELECT valor FROM pontuacao WHERE id = 1")
 resultado = cursor.fetchone()
 conn.close()
 return resultado[0] if resultado else 0
def salvar_pontuacao(valor):
 conn = sqlite3.connect(BANCO)
 cursor = conn.cursor()
 cursor.execute("UPDATE pontuacao SET valor = ? WHERE id = 1", (valor,))
 conn.commit()
 conn.close()
def buscar_atividade(tipo):
 conn = sqlite3.connect(BANCO)
 cursor = conn.cursor()
 cursor.execute(
 "SELECT pergunta, resposta FROM atividades WHERE tipo = ?", (tipo,)
 )
 resultados = cursor.fetchall()
 conn.close()
 if not resultados:
 return "Nenhuma pergunta encontrada.", ""
 pergunta, resposta = random.choice(resultados)
 return pergunta, resposta
