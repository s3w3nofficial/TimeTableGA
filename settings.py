from configparser import ConfigParser
from TimeTablePython.handler import Handler

def main():

    cfg = ConfigParser()
    cfg.read('config.ini')

    data = cfg.get('configData', 'data')
    mutationRate = cfg.getfloat('configData', 'mutationRate')
    populationSize = cfg.getint('configData', 'populationSize')
    generations = cfg.getint('configData', 'generations')

    handler = Handler(data, mutationRate, populationSize, generations)
    handler.createPopulation()
    handler.run()
    handler.writeRes()

if __name__ == "__main__":
    main()