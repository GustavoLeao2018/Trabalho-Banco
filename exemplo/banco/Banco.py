#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlite3 import *

def executar(sqls):
    db = Connection("banco.db")
    cursor = db.cursor()
    for sql in sqls:
        cursor.execute(sql)
    db.commit()
    db.close()

def criar_tabelas():
    sqls = ["""
CREATE TABLE IF NOT EXISTS `departamento` (
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nome` TEXT NOT NULL
);
    """,
    """
CREATE TABLE IF NOT EXISTS `funcionario` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nome`	TEXT NOT NULL,
	`sexo`	TEXT NOT NULL,
	`data_nascimento`	TEXT NOT NULL,
  `id_departamento` INTEGER,
	FOREIGN KEY (`id_departamento`) REFERENCES `departamento`(`id`)
);
    """,
    """
CREATE TABLE IF NOT EXISTS `produto` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nome`	TEXT NOT NULL,
	`tipo`	TEXT NOT NULL,
	`preco_unitario`	REAL NOT NULL,
	`quantidade`	INTEGER NOT NULL
);
    """,
    ]

    executar(sqls)


if __name__ == '__main__':
    criar_tabelas()
