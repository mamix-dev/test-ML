import random as rd
import numpy as np
import matplotlib.pyplot as plt

class creatingData:
    """"Generally followed https://medium.com/analytics-vidhya/polynomial-regression-in-tensorflow-53f958cef2d2 to put this."""
    def __init__(self, degree):
        self.degree = degree
        self.x, self.y = None, None
    
    def createData(self):
        """Creates a random polynomial function and associated values"""
        self.roots = np.random.uniform(-5,5, self.degree)
        polyCoefficients = np.poly(self.roots)
        self.x = np.arange(-50,50)
        self.y = np.polyval(polyCoefficients, self.x)
    
    def plotData(self):
        """Plots data using matplotlib"""
        self.createData()
        plt.plot(self.x, self.y, 'green')
        plt.show()

    def saveData(self):
        self.createData()
        dataFile = open('./src/data/output.csv', 'w')
        for ind in self.x:
            dataFile.write(f'{self.x[ind]}, {self.y[ind]}\n')
        dataFile.close()
        actualData = open('./src/data/actual.txt', 'w')
        actualData.write(f'{self.degree}\n')
        for x in self.roots:
            actualData.write(f'{x}\n')

if __name__ == '__main__':
    main = creatingData(5)
    main.saveData()