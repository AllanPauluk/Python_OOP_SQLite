import sqlite3

class Database:
    conexao = None
    cursor = None

    def __init__(self):
        self.conexao = sqlite3.connect("database/imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.conexao.commit()