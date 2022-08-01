import random as rd
import numpy as np
import matplotlib.pyplot as plt

class creatingData:
    """"Generally followed https://medium.com/analytics-vidhya/polynomial-regression-in-tensorflow-53f958cef2d2 to put this."""
    def __init__(self, degree):
        self.degree = degree
        self.x, self.y = None, None
    
    def linear_function(self, x):
            return self.m * x + self.b

    def createData(self):
        """Creates a random polynomial function and associated values"""
        self.m = rd.randint(0,10)
        self.b = rd.randint(0,10)
        self.x = np.arange(0,500)
        self.y = []
        for val in self.x:
            self.y.append(self.linear_function(val))
        print(self.y)


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
        actualData.write('----M----\n')
        actualData.write(f'{self.m}\n')
        actualData.write('----B----\n')
        actualData.write(f'{self.b}\n')
        actualData.close()

if __name__ == '__main__':
    main = creatingData(2)
    main.saveData()