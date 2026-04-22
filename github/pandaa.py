# import pandas as pd
# mydataset= {
#     'cars':["BM","Volvo","Ford"],
#     'passings':[3,7,2]
# }

# myvar=pd.DataFrame(mydataset)
# print(myvar)

import pandas as pd
data= {
    "name":['Riya','Neelu','Biya','Ann','Ben','Rahul','Bob','Charlie','Carol','Krishna'],
    "marks":[34,56,28,37,47,19,28,45,53,49]}
df=pd.DataFrame(data)
# print(df)
print(df.loc[[3,6]])