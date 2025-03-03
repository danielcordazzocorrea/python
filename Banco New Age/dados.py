from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
app = Flask(__name__)
def conectar_db():
    banco = sqlite3.connect('Banco New Age/contas.db')
    return banco
def criar_tabela():
    banco = conectar_db()
    cursor = banco.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nome TEXT NOT NULL,
                   senha TEXT NOT NULL)''')