
"""Python code to scrap the points table and visualize using matplotlib
https://en.wikipedia.org/wiki/2016_Pro_Kabaddi_League_season_(June)"""

#Python modules
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

# url of the search page and get the search url using requests
r=requests.get("http://en.wikipedia.org/wiki/2016_Pro_Kabaddi_League_season_(June)")

#create a BeautifulSoup object 'soup' for the content
soup=BeautifulSoup(r.content,'html.parser')

# search for table of class "wikitable"
searched = soup.select('table.wikitable')

# the third table of class "wikitable" contains the points table
points_table=searched[2]

#copy the contents of headings to "headings"
# and body to "body"
headings=points_table.select('th')
body=points_table.select('td')

#create two empty lists to extract and sotre the
# data from the headings and body
head_parsed=[]
values=[]

# append the values in heading to "head_parsed"
#this includes the heading of each coloumn
for th in headings:
	head_parsed.append(th.get_text())
#print (head_parsed)
# append the values in heading to "head_parsed"
# this include points and other data of all the rows
for td in body:
	values.append(td.get_text())

#create an empty list for all the values in "head_parsed"
# i.e create empty lists for headings of all coloumns
for i in head_parsed:
	exec("%s=[]"%(i))
#print (values)

#append the values to the corresponding list
for i in range(len(values)):
	exec("%s.append('%s')" % (head_parsed[i%6],values[i]))



# now, the Points of each team is stored in "Points"
# and the team names are stored in "Teams"

y_pos=np.arange(len(Team))
plt.figure(1)

# names of the teams as x axis identifiers
plt.xticks(y_pos,Team)
# points are the bar graph plot along y axis
plt.bar(y_pos, Points, 0.4,align='center', alpha=0.5)



plt.show()