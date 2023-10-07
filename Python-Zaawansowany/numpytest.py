import numpy as np
import matplotlib.pyplot as plt

# simple linear regression

# least squares method for linear regression
# squares being the difference between actuall va

x = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125])
y = np.array([5, 20, 14, 32, 22, 38, 41, 33, 28, 45, 61, 50, 55])

# avg of elements in arrays x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# difference of each element in array with the array avg
x_diff = x - x_mean
y_diff = y - y_mean
x_diff_squared = x_diff ** 2

# slope of the regression line - b1
m = np.sum(x_diff * y_diff) / np.sum(x_diff_squared)

# interception of y axis by the regression line - b0
b = y_mean - m * x_mean

# simple linear regression - f(x) = b0 + b1 * x
def predict(x):
    return b + m * x

# function to create a graph
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()


plot_regression_line(x, y, (b, m))