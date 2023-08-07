# if You want to scraper a website
# 1 Use Api
# Html Web Scraping Using Some Tool like bs4

#  I nstall all requiment 


import requests
from bs4 import BeautifulSoup
url="https://www.linkedin.com/jobs/search/?currentJobId=3655328471&keywords=it%20python%20job"


# step 1: Get The Element
r=requests.get(url=url)
htmlContent=r.content
# print(htmlContent)

# Step : Parse The Html
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)


# Step 3 : Html Tree Traversel



# Commonly used  type of objects
# print(type(title)) # 1: Tag
# print(type(title.string)) # 2:NavigableString
# print(type(soup))# 3: Beautifulsoup
# 4: Comment
# markup="<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup=markup)
# print(type(soup2.p.string))


# Get The title of the Html Page
# title=soup.title

# Get The Paragraph from the pages
# paras=soup.find_all('p')
# print(paras)



# Get All The Ancher tag from the pages  
# a=soup.find_all('a')
# all_links=set()
# Get Al  The Link From the Pages
# for link in a:
#     if(link.get('href')!='#'):
#         linkText="https://www.linkedin.com" + link.get('href')
#         all_links.add(linkText)
#         print(linkText) 






# idOfany=soup.find(id="artdeco-toasts__wormhole")
# for ele in idOfany.contents:
#     print(ele)


# idOfanyitem=soup.find(id="artdeco-toasts__wormhole")
# for item in idOfanyitem.string:
#     print(item)



# idOfanyitem=soup.find(id="artdeco-toasts__wormhole")
# for item in idOfanyitem.stripped_strings:
#     print(item)


# idOfanyitem=soup.find(id="artdeco-toasts__wormhole")
# for item in idOfanyitem.string:
#     print(item)


idOfanyitem=soup.find(id="artdeco-toasts__wormhole")
print(idOfanyitem.parents)


















# Get classes  of any element in the html pages
# cl=soup.find('a')['class']
# print(cl)




# Find all the element with clas  lead
# cl=soup.find_all("p",class_="btn-md")
# print(cl)


# Get text from the tags/soup
# tx=soup.find('p').get_text()
# print(tx)


# Get  all text from the soup
# tx=soup.get_text()
# print(tx)






