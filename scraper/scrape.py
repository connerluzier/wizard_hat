import csv
import requests
from BeautifulSoup import BeautifulSoup

#this is the url to grab the information from:
url = 'https://www.us-proxy.org/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        print cell.text.replace('no','')
        list_of_rows.append(list_of_cells)

outfile = open("./fresh_proxies.txt")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
