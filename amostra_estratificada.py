import panda as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
iris['class'].value_counts()

 x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                                test_size = 0.5, stratify = iris.iloc[:,4])

y.value_counts()

infert = pd.read_csv('infert.csv')
infert['education'].value_counts()

X1, _, Y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], 
                               test_size = 0.6, stratify = infert.iloc[:, 1])
Y1.value_counts()