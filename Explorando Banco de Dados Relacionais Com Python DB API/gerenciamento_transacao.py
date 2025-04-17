import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cur = con.cursor()
cur.row_factory = sqlite3.Row

try:
    cur.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", ("test5","test5@gmail.com"))
    cur.execute("INSERT INTO clientes (id,nome,email) VALUES (?,?,?)", (25,"test6","test6@gmail.com"))
    # cur.execute("DELETE FROM clientes Where id = 25;")
    con.commit()
except Exception as e:
    print(f"Ocorreu o seguinte erro: {e}")
    con.rollback()