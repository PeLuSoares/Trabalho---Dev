import sqlite3 as lite

# Creating connection

con = lite.connect("todo.db")


with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


def adicionar(i):
    with con:
        cur = con.cursor()
        q = "INSERT INTO tarefas(nome) VALUES(?) "
        cur.execute(q, i)

def atualizar():
    lista = []
    with con:
        cur = con.cursor()
        q = "SELECT * FROM tarefas"
        cur.execute(q)
        row = cur.fetchall()
        for r in row:
            lista.append(r)
    return lista

def remover(i):
    with con:
        cur = con.cursor()
        q = "DELETE FROM tarefas WHERE id=?"
        cur.execute(q, i)
