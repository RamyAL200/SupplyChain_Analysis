#!/bin/python

# This just verifies that the dataframes are equal
import pandas as pd

df1 = pd.read_csv(r"C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\Ramy_Names.csv")
df2 = pd.read_csv(r"C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\Reassembled_CSV.csv")

df1Sorted = df1[sorted(df1.columns)]
df2Sorted = df2[sorted(df2.columns)]

print(df1Sorted.head(10))
print(df2Sorted.head(10))

print(f"Are the columns identical?: {df1Sorted.columns == df2Sorted.columns}")
equality = df1Sorted.equals(df2Sorted)
print(f"Are they equal?: {equality}")