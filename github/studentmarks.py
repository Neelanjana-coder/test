import pandas as pd
import matplotlib.pyplot as py

df=pd.read_csv("studentmarks.csv")
print(df)
py.bar(df["names"],df["total"])
py.xlabel("names")
py.ylabel("total marks")
py.title("Students Marks Graph")
py.show()
# py.pie(df["names"],df["eng"],df["maths"],df["chemistry"],df["physics"])
# py.show()