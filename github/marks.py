import pandas as pd
import matplotlib.pyplot as py

df=pd.read_csv("marks.csv")
print(df)
py.bar(df["name"],df["marks"])
py.xlabel("Students")
py.ylabel("Marks")
py.title("Students Marks Graph")
py.show()


py.scatter(df["name"],df["marks"])
py.xlabel("Students")
py.ylabel("Marks")
py.title("Students Marks Graph")
py.show()