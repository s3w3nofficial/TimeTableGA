from population import Population
from teacher import Teacher

import json, sys
from termcolor import colored

sys.setrecursionlimit(100000000)

class Handler():


    def __init__(self, data, float mutationRate, int populationSize, int generations):
        
        #self.data = data
                
        teacher = {}
        teacher['T1'] = Teacher('T1', ['M','CJ','D'])
        teacher['T2'] = Teacher('T2', ['M','CJ','D'])
        teacher['T3'] = Teacher('T3', ['M','CJ','D'])

        self.data = [
                        ['C1', [teacher['T1'], teacher['T2']], ['M', 'CJ', 'D']],
                        ['C2', [teacher['T1'], teacher['T2']], ['M', 'CJ']],
                        ['c3', [teacher['T3']], ['M', 'CJ',  'D']]        
                    ]        

        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.generations = generations

    def createPopulation(self):
        
        self.population = Population(self.data, self.mutationRate, self.populationSize)

    def run(self):
        
        cdef int i
        for i in range(self.generations):
            self.population.evaluate()
            average = self.population.calcAverage(self.populationSize, i+1)
            #self.population.generate()
            print "best is: "  + colored(str(self.population.best), 'green') + " and worst is: " + colored(str(self.population.worst), 'red') + " average is: " + colored(str(average), 'yellow')
        self.population.evaluate()

    def writeRes(self):
        cdef int i
        cdef int j
      
        classes = {}
        for i in range(len(self.population.bestData)):
            position = {}
            for j in range(len(self.population.bestData[i][1])):
                position[str(j)] = [self.population.bestData[i][1][j][0], self.population.bestData[i][1][j][1].name] 
            classes[self.population.bestData[i][0]] = position

        print json.dumps(classes, sort_keys=True, indent=4, separators=(',', ': '))
