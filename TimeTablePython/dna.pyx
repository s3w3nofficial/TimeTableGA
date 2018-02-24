from copy import deepcopy
import random

class DNA():


    def __init__(self, data, int mutationRate):

        self.realdata = data
        self.data = deepcopy(data)
        self.mutationRate = mutationRate

        self.genes = []
        self.fitness = 0

        cdef int i
        cdef int j
        for i in range(len(self.data)):
            classGenes = []
            for j in range(len(self.data[i][2])):
                tmp = self.newGen(self.data[i][1], self.data[i][2])
                classGenes.append(tmp)
                self.data[i][2].remove(tmp[0])
            self.genes.append([self.data[i][0], classGenes])

    def newGen(self, teachers, subjects):
        subject = random.choice(subjects)
        
        teacher = self.selectTeacher(subject, teachers)
        while teacher == None:
            teacher = self.selectTeacher(subject, teachers)

        return [subject, teacher]

    def selectTeacher(self, subject, teachers):
      
        tmp = random.choice(teachers)
        if subject in tmp.subjects:
            return tmp
        else:
            return None

    def calcFitness(self):
        
        self.fitness = 0
        cdef int score = 0
        
        cdef int i
        cdef int j
        cdef int k

        for i in range(len(self.genes)):
            for k in range(len(self.genes)):
                for j in range(len(self.genes[i][1])):
                    if j < len(self.genes[k][1]) and self.genes[i][1][j][1].name != self.genes[k][1][j][1].name:
                        score += 1


        self.fitness = float(score) / 100
        return self.fitness

    def crossover(self, partner):
        
        midpoints = []
        
        cdef int i
        
        for i in range(len(self.genes[1])):
            midpoints.append(random.randint(0, len(self.genes[1][i])))

        cdef int j
        for i in range(len(self.genes[1])):
            for j in range(len(self.genes[1][i])):
                if i > midpoints[i]:
                    self.genes[1][i][j][1] = partner.genes[1][i][j][1]

        return self
    
    def mutate(self):
        cdef int i
        cdef int j
        for i in range(len(self.genes[1])):
            for j in range(len(self.genes[1][i])):
                if(random.uniform(0, 1) < self.mutationRate):
                    self.genes[i][1][j] = self.newGen(self.realdata[i][1], self.genes[i][1][j][0])

