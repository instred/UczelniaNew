import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
import seaborn as sns
from sklearn.model_selection import KFold
import graphviz
import os

# Needed for tree visualization
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

PATH_TRAIN = 'train.csv'
PATH_TEST = 'test.csv'

train = pd.read_csv(PATH_TRAIN)
test = pd.read_csv(PATH_TEST)

# print(train.head(5))
pd.set_option('display.max_columns', 9)
pd.options.display.width = 0

# print('NaN: ', sum(train['Age'].isna()), ' / ', len(train['Age']))

l_col = ['Survived','Pclass','Sex']

train['Age'] = train['Age'].fillna(train.groupby(l_col)['Age'].transform('mean'))

nan = train[train['Age'].isna()]
# print('NaN after filling: ', len(nan), ' / ', len(train['Age']))

PassengerId = test['PassengerId']
original_train = train.copy()

full_data = [train, test]

# Mapping Cabins 
train['Has_Cabin'] = train["Cabin"].apply(lambda x: 0 if type(x) == float else 1)
test['Has_Cabin'] = test["Cabin"].apply(lambda x: 0 if type(x) == float else 1)

# Create new feature FamilySize as a combination of SibSp and Parch
for dataset in full_data:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

# Create new feature IsAlone from FamilySize
for dataset in full_data:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1

# Remove all NULLS in the Embarked column
for dataset in full_data:
    dataset['Embarked'] = dataset['Embarked'].fillna('S')

# Mapping Embarked
    dataset['Embarked'] = dataset['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

 # Mapping Sex
    dataset['Sex'] = dataset['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

drop_elements = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'SibSp', 'Fare']
train = train.drop(drop_elements, axis = 1)
test  = test.drop(drop_elements, axis = 1)
# print(train.head(4))

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
features = sns.heatmap(train.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
# plt.show()

cv = KFold(n_splits=10)            # Desired number of Cross Validation folds
accuracies = list()
max_attributes = len(list(test))
depth_range = range(1, max_attributes + 1)

# Testing max_depths from 1 to max attributes

for depth in depth_range:
    fold_accuracy = []
    tree_model = tree.DecisionTreeClassifier(max_depth = depth)

    # print("Current max depth: ", depth, "\n")

    for train_fold, valid_fold in cv.split(train):
        f_train = train.loc[train_fold] # Extract train data with cv indices
        f_valid = train.loc[valid_fold] # Extract valid data with cv indices

        model = tree_model.fit(X = f_train.drop(['Survived'], axis=1), 
                               y = f_train["Survived"]) # We fit the model with the fold train data
        valid_acc = model.score(X = f_valid.drop(['Survived'], axis=1), 
                                y = f_valid["Survived"])# We calculate accuracy with the fold validation data
        fold_accuracy.append(valid_acc)

    avg = sum(fold_accuracy)/len(fold_accuracy)
    accuracies.append(avg)

    # print("Accuracy per fold: ", fold_accuracy, "\n")
    # print("Average accuracy: ", avg)
    # print("\n")

# df = pd.DataFrame({"Max Depth": depth_range, "Average Accuracy": accuracies})
# df = df[["Max Depth", "Average Accuracy"]]
# print(df.to_string(index=False))

y_train = train['Survived']
X_train = train.drop(['Survived'], axis=1).values 
X_test = test.values

# print(X_train, y_train)
# print(X_test)

decision_tree = tree.DecisionTreeClassifier(max_depth = 5)
decision_tree.fit(X_train, y_train)

y_pred = decision_tree.predict(X_test)
submission = pd.DataFrame({
        "PassengerId": PassengerId,
        "Survived": y_pred
    })


# submission.to_csv('predict.csv', index=False)

dot_tree = tree.export_graphviz(decision_tree,
                            max_depth = 5,
                            impurity = True,
                            feature_names = list(train.drop(['Survived'], axis=1)),
                            class_names = ['Died', 'Survived'],
                            rounded = True,
                            filled= True )
     
graph = graphviz.Source(dot_tree)
graph.format = "png"
graph.render("tree_image")
        

acc_decision_tree = round(decision_tree.score(X_train, y_train) * 100, 2)
print(acc_decision_tree)