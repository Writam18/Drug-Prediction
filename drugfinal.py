from selenium import webdriver
import time
import numpy as np
import pandas as pd


df1 = pd.read_csv('drugname1.csv')
df1 = df1[['Condition','Drug Name']]

df2 = pd.read_csv('drugsentiment.csv')
df2 = df2[['drugName','average_sentiment']]

df3 = pd.read_csv('drugrating.csv')
df3 = df3[['DrugName','Average Rating']]

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

def scrapdrug(w):
	driver.get("https://www.1mg.com/search/all?name="+w)
	elements = driver.find_elements_by_css_selector("div.style__horizontal-card___1Zwmt a")
	link1 = elements[0].get_attribute("href")
	driver.get(link1)
	genericlist = driver.find_elements_by_xpath('//div[@class = "saltInfo DrugHeader__meta-value___vqYM0"]')
	generic = genericlist[0].text
	print("The Generic Name of the given drug is : "+generic)
	driver.get("https://www.1mg.com/search/all?name="+generic+"&filter=true&sort=rating")
	drugs = driver.find_elements_by_class_name('style__pro-title___3zxNC')
	time.sleep(15)
	drugs_list = []
	for p in range(len(drugs)):
		drugs_list.append(drugs[p].text)
	return drugs_list
		
		
try:			
	print("Do you want search a drugname by \n 1.Condition \n 2.Drugname")
	op = input("Enter 1 or 2\n")

	print(op)

	if op=="1":

		condition=input("Enter a Condition : \n")
		condition=condition.lower()
		drugname=finddrug(condition)
		druglist=sortdrug(drugname)
		drugdata=ratedrug(druglist)
		print('\n')
		print("Showing Drug Names and Average User Rating for {} \n".format(condition))
		print(drugdata)
		print('\n')
		print("Drug Names are sorted on the basis of sentiment of reviews given by users\n")
		  
	elif op=="2":
		
		w = input("Enter a Drug Name\n")
		driver = webdriver.Chrome()
		drugs_list=scrapdrug(w)
		print('\n')
		print("Alternative Brand Names of Drugs of the above generic name is : \n")
		print('\n')
		for d in range(len(drugs_list)):
			print(drugs_list[d])
		print('\n')
		print("Drugnames are sorted according to Average Customer Rating")
		print('\n')
		driver.close()
		
	else:
		print("Invalid Choice")

	print('\n')
	print("Thanks for using the application....Take Care..")
	print('\n')
except Exception as e:
	print(str(e))
	pass
