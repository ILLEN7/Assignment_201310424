
# coding: utf-8

# In[2]:

import urllib
keyword='벚꽃'
f=urllib.urlopen("http://music.naver.com/search/search.nhn?query=%EB%B2%9A%EA%BD%83&target=track")
mydata=f.read();
pos=mydata.find("트랙 리스트")


# In[6]:

if (pos>0): 
    pos = mydata.find("_title title NPI=", pos);
    pos = mydata.find("title=", pos+20)
    pos2 = mydata.find("\"", pos+8)
    print "---", mydata[pos+7:pos2]
    print len(mydata)


# In[7]:

import re
p=re.compile('title=".*벚꽃.*"')
res=p.findall(mydata)


# In[9]:

for item in res:
    print item


# In[7]:

import lxml.html
from lxml.cssselect import CSSSelector
html=lxml.html.fromstring(mydata)
sel=CSSSelector('#content > div:nth-child(3) \
> div._tracklist_mytrack.tracklist_table._searchTrack \
> table > tbody > tr:nth-child(2) > td.name > a.title')
results=sel(html)


# In[9]:

len(results)


# In[14]:

for result in results:
    print result.text_content()


# In[17]:

import lxml.html
import requests
keyword='벚꽃'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")

_html=lxml.html.fromstring(r.text)


# In[19]:

len(lxml.html.tostring(_html))


# In[20]:

from lxml.cssselect import CSSSelector

sel=CSSSelector('table[summary] > tbody > ._tracklist_move > .name > a.title')
nodes=sel(_html)


# In[22]:

len(nodes)


# In[24]:

for node in nodes:
    print node.text_content()


# ### 곡명, 아티스트, 앨범 모두 가져오기

# In[27]:

from lxml.cssselect import CSSSelector

sel=CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes=sel(_html)
print lxml.html.tostring(nodes[0])


# In[29]:

_selName=CSSSelector('.name > a.title')
_selArtist=CSSSelector('._artist.artist')
_selAlbum=CSSSelector('.album > a')


# In[31]:

_name=_selName(nodes[1])
_artist=_selArtist(nodes[1])
_album=_selAlbum(nodes[1])


# In[35]:

print _name[0].text_content()
print _artist[0].text_content().strip()
print _album[0].text_content()


# In[37]:

for node in nodes:
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()

