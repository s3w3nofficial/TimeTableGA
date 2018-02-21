from termcolor import colored
import sys, json

sys.setrecursionlimit(100000000)

from population import Population
from teacher import Teacher

subjects = [
    ['M','V','A','C','C','V','Z','Z','C'],
    ['D','M','M','C','C','A'],
    ['Z','F','F','C','A','C'],
    ['M','V','A','F','F','A','D']
]

teachers = []
teachers.append(Teacher('T1', ['M','V','D','C','F','Z']))
teachers.append(Teacher('T2', ['M','V','A','D','C','F','Z']))
teachers.append(Teacher('T3', ['M','D','C','F','Z']))
teachers.append(Teacher('T4', ['M','V','A','D','C','F','Z']))

perfectFit = 0

mutationRate = 0.01
populationSize = 1

generations = 1

def writeRes(data):

    classes = {}
    for i in range(len(data)):
        hours = {}
        for j in range(len(data[i])):
            hours[data[i][j][0]] = data[i][j][1].name
        classes[str(i)] = hours

    with open('data/best.json', 'w') as f:
        f.writelines(json.dumps(classes, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    
    population = Population(subjects, teachers, mutationRate, populationSize)

    for i in range(generations):
        if generations == 1:
            population.evaluate(calcPerfect=True)
            perfectFit = population.perfectFit
        else:
            population.evaluate()
        average = population.calcAverage(populationSize, i+1)
        population.generate()
        print "perfect is: " + colored(str(perfectFit), 'blue') + " best is: "  + colored(str(population.best), 'green') + " and worst is: " + colored(str(population.worst), 'red') + " average is: " + colored(str(average), 'yellow')
    
    writeRes(population.bestData)

if __name__ == "__main__":
    main()