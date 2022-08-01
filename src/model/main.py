import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sys

class Model:

    def getData(self):
        column_names = 'x', 'y'
        raw_data = pd.read_csv('./src/data/output.csv', names = column_names, index_col=False)
        self.xTrain, self.xTest, self.yTrain, self.yTest = train_test_split(raw_data['x'], raw_data['y'], shuffle = True, test_size = .2)

    def trainModel(self):
        self.getData()
        linear_model = LinearRegression()
        xTrain = self.xTrain.values.reshape(-1,1)
        yTrain = self.yTrain.values.reshape(-1,1)
        self.reg = linear_model.fit(xTrain, yTrain)

    def predict(self, xVal):
        self.trainModel()
        prediction = self.reg.predict([[xVal]])
        return prediction

if __name__ == "__main__":
    model = Model()
    print(model.predict(sys.argv[1])[0][0])
