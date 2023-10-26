import matplotlib
matplotlib.use("WXAgg")
import matplotlib.pyplot as plt
import numpy as np
#plt.ioff()
print(matplotlib.is_interactive())

x = np.arange(1,11) 
y = 2 * x + 5 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()