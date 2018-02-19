import random

from dna import DNA

class Population():


    def __init__(self, subjects, teachers, mutationRate, populationSize):

        self.population = []
        self.matingpool = []

        self.best = 0
        self.worst = 0
        self.average = 0
        self.populationSize = populationSize

        for i in range(self.populationSize):
            self.population.append(DNA(i, [
                        ['M','V','A','C','C','V','Z','Z','C'],
                        ['D','M','M','C','C','A'],
                        ['Z','F','F','C','A','C'],
                        ['M','V','A','F','F','A','D']                
                                            ], teachers, mutationRate))

    def evaluate(self):

        #calculate maxFit and worstFit from population
        maxFit = 0
        worstFit = 0

        for i in range(self.populationSize):
            tmp = self.population[i].caclFitness()
            self.average += tmp
            if tmp > maxFit:
                maxFit = tmp
            if tmp < worstFit:
                worstFit = tmp

        #calculate overall best
        if maxFit > self.best: self.best = maxFit
        #calculate overall worst
        if worstFit < self.worst: self.worst = worstFit

        for i in range(self.populationSize):
            n = int(self.population[i].caclFitness()*100)
            for _ in range(n):
                self.matingpool.append(self.population[i])

    def generate(self):

        newPopulation = []
        for i in range(self.populationSize):
            partnerA = self.matingpool[random.randint(0, (len(self.matingpool)-1))]
            partnerB = self.matingpool[random.randint(0, (len(self.matingpool)-1))]
            child = partnerA.crossover(partnerB)
            child.mutate()
            newPopulation.append(child)

        self.population = newPopulation

    def calcAverage(self, population, generations):
        return (self.average / population) / generations