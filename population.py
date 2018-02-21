import random

from dna import DNA

class Population():


    def __init__(self, subjects, teachers, mutationRate, populationSize):

        self.population = []
        self.matingpool = []

        self.subjects = subjects

        self.best = 0
        self.bestData = []
        self.worst = None
        self.average = 0
        self.populationSize = populationSize
        self.perfectFit = 0

        for i in range(self.populationSize):
            self.population.append(DNA(i, self.subjects, teachers, mutationRate))

    def evaluate(self, calcPerfect=False):

        #calculate maxFit and worstFit from population
        maxFit = 0
        maxFitData = []
        worstFit = None

        if calcPerfect == True:
            self.population[0].caclFitness(calcPerfect)
            self.perfectFit = self.population[0].perfectFit

        for i in range(self.populationSize):
            tmp = self.population[i].caclFitness()
            self.average += tmp
            if tmp > maxFit: 
                maxFit = tmp
                maxFitData = self.population[i].genes

            if worstFit == None or tmp < worstFit: worstFit = tmp

        #calculate overall best
        if maxFit > self.best: 
            self.best = maxFit
            self.bestData = maxFitData
        #calculate overall worst
        if self.worst == None or worstFit < self.worst: self.worst = worstFit

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