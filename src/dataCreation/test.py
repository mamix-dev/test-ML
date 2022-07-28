import pandas as pd
import random as rd
import numpy as np

class creatingData():

    def createList(rootFunction, variation, sampleCount):
        listOfNumbers = []
        for x in range(sampleCount):
            listOfNumbers.append(rootFunction(x,-3,5) + rd.randint(variation[0],variation[1]))

    def quadraticFunction(x, h, k):
        return np.power((x-h),2)+k


mainDF = pd.DataFrame()