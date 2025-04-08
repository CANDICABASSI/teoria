import matplotlib.pyplot as plt

label=["a","b","c","d"]
datos=[25,56,76,25]
colores=["gold","lightcoral","lightskyblue","lightgreen"]

plt.pie(datos,labels=label,colors=colores,autopct="%1.1f%%",startangle=140)
plt.axis("equal")
plt.show()