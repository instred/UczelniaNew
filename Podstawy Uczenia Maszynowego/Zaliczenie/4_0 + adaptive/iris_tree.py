import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz
import os

# Needed for tree visualization
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

PATH = 'iris.csv'

# Loading
iris_df = pd.read_csv("iris.csv")

# All data must be in number form, so we do mapping with variety
iris_df["variety"] = iris_df["variety"].map({'Setosa':0,'Versicolor':1,'Virginica':2})

# Prepraring data and target
X = iris_df.drop(["variety"],axis=1).values
y = iris_df["variety"].values

# print(X)

# Splitting it for train and test 70/30
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, stratify=y)

# Experimenting - best one is 3
# for depth in range(1,8):
#     decision_tree = tree.DecisionTreeClassifier(max_depth = depth)
#     decision_tree.fit(train_X, train_y)

#     y_pred = decision_tree.predict(test_X)
#     acc_decision_tree = round(decision_tree.score(test_X, test_y) * 100, 2)
#     print(f'Depth: {depth}, tree acc: {acc_decision_tree}')

decision_tree = tree.DecisionTreeClassifier(max_depth = 3)
decision_tree.fit(train_X, train_y)

y_pred = decision_tree.predict(test_X)


dot_tree = tree.export_graphviz(decision_tree,
                            max_depth = 4,
                            impurity = True,
                            feature_names = list(iris_df.drop(["variety"],axis=1)),
                            class_names = ['Setosa', 'Versicolor', 'Virginica'],
                            rounded = True,
                            filled= True)

graph = graphviz.Source(dot_tree)
graph.format = "png"
graph.render("tree_image")

acc_decision_tree = round(decision_tree.score(test_X, test_y) * 100, 2)
print(f'Depth: 3, tree acc: {acc_decision_tree}')
     


