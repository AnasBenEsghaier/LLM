import pandas as pd

columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income"
]

df = pd.read_csv(
    "dataset/adult.data",
    names=columns,
    skipinitialspace=True
)

#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df['income'])

for each in columns:
    print(df[each].value_counts())
    print("-------------------------------")