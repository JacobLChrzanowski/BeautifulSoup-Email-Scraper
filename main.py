############################################################
##                                 /##` ###` ###`   ##  ## #
##  Jacob L. Chrzanowski           #  #  #    #    #  ## ##
##    BeautifulSoup Email Scraper  ###   #    #     ##  #
##                                 #  \ ###   #    # ## 
######################################################


import code
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = "https://www.rit.edu/its/about/staff"
url = "https://pastebin.com/37wZg26w"
html = urlopen(url)
bsObj = BeautifulSoup( html.read(), "html.parser")

#emails = re.findall(r"[A-Za-z0-9._%+-]+(\@|\[at\]|\[\@\])[A-Za-z0-9.-]+(\.|\['dot'\]|\[.\])[A-Za-z]{2,4}", str(bsObj))

bsObj = str(bsObj)

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", bsObj)
visited_emails = set()
for email in emails:
    #print(email)

    if email not in visited_emails:
            print('found email type1: ' + str(email))
            visited_emails.add(email)

emails = re.findall(r"[A-Za-z0-9._%+-]+\[at\][A-Za-z0-9.-]+\.[A-Za-z]{2,4}", bsObj)
visited_emails = set()
for email in emails:
    #print(email)

    if email not in visited_emails:
            print('found email type2: ' + str(email))
            visited_emails.add(email)

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\[dot\][A-Za-z]{2,4}", bsObj)
visited_emails = set()
for email in emails:
    #print(email)

    if email not in visited_emails:
            print('found email type3: ' + str(email))
            visited_emails.add(email)

emails = re.findall(r"[A-Za-z0-9._%+-]+\[at\][A-Za-z0-9.-]+\[dot\][A-Za-z]{2,4}", bsObj)
visited_emails = set()
for email in emails:
    #print(email)

    if email not in visited_emails:
            print('found email type4: ' + str(email))
            visited_emails.add(email)










# links = bsObj.findAll("link")
# for link in links:
#     link = str(link)
    
#     if r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}' in link:
#         print(link)



#     # reg = re.search(r'[\w\.-]+@[\w\.-]+', link)
#     # reg.group(0)

# code.interact(local=locals())
# print(bsObj.prettify()[0:100])

# print('\n\n\n')

# #print([a["href"] for a in bsObj.select("a[href^=mailto:]")])





# line = "should we use regex more often? let me know at  321dsasdsa@dasdsa.com"
# match = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', line)
# match.group(0)

quit()