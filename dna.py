import random
import copy

class DNA():


    def __init__(self, dnaId, subjects, teachers, mutationRate):
        
        self.dnaId = dnaId

        self.subjects = subjects
        self.subjectsCopy = copy.deepcopy(subjects)
        self.teachers = teachers
        self.mutationRate = mutationRate
        self.genes = []
        self.fitness = 0

        for i in range(len(self.subjects)):
            classGenes = []
            for j in range(len(self.subjects[i])):
                tmp = self.newGen(self.subjects[i], self.teachers)
                classGenes.append(tmp)
                self.subjects[i].remove(tmp[0])
            self.genes.append(classGenes)

    def newGen(self, subjectsDay, teachers):
        
        subject = random.choice(subjectsDay)
        
        teacher = self.selectTeacher(subject, teachers)
        while teacher == None:
            teacher = self.selectTeacher(subject, teachers)

        return [subject, teacher]

    # this function is rekursiv :D
    def selectTeacher(self, subject, teachers):
        tmp = random.choice(teachers)
        if subject in tmp.subjects:            
            return tmp
        else:
            return None

    def caclFitness(self):
        
        self.fitness = 0
        score = 0
        
        for i in range(len(self.genes)):
            for j in range(len(self.genes[i])):

                for k in range(len(self.genes)):
                    if j < len(self.genes[k]) and self.genes[i][j][1].name != self.genes[k][j][1].name:
                        score += 1

        self.fitness = float(score) / 100
        return self.fitness

    #pereform crossover with partner
    def crossover(self, partner):

        midpoints = []

        for i in range(len(self.genes)):
            midpoints.append(random.randint(0, len(self.genes[i])))

        for i in range(len(self.genes)):
            for j in range(len(self.genes[i])):
                if(i > midpoints[i]):
                    self.genes[i][j] = partner.genes[i][j]
        
        return self

    def mutate(self):

        for i in range(len(self.genes)):
            for j in range(len(self.genes[i])):
                if(random.uniform(0, 1) < self.mutationRate):
                    self.genes[i][j] = self.newGen(self.subjectsCopy[i], self.teachers)