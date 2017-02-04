#!/usr/bin/python

import sys
from frase import Frase
import random

def getNewPopulation(popSize,size):
    return [Frase(size=size) for i in range(popSize)]

def nextGen(pop,goal):
    selection = []
    m_fit = max([frase.fitness(goal) for frase in pop])
    for frase in pop:
        fit = frase._fit/m_fit
        selection += [frase]*int(fit*100)
    if(len(selection)>10):
        nGen = []
        for i in range(len(pop)):
            p1 = random.choice(selection)
            p2 = random.choice(selection)
            nGen.append(Frase(parent1 = p1,parent2 = p2))
        return nGen
    else:
        return getNewPopulation(len(pop),len(pop[0].dna))

def done(population,sWord):
    for f in population:
        if f.fitness(sWord)==1.0:
            return True
    return False

sWord = 'lucas teste!'
if len(sys.argv) > 1:
    sWord = ' '.join(''.join(e) for e in sys.argv[1:])
    sWord = sWord.lower()

p = getNewPopulation(400,len(sWord))

while not done(p,sWord):
    p = nextGen(pop=p,goal=sWord)
    k = sum([f.fitness(sWord) for f in p])/len(p)
    print('Medium Fitness: ',str(int(k*100))+'%')
p = sorted(p,key=lambda f:f.fitness(sWord),reverse=True)


print('My First Genetic Algorithim',p[0].dna, p[0].gen)
