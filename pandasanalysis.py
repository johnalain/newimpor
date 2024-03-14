#https://youtu.be/ZyhVh-qRZPA?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#https://insights.stackoverflow.com/survey data from stackoverflow
#https://youtu.be/Kg1Yvry_Ydk venv how to use it
#https://youtu.be/HW29067qVWk how to use jupyter notebook
import pandas as pd
df = pd.read_csv('/Users/michelkadi/Desktop/datachannel.csv')
print(df)
print('@'*30)
a = df.shape
print(a)#output:(3, 5)(3rows, 5columns)
