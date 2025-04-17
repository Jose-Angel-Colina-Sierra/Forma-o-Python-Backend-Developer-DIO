import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cur = con.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela(con, cur):
    cur.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(50))"
    )
    con.commit()


def inserir_registro(con, cur, nome, email):
    data = (nome, email)
    cur.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
    con.commit()


def atualizar_registro(con, cur, nome, email, id):

    data = (nome, email, id)

    cur.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()


def deletar_registros(con, cur, id):

    data = (id,)
    cur.execute("DELETE FROM clientes WHERE id=?", data)
    con.commit()


def inserir_varios_registros(con, cur, dados):
    """
    dados: lista de tuplas no formato [(nome1, email1), (nome2, email2), ...]
    """
    cur.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    con.commit()


def recuperar_cliente(cur, id):
    cur.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cur.fetchone()


def recuperar_varios_clientes(cur):
    return cur.execute("SELECT * FROM clientes ORDER BY nome DESC;")

clientes = recuperar_varios_clientes(cur)

for cliente in clientes:
    print(dict(cliente))

cliente_sozinho = dict(recuperar_cliente(cur, 25))

print(cliente_sozinho)

print(f"Hola, como estas {cliente_sozinho["nome"]}")

# dados= [
#     ("Guilerme", "gui@gmail.com"),
#     ("jose", "jose@gmail.com"),
#     ("rosa", "rosa@gmail.com"),
#     ("gustavo", "gui@gmail.com")
# ]
