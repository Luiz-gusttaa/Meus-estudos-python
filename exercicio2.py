import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        curso TEXT
    )
            
""")


cursor.execute("UPDATE  alunos SET idade = ?  WHERE nome = ?", (27 , "Luiz"))
cursor.execute("DELETE FROM alunos WHERE nome = ?", ("Gustavo",))
conexao.commit()

cursor.execute("SELECT * FROM alunos")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)