import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS alunos")
cursor.execute("DROP TABLE IF EXISTS cursos")


cursor.execute("""
    CREATE TABLE alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        curso_id INTEGER
    )
            
""")

cursor.execute("""
    CREATE TABLE cursos(
    id INTEGER PRiMARY KEY,
    nome TEXT,
    duracao_anos INTEGER
    )

""")

cursor.execute("INSERT INTO cursos (nome, duracao_anos) VALUES (?, ?)", ("Engenharia", 5))
cursor.execute("INSERT INTO cursos (nome, duracao_anos) VALUES (?, ?)", ("Sistema de informação", 4))
cursor.execute("INSERT INTO alunos (nome, idade, curso_id) VALUES (?, ?, ?)", ("Luiz", 26, 1) )
cursor.execute("INSERT INTO alunos (nome, idade, curso_id) VALUES (?, ?, ?)", ("Ana" , 22, 2) )
cursor.execute("INSERT INTO alunos (nome, idade, curso_id) VALUES (?, ?, ?)", ("Gustavo", 25, 2) )


conexao.commit()

cursor.execute("""
    SELECT alunos.nome, alunos.idade, cursos.nome, cursos.duracao_anos
    FROM alunos
    JOIN cursos ON alunos.curso_id = cursos.id
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)