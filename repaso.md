import pandas as pd
df=pd.read_csv("users.csv") 
print(df[df["pais"]=='France'].sort_values(['edad'], ascending = True).head(5), df[df["pais"]=='France']["edad"].mean())
print(df[df["pais"]=='Australia'].sort_values(['edad'], ascending = True).head(5), df[df["pais"]=='Australia']["edad"].mean())
