
# coding: utf-8

# In[ ]:

import codecs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import urllib
import requests
from BeautifulSoup import BeautifulSoup

SearchWords=raw_input('Give the search word : ')

driver = webdriver.Chrome('C:/Users/ILLEN/Anaconda2/selenium/webdriver/chrome/chromedriver.exe')
driver.get('http://search.daum.net/search?w=blog&f=section&SA=tistory&lpp=10&nil_profile=vsearch&nil_src=tistory&q='+SearchWords)

driver.find_element_by_css_selector('#sourceOption > dd:nth-child(4) > a').click()

#make a file
f=codecs.open('Tistory_'+SearchWords+'.txt','a','utf-8')

# Crawling links the first page
hrefs=driver.find_elements_by_css_selector('a.f_url')
for href in hrefs:
    linkText=href.get_attribute('href') + '\n'
    f.write(linkText)
    print linkText
    
#Clink n pages and Crawling pages
for i in range(4,12):
    driver.find_element_by_css_selector('#pagingArea > span > a:nth-child('+str(i)+')').click()
    hrefs=driver.find_elements_by_css_selector('a.f_url')
    for href in hrefs:
        linkText=href.get_attribute('href') + '\n'
        f.write(linkText)
        print linkText
f.close()    
driver.close()       


# In[ ]:

# Open the file        
F=codecs.open('Tistory_'+SearchWords+'.txt','r','utf-8')
Frs=F.readlines()
F.close()

# Make a new file
FF=codecs.open('Tistroy_Words'+SearchWords+'.txt','w','utf-8')

for Fr in Frs:
    link=Fr.rstrip()
    database=requests.get(link).text
    database.encode('utf-8')
    soup=BeautifulSoup(database)
    psts=soup.findAll('p')
    for pst in psts:
        print pst.text
        FF.write(pst.text)      
FF.close()


# In[ ]:

# Word Cloud

from os import path
from wordcloud import WordCloud

d = path.dirname('wordcloud')

# Read the file.
text = open(path.join(d, 'Tistroy_Wordseuro trip.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[ ]:

get_ipython().magic(u'pinfo ')
import codecs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

print '*****Hello! Welcome! :D ******\n'

while True:
    
    Locate=raw_input('Please write the city, region, district or specific hotel. : ') #searching locate
    CheckInYear=raw_input('Please Write Check-In year. (yyyy) : ')
    CheckInMonth=raw_input('Please Write Check-In month. (mm) : ')
    CheckInDay=raw_input('Please Write Check-In day. (dd) : '),'\n'
    CheckOutYear=raw_input('Please Write Check-Out year. (yyyy) : ')
    CheckOutMonth=raw_input('Please Write Check-Out month. (mm) : ')
    CheckOutDay=raw_input('Please Write Check-Out day. (dd) : ')
    
    # Make a txt file
    f=codecs.open('hotels_'+str(Locate)+'.txt','w','utf-8')
        
    # Start WebDriver
    driver = webdriver.Chrome('C:/Users/ILLEN/Anaconda2/selenium/webdriver/chrome/chromedriver.exe')
    driver.get('http://booking.com')
    
    # Input Location
    driver.find_element_by_css_selector("#ss").send_keys(Locate) #CityName
    
    #Input Check-In-Out Data
    driver.find_element_by_css_selector(".sb-date-field__input.-year").send_keys(CheckInYear) #checkin year
    driver.find_element_by_css_selector(".sb-date-field__input.-month").send_keys(CheckInMonth) #checkin month
    driver.find_element_by_css_selector(".sb-date-field__input.-day").send_keys(CheckInDay) #checkin day
    driver.find_element_by_css_selector('div.c2-wrapper.c2-wrapper-s-hidden.c2-wrapper-s-position-undefined.c2-wrapper-s-checkout.c2-wrapper-s-has-arrow > div.sb-date-field.b-datepicker > div > div.sb-date-field__controls > input.sb-date-field__input.-year').send_keys(CheckOutYear) #checkout year
    driver.find_element_by_css_selector('div.c2-wrapper.c2-wrapper-s-hidden.c2-wrapper-s-position-undefined.c2-wrapper-s-checkout.c2-wrapper-s-has-arrow > div.sb-date-field.b-datepicker > div > div.sb-date-field__controls > input.sb-date-field__input.-month').send_keys(CheckOutMonth) #checkout month
    driver.find_element_by_css_selector('div.c2-wrapper.c2-wrapper-s-hidden.c2-wrapper-s-position-undefined.c2-wrapper-s-checkout.c2-wrapper-s-has-arrow > div.sb-date-field.b-datepicker > div > div.sb-date-field__controls > input.sb-date-field__input.-day').send_keys(CheckOutDay) #checkout day
    
    # Submit
    driver.find_element_by_css_selector(".sb-searchbox__button").submit()
    
    # Filter Price
    #driver.find_element_by_css_selector('#filter_price > div.filteroptions > a:nth-child(1) > div > span.filter_label').click()
    #driver.find_element_by_css_selector('#filter_price > div.filteroptions > a:nth-child(2) > div > span.filter_label').click()
    
    # Hotel Info
    hotelurls=driver.find_elements_by_css_selector("a.hotel_name_link.url")
    hotelurls=driver.find_elements_by_css_selector("a.hotel_name_link.url")
    hotelnames=driver.find_elements_by_css_selector("h3 > a > span")
    hotelnights=driver.find_elements_by_css_selector("th.roomPrice.no_bg > div > span.price_for_x_nights_format")
    hotelprices=driver.find_elements_by_css_selector("b")

    for hotelname, hotelurl,hotelnight, hotelprice in zip(hotelnames, hotelurls, hotelnights, hotelprices) :
        hna=hotelname.text
        hni=hotelnight.text
        hp=hotelprice.text
        hu=hotelurl.get_attribute('href')
        print hna
        print hni, hp
        print hu,'\n'
        lines=hna+'\n'+hni+'_'+hp+'\n'+hu,'\n'
        for line in lines:
            f.write(line)            
    f.close() 
    driver.close()
    
    
    print 'Finish!\n'
    print 'Do you want to search again? (Y / N)'
    c=raw_input()
    if c =='N' or c=='n':
        break


print 'The program is over.'

