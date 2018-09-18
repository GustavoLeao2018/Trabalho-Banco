#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint, random, choice
import Banco as db

def cadastrar_departamentos():
    departamentos = [ "Açougeiro", "Padeiro", "Caixa", "Limpeza", "Segurança", "Estoquista"]

    for departamento in departamentos:
        db.Banco().inserir_departamento(departamento)

def cadastrar_funcionarios():
    nomes = [ "Miguel","Lucas","Guilherme","Gabriel","Enzo","Arthur","Rafael","João","Gustavo",
             "Beatriz","Laura","Maria","Júlia","Ana","Alice","Sofia","Maria Eduarda","Larissa","Mariana" ]
    for nome in nomes:
         db.Banco().inserir_funcionario(nome, randint(0, 5))

def cadastrar_produtos():
    produtos = [
        "Arroz","Feijão","Açúcar","Café","Chá","Achocolatado","Leite","Páo",
        "Farinha de Trigo","Farinha de Rosca","Amido de Milho","Fermento","Macarrão",
        "Molho de Tomate","Leite condensado","Creme de leite","Gelatina","Ketchup",
        "Maionese","Óleo","Azeite","Vinagre","Tempero Pronto", "Sal",

        "Alface","Repolho","Vagem","Tomate","Pepino","Cebola","Batata","Cenoura",
        "Pimentão","Chuchu","Limão","Banana","Mamão","Melão","Laranja","Abacaxi",
        "Morango","Maçã","Maracujá","Melancia",

        "Água mineral","Refrigerante","Suco","Cerveja","Vinho",

        "Detergente","Desinfetante","Água sanitária","Sabão em Pó","Sabão em pedra","Amaciante",
        "Álcool","Lustra móveis","Inseticida","Saco de Lixo","Papel Toalha","Guardanapo",
        "Papel Alumínio","Filme plástico","Esponja de aço","Rodo / vassoura","Fósforo","Vela",
        "Lâmpada","Palito de dente", "Filtro para café",


        "Shampoo","Condicionador","Sabonete","Desodorante","Papel higiênico","Creme dental",
        "Fio dental","Escova de dentes","Cotonete","Algodão","Absorvente",

        "Bife","Carne Moída","Carne de frango","Presunto","Mussarela","Mortadela","Salsicha","Linguiça"

    ]
    tipo = [ "Diversos", "Frutas e verduras", "Bebidas", "Utilidades e limpeza", "Higiene", "Carnes" ]

    for cont, produto in enumerate(produtos):
        if cont >= 0 and cont <= 23:
            n = 0
        elif cont >= 24 and cont <= 43:
            n = 1
        elif cont >= 44 and cont <= 48:
            n = 2
        elif cont >= 49 and cont <= 69:
            n = 3
        elif cont >= 70 and  cont <= 80:
            n = 4
        elif cont >= 81 and cont <= 88:
            n = 5
        else:
            n = 0
        db.Banco().inserir_produto(produto, tipo[n], randint(0, 100), format((random() * 10), ".2f"))


def listar_produtos():
    lista = db.Banco().listar_produtos()
    for item in lista:
        print(item)

def lista_funcionarios():
    lista = db.Banco().listar_funcionairos()
    for item in lista:
        print(item)

def lista_departamentos():
    lista = db.Banco().listar_departamentos()
    for item in lista:
        print(item)


def apagar_produto(id):
    db.Banco().apagar_produto(id)
    print("="*100)
    listar_produtos()
    print("="*100)

def apagar_funcionario(id):
    db.Banco().apagar_funcionario(id)
    print("="*100)
    lista_funcionarios()
    print("="*100)

def apagar_departamento(id):
    db.Banco().apagar_departamento(id)
    print("="*100)
    lista_departamentos()
    print("="*100)
    lista_funcionarios()

def editar_departamento(id):
    db.Banco().editar_departamento(id, "Lancheria")
    print("="*100)
    lista_departamentos()

def editar_funcionario(id):
    db.Banco().editar_funcionario(id, choice(["Miguel","Lucas","Guilherme","Gabriel","Enzo","Arthur","Rafael","João","Gustavo",
             "Beatriz","Laura","Maria","Júlia","Ana","Alice","Sofia","Maria Eduarda","Larissa","Mariana" ]))
    print("="*100)
    lista_funcionarios()

def editar_produto(id):
    db.Banco().editar_produto((randint(0, 100)), (random() * 10), id)
    print("="*100)
    lista_funcionarios()


if __name__ == '__main__':

    cadastrar_departamentos()
    cadastrar_funcionarios()
    cadastrar_produtos()

    listar_produtos()
    lista_funcionarios()
    lista_departamentos()

    prod = randint(1, 89)
    print(prod)
    apagar_produto(prod)

    func = randint(1, 19)
    print(func)
    apagar_funcionario(func)

    dep = randint(1, 6)
    print(dep)
    apagar_departamento(dep)


    prod = randint(1, 89)
    print(prod)
    editar_produto(prod)

    func = randint(1, 19)
    print(func)
    editar_funcionario(func)

    dep = randint(1, 6)
    print(dep)
    editar_departamento(dep)
