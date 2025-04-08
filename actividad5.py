import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,5,8,11,14,17,20,23,26,29]

plt.scatter(x,y,color="blue",marker="o")
plt.title("grafico")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.show()