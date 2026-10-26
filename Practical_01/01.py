import pandas as pd
data={

    "Name":["ABC","PQR","XYZ"],
    "Marks":[1,2,3]
}
df = pd.DataFrame(data)
print(df)




#program template 
#Program :01
#Aim: To perform data subsetting , sorting, and grouping operations to organize and analyze dataset attributes

import pandas as pd

df= pd.DataFrame({
    "Name":["Ritu","Priya","rahul","tushar"],
     "Dept":["CSE","IT","CSE","IT"],
     "Marks": [85,88,98,78]

})

print("Original Data:\n",df)


#Data Subsetting
print("\nSubset (Marks>50):\n", df[df["Marks"]>50])


#Sorting in ascending order
print("\nSorted by Marks (Ascending):\n",df.sort_values("Marks"))


#Sorting in descending order
print("\nSorted by Marks (descending):\n",df.sort_values("Marks",ascending=False))

#Grouping
print("\ngrouped (Averege Marks by Department) :\n", df.groupby("Dept")["Marks"].mean())


#statistical operations
print("\nMean", df["Marks"].mean())
print("\nMedian", df["Marks"].median())
print("MOde=")
print(df["Marks"].mode())