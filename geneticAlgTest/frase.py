import random
import string
class Frase:
    possible_char = string.ascii_lowercase + ' '

    def __init__(self,size=0,parent1=None,parent2=None):
        self._fit = -1
        if parent1 != None and parent2 != None:
            size_dna = len(parent1.dna)
            self.dna = parent1.dna[0:size_dna//2] + parent2.dna[size_dna//2:size_dna]
            self._mutation()
            self.gen = parent1.gen + 1

        else:
            self.gen = 0
            self.dna = []
            for i in range(size):
                self.dna.append(random.choice(self.possible_char))

    def _mutation(self):
        l = [False]*99 + [True]*1
        for i in range(len(self.dna)):
            if random.choice(l):
                self.dna[i] = random.choice(self.possible_char)
    def fitness(self,goal):
        if self._fit == -1:
            self._fit = 0
            #print(goal,frase.dna, frase.gen)
            for i in range(len(goal)):
                if goal[i] == self.dna[i]:
                    self._fit += 1
            self._fit = (self._fit/len(self.dna))**4
        return self._fit
