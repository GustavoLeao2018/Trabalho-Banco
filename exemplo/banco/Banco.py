
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlite3 import *

class Banco:
    def __init__(self):
        self.tabelas()

    def criar_tabela(self, sql):
        banco = Connection("banco.db")
        cursor = banco.cursor()
        cursor.execute(sql)
        banco.commit()
        banco.close()

    def executar_select(self, sql):
        banco = Connection("banco.db")
        cursor = banco.cursor()
        lista = cursor.execute(sql)
        lista_final = lista.fetchall()
        banco.close()
        return lista_final

    def executar_sql(self, sql, *args):
        banco = Connection("banco.db")
        cursor = banco.cursor()
        cursor.execute(sql, *args)
        banco.commit()
        banco.close()

    def editar_departamento(self, id, nome):
        sql = "UPDATE departamento SET nome = ? WHERE id = ?;"
        self.executar_sql(sql, (nome, id))

    def editar_funcionario(self, id, nome):
        sql = "UPDATE funcionario SET nome = ? WHERE id = ?;"
        self.executar_sql(sql, (nome, id))

    def editar_produto(self, quantidade, preco_unitario, id):
        sql = "UPDATE produto SET preco_unitario = ?, quantidade = ? WHERE id = ?;"
        self.executar_sql(sql, (preco_unitario, quantidade, id))

    def apagar_produto(self, id):
        sql = "DELETE FROM produto WHERE id = ?;"
        self.executar_sql(sql, (id,))

    def apagar_funcionario(self, id):
        sql = "DELETE FROM funcionario WHERE id = ?;"
        self.executar_sql(sql, (id,))

    def apagar_departamento(self, id):
        sql1 = "DELETE FROM departamento WHERE id = ?;"
        sql2 = "DELETE FROM funcionario WHERE id_departamento = ?;"
        self.executar_sql(sql1, (id,))
        self.executar_sql(sql2, (id,))

    def listar_produtos(self):
        sql = "SELECT * FROM produto;"
        lista = self.executar_select(sql)
        return lista

    def listar_departamentos(self):
        sql = "SELECT * FROM departamento;"
        lista = self.executar_select(sql)
        return lista

    def listar_funcionairos(self):
        sql = "SELECT * FROM funcionario;"
        lista = self.executar_select(sql)
        return lista

    def inserir_produto(self, produto, tipo, quantidade, preco_unitario):
        sql = "INSERT INTO produto VALUES (?, ?, ?, ?, ?);"
        self.executar_sql(sql, (None, produto, tipo, quantidade, preco_unitario))

    def inserir_departamento(self,  departamento):
        sql = "INSERT INTO departamento VALUES (?, ?);"
        self.executar_sql(sql, (None, departamento))

    def inserir_funcionario(self, nome, departamento):
        sql = "INSERT INTO funcionario VALUES (?, ?, ?);"
        self.executar_sql(sql, (None, nome, departamento))

    def tabelas(self):
        sql1 = """
                CREATE TABLE IF NOT EXISTS departamento(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT
                );
                """
        sql2 = """
                CREATE TABLE IF NOT EXISTS funcionario(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    id_departamento INTEGER,
                    FOREIGN KEY (id_departamento) REFERENCES departamento(id)
                );
                """
        sql3 = """
                CREATE TABLE IF NOT EXISTS produto(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    tipo TEXT,
                    quantidade INTEGER,
                    preco_unitario REAL
                );
                """
        self.criar_tabela(sql1)
        self.criar_tabela(sql2)
        self.criar_tabela(sql3)
