import sqlite3

#BANCO DE DADOS
def conectar():
    return sqlite3.connect("atividades.db")

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    
    # Cria tabelas se não existirem
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atividades (
            tipo TEXT NOT NULL,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pontuacao (
            pontos INTEGER NOT NULL
        )
    """)
    
    # Inicializa pontuação se tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM pontuacao")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO pontuacao (pontos) VALUES (0)")
    
    # Insere atividades padrão apenas se tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM atividades")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO atividades (tipo, pergunta, resposta)
            VALUES (?, ?, ?)
        """, [
            ('email', 'Digite um exemplo de email válido:', 'teste@gmail.com'),
            ('atalho', 'Qual tecla completa Ctrl + C ?', 'V'),
            ('google', 'Digite o endereço correto do Google:', 'google.com')
        ])
    
    conn.commit()
    conn.close()

def buscar_atividade(tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT pergunta, resposta FROM atividades WHERE tipo=?", (tipo,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado
    return ("Pergunta não encontrada", "")

def carregar_pontuacao():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT pontos FROM pontuacao LIMIT 1")
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0

def salvar_pontuacao(pontos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE pontuacao SET pontos=? WHERE rowid = 1", (pontos,))
    conn.commit()
    conn.close()
