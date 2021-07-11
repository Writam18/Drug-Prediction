import numpy as np
import pandas as pd

df1 = pd.read_csv('drugname1.csv')
df1 = df1[['Condition','Drug Name']]

df2 = pd.read_csv('drugsentiment.csv')
df2 = df2[['drugName','average_sentiment']]

df3 = pd.read_csv('drugrating.csv')
df3 = df3[['DrugName','Average Rating']]

#snt = pd.DataFrame(columns=['drugName', 'average_sentiment'])
		
def finddrug(x):
  w= df1.loc[df1['Condition'] == x]['Drug Name']
  v = w.item()
  u = v.split(',')
  return u
  
def sortdrug(d):
	snt = pd.DataFrame(columns=['drugName', 'average_sentiment'])
	for i in range(len(d)):
		s=df2[df2['drugName']==d[i]]
		snt=pd.concat([snt,s])
	m=snt.sort_values(by='average_sentiment', ascending=False).reset_index(drop=True)['drugName'].tolist()
	return m

r_ls=[]

def ratedrug(m):
  for i in m:
    q=df3.loc[df3['DrugName']==i]['Average Rating']
    r_ls.append((i,q.item()))
  df_r=pd.DataFrame(r_ls,columns=["Drug Name","Average User Rating"])
  return df_r


condition=input("Enter a Condition\n")
condition=condition.lower()
drugname=finddrug(condition)
druglist=sortdrug(drugname)
drugdata=ratedrug(druglist)

'''
print('\n')
for i in range(len(d)):
  print(d[i])
'''
'''
print('\n')
print("Showing Drug Values on the basis of sentiment given by users\n")
for i in range(len(c)):
  print(c[i])
'''
print('\n')
print("Showing Drug Names and Average User Rating for {} \n".format(condition))
print(drugdata)
print('\n')
print("Drug Names are sorted on the basis of sentiment of reviews given by users\n")
