import sys
import pandas as pd

in_fpkm = sys.argv[1]
in_final = sys.argv[2]
out_fpkm = sys.argv[3]

df1 = pd.read_table(in_fpkm)
df2 = pd.read_table(in_final)
print(df1.columns)
print(df1.shape)
print(df2.columns)
print(df2.shape)
df = df1.merge(right=df2,how="right",left_on="transcript_id",right_on="transcript_id_1")
df = df.drop(labels="transcript_id_1",axis=1)
df.to_csv(out_fpkm,index=False)
print(df.shape)
print("Everything is ok!")
