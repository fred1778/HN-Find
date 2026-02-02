import sys
import os
import re
import csv
import datetime

from bs4 import BeautifulSoup
from urllib import request
from pprint import pprint

#https://news.ycombinator.com

term = " AI "
csv_headers = ["URL", "Title", "Extract"]
file_data = []
dt_str = str(datetime.datetime.now())
file_name = "hacker_news_" + term +  " at " + dt_str + ".csv"


def writeExtracts(extracts, url, title):
   for ex in extracts:
      writeEntry([url, title, ex])


def writeEntry(row_data):
   file_data.append(row_data)


def generateExtracts(indexes, pText):
   extracts = []
   for i in indexes:
      extract = ""
      if i < 150 :
         leading = 0
      else:
         leading = i - 150

      if len(pText) < (i + 150):
         trailing = len(pText)
      else:
         trailing =  i + 150
      extract += pText[leading:trailing]
      extracts.append(extract)
   return extracts
   






def stripText(soup, url):
   #extract readable text 
   count = 0
   title = "-"
   if soup.title is not None:
      title = soup.title.string

   txt = ""

   for p in soup.find_all('p'):
      txt += p.getText().strip().rstrip()
      
   if txt != '\n':
      pprint(txt)
      indexes = [match.start() for match in re.finditer(term, txt)]
      writeExtracts(generateExtracts(indexes, txt), url, title)
      count = len(indexes)
   




   

def pageCheck(page):
   pageSoup = makeSoup(page)
   if pageSoup is not None:
      stripText(pageSoup, page)
   else:
     print("Cannot handle", '\n')


def makeSoup(page):
   try:
    response = request.urlopen(page)
    #print(response.reason)
    return BeautifulSoup(response, 'html.parser')
   except:
      print("HTTP Error", '\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# start point...

#setup

#base url
hn_url = "https://news.ycombinator.com"
soup = makeSoup(hn_url)

#table element containing list if of links
contentTable = soup.body.center.table.find_all('td')
manifest = []

for tbl_data in contentTable:
    link_tag = tbl_data.find_all('a')
    if len(link_tag) > 0:
     extLink = link_tag[0]['href']
     #isolate external links
     if(extLink.startswith("http")):
        manifest.append(extLink)
for ln in manifest:
  # pprint("Getting data for " + ln + '\n')
   pageCheck(ln)


# create csv output
with open(file_name, 'w', newline='') as f:
   writer = csv.writer(f)
   writer.writerow(csv_headers)
   writer.writerows(file_data)


   
