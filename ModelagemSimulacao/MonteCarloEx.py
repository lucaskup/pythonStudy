import random

def sorteio(lista):
    lista_r = []
    for pair in lista:
        lista_r += [pair[0]]*pair[1]
    return random.choice(lista_r)

def demanda():
    return sorteio([(50000,15), (100000,25), (150000,35), (200000,25)])
def custo():
    return sorteio([(70,2), (90,4), (120,4)])
def preco_venda():
    return sorteio([(120,1), (130,2), (140,4), (150,3)])
def experimento():
    return (demanda(), custo(), preco_venda())
