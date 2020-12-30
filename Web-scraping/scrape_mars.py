#!/usr/bin/env python
# coding: utf-8

# In[56]:


import time
import requests 
import pandas as pd
import pymongo
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape_all():

    data = {
        "news_title": results,
        "news_paragraph": paragraph.text,
        "featured_image": featured_image_url,
        "facts": mars_facts,
        "hemispheres": hemisphere_image_urls

    }

    browser.quit()
    return data

# In[57]:


url = 'https://mars.nasa.gov/news/'
response = requests.get(url)


# In[58]:


soup = bs(response.text, 'html.parser')


# In[59]:


print(soup.prettify)


# In[60]:


results = soup.title.text
print('news_title =', results)


# In[61]:


paragraph = soup.find_all("p")
for paragraph in paragraph:
    print('news_p =', paragraph.text)


# In[62]:


from webdriver_manager.chrome import ChromeDriverManager


# In[63]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[64]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)
time.sleep(1)


# In[65]:


html = browser.html


# In[66]:


image_soup = bs(html, 'html.parser')


# In[67]:


image = image_soup.find('div', class_= 'carousel_items')
image_url = image.article['style']
url = image_url.split('/s')[-1].split('.')[0]
featured_image_url = 'https://www.jpl.nasa.gov' + '/s' + url + '.jpg'
print('featured_image_url=', featured_image_url)


# In[68]:


facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
tables


# In[69]:


df = tables[0]
df.columns = ['Mars_facts', 'Data']
df


# In[70]:


mars_facts = df.to_dict('records')
Table = []
for i in range (0, len(mars_facts)):
    temp = list(mars_facts[i].values())
    Table.append(temp)


# In[71]:


print(mars_facts)


# In[72]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[73]:


hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hem_url)

html = browser.html
soup = bs(html, "html.parser")

h3s = soup.find_all("h3")


# In[74]:


titles = []
for h3 in h3s:
    h3 = str(h3)
    h3 = h3[4:-14]
    titles.append(h3)
titles


# In[75]:


img_urls = []
for title in titles:
    browser.click_link_by_partial_text(title)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    img_urls.append(soup.find("div", class_="downloads").find("a")["href"])
img_urls


# In[76]:


hemisphere_image_urls = []
for title , img_url in zip(titles, img_urls):
    hemisphere_image_urls.append({"title": title, "img_url": img_url})
    
hemisphere_image_urls

