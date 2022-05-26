import pandas as pd

Id =3
df = pd.read_csv("StudentDetails\StudentDetails.csv")
aa=df.loc[df['Id'] == Id]['Name'].values

# print(df)
print(aa)
