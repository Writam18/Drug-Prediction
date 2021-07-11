from selenium import webdriver
import time
#import chromedriver_binary  # Adds chromedriver binary to path

w = input("Enter a Drug Name\n")

driver = webdriver.Chrome()

'''
driver.get("https://www.1mg.com/search/all?name="+w)
time.sleep(2)
#style__pro-title___3zxNC

drugs = driver.find_elements_by_class_name('style__pro-title___3zxNC')
time.sleep(10)

drugs_list = []
for p in range(len(drugs)):
    drugs_list.append(drugs[p].text)

print("Alternative Drugs of thheh given drug name is : \n");
print("\n")

for d in range(len(drugs_list)):
	print(drugs_list[d])
'''

'''
driver.get("https://www.1mg.com/drugs/duzela-20-capsule-dr-6326")
time.sleep(2)

#"saltInfo DrugHeader__meta-value___vqYM0"
genericlist = driver.find_elements_by_xpath('//div[@class = "saltInfo DrugHeader__meta-value___vqYM0"]')
#generic = driver.find_elements_by_class_name('saltInfo DrugHeader__meta-value___vqYM0')

generic = genericlist[0].text

print(generic)
'''

driver.get("https://www.1mg.com/search/all?name="+w)

elements = driver.find_elements_by_css_selector("div.style__horizontal-card___1Zwmt a")

link1 = elements[0].get_attribute("href")
#print(link1)

driver.get(link1)

genericlist = driver.find_elements_by_xpath('//div[@class = "saltInfo DrugHeader__meta-value___vqYM0"]')
generic = genericlist[0].text

print("The Generic Name of the given drug is : "+generic)
driver.get("https://www.1mg.com/search/all?name="+generic+"&filter=true&sort=rating")

drugs = driver.find_elements_by_class_name('style__pro-title___3zxNC')
time.sleep(10)

drugs_list = []
for p in range(len(drugs)):
    drugs_list.append(drugs[p].text)
    
print("\n")
print("Alternative Brand Names of Drugs of the above generic name is : \n");
print("\n")

for d in range(len(drugs_list)):
	print(drugs_list[d])

print("\n")
print("The drugnames are sorted according to Average Customer Rating")

driver.close()

