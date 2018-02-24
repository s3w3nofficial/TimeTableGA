from dna import DNA

import random
from copy import deepcopy

class Population():


    def __init__(self, data, float mutationRate, int populationSize):
        
        self.data = data
        self.mutationRate = mutationRate
        self.populationSize = populationSize 
       
        self.best = 0
        self.average = 0
        self.worst = None

        self.bestData = []

        self.population = []
        self.matingpool = []
        
        cdef int i
        for i in range(self.populationSize):
            self.population.append(DNA(self.data, self.mutationRate))

    def evaluate(self):
        
        cdef float maxFit = 0
        cdef float worstFit = 10000
        cdef float tmp        

        maxFitData = []

        cdef int i
        for i in range(self.populationSize):
            tmp = self.population[i].calcFitness()
            self.average += tmp
            if tmp > maxFit: 
                maxFit = tmp
                maxFitData = self.population[i].genes
            if worstFit == None or tmp < worstFit: worstFit = tmp

        if maxFit > self.best: 
            self.best = maxFit
            self.bestData = deepcopy(maxFitData)
        if self.worst == None or worstFit < self.worst: self.worst = worstFit
        
        cdef int n
        for i in range(self.populationSize):
            n = int(self.population[i].calcFitness()*100)
            for _ in range(n):
                self.matingpool.append(self.population[i])

    def generate(self):
        
        newPopulation = []
        
        cdef int i
        for i in range(self.populationSize):
            partnerA = self.matingpool[random.randint(0, (len(self.matingpool)-1))]
            partnerB = self.matingpool[random.randint(0, (len(self.matingpool)-1))]

            child = partnerA.crossover(partnerB)
            child.mutate()
            newPopulation.append(child)

        self.population = newPopulation
    
    def calcAverage(self, populationSize, generations):
        return (self.average / populationSize) / generations
