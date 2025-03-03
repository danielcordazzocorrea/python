from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

# Criar a tabela se não existir
def init_db():
    banco = sqlite3.connect("contas.db")
    cursor = banco.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Senha TEXT NOT NULL,
            dinheiro REAL DEFAULT 0,
            Investimento REAL DEFAULT 0
        )
    ''')
    banco.commit()
    banco.close()

@app.route("/dados", methods=["POST"])
def receber_dados():
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    if nome and senha:
        banco = sqlite3.connect("contas.db")
        cursor = banco.cursor()

        print(f"Nome: {nome}, Senha: {senha}") 

        # Inserção correta com segurança
        cursor.execute("INSERT INTO dados (Nome, Senha, dinheiro, Investimento) VALUES (?, ?, ?, ?)", 
                       (nome, senha, 0, 0))

        banco.commit()
        banco.close()
        return redirect(r"C:\Users\Pr. Genival\Downloads\python\Banco New Age\Banco.html")  # Verifique se esse arquivo está na pasta correta

    return "Erro ao cadastrar usuário!", 400

if __name__ == "__main__":
    init_db()  # Garante que a tabela exista
    app.run(debug=True)
