import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.moh.gov.sg/covid-19')
soup = BeautifulSoup(page.content,'html.parser')
dataset = soup.find_all('span',attrs={'style':'font-size: 20px;'})
dataset_ = soup.find_all('font',attrs={'color':'#00b050'})
activeCases = dataset_[0].string
activeCases_Critical = dataset_[1].string
dataset2 = soup.find_all('font',attrs={'color':'#00b050'})
activeCases_Stable = dataset2[1].string
dataset3 = soup.find_all('span',attrs={'style':'color: rgb(0, 176, 80); font-family: Arial; font-size: 20px;'})
discharged = dataset3[0].string[1:4]
dataset4 = soup.find_all('font',attrs={'color':'#ff0000'})
deathCount = dataset4[0].contents[0].string
dataset5 = soup.find_all('span',attrs={'style':'caret-color: rgb(0, 176, 240);'})
importedCases = dataset5[0].string
dataset6 = soup.find_all('span',attrs={'style':'color: rgb(0, 176, 240);'})
importedCases_Visitors = dataset6[0].string
dataset7 = soup.find_all('strong',attrs={'style':'font-family: Arial; font-size: 20px; caret-color: rgb(0, 176, 240);'})
importedCases_Residents_LongTermPass = dataset7[0].string
print ("activeCases: " + activeCases)
print ("activeCases_Critical: " +activeCases_Critical)
print ("activeCases_Stable: " +activeCases_Stable)
print ("deathCount: " +deathCount)
print ("importedCases: " + importedCases)
print ("importedCases_Residents_LongTermPass: " + importedCases_Residents_LongTermPass)
print ("importedCases_Visitors: " +importedCases_Visitors)
