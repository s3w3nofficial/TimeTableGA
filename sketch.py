from termcolor import colored
import sys

sys.setrecursionlimit(100000000)

from population import Population
from teacher import Teacher

subjects = [
    ['M','V','A','C','C','V','Z','Z','C'],
    ['D','M','M','C','C','A'],
    ['Z','F','F','C','A','C'],
    ['M','V','A','F','F','A','D']
];

teachers = []
teachers.append(Teacher('T1', ['M','V','A','D','C','F','Z']))
teachers.append(Teacher('T2', ['M','V','A','D','C','F','Z']))
teachers.append(Teacher('T3', ['M','V','A','D','C','F','Z']))
teachers.append(Teacher('T4', ['M','V','A','D','C','F','Z']))

mutationRate = 0.01
populationSize = 2

generations = 100

def main():
    
    population = Population(subjects, teachers, mutationRate, populationSize)

    for i in range(generations):
        population.evaluate()
        average = population.calcAverage(populationSize, i+1)
        population.generate()
        print "best is: "  + colored(str(population.best), 'green') + " and worst is: " + colored(str(population.worst), 'red') + " average is: " + colored(str(average), 'yellow')

if __name__ == "__main__":
    main()