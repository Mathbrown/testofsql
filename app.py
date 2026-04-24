from flask import Flask, request
import sqlite3

app = Flask(__name__)    

database = sqlite3.connect("database.db", check_same_thread=False)
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")

@app.route("/")
def hello():
    return "Hello Matheus!"

@app.route("/usuarios")
def usuarios():
    cursor.execute("SELECT * FROM usuarios");
    usuariosFetch = cursor.fetchall()

    html = "<h1>Usuários</h1><a href='/adicionar_usuario'>Adicionar Usuário</a><ul>"

    for usuario in usuariosFetch:
        html += f"<li># {usuario[0]} - {usuario[1]}</li>"
        # editar e excluir
        html += f'<a href="/editar_usuario/{usuario[0]}">Editar</a> | <a href="/excluir_usuario/{usuario[0]}">Excluir</a>'

    html += "</ul>"
    return html

@app.route("/adicionar_usuario")
def adicionar_usuario_form():
    return '''
        <form action="/adicionar_usuario" method="post">
            <input type="text" name="nome" placeholder="Nome do usuário">
            <input type="submit" value="Adicionar">
        </form>
    '''

@app.route("/adicionar_usuario", methods=["POST"])
def adicionar_usuario():
    nome = request.form["nome"]
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    database.commit()
    return f"Usuário adicionado: {nome}"

@app.route("/editar_usuario/<int:id>")
def editar_usuario(id):
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
    usuario = cursor.fetchone()
    if not usuario:
        return "Usuário não encontrado", 404
    return f'''
        <form action="/editar_usuario/{id}" method="post">
            <input type="text" name="nome" value="{usuario[1]}">
            <input type="submit" value="Atualizar">
        </form>
    '''

@app.route("/editar_usuario/<int:id>", methods=["POST"])
def atualizar_usuario(id):
    nome = request.form["nome"]
    cursor.execute("UPDATE usuarios SET nome=? WHERE id=?", (nome, id))
    database.commit()
    return f"Usuário atualizado: {nome}"

@app.route("/excluir_usuario/<int:id>")
def excluir_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    database.commit()
    return f"Usuário com ID {id} excluído"

if __name__ == "__main__":
    app.run(port=3000)