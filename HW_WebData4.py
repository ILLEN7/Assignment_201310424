{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 웹데이터-4: 한국 포털사이트에서 노래 제목을 검색"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## regex 활용해서 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib\n",
    "keyword='벚꽃'\n",
    "f=urllib.urlopen(\"http://music.naver.com/search/search.nhn?query=%EB%B2%9A%EA%BD%83&target=track\")\n",
    "mydata=f.read();\n",
    "pos=mydata.find(\"트랙 리스트\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 벚꽃\n",
      "222676\n"
     ]
    }
   ],
   "source": [
    "if (pos>0): # 이 부분 무슨 말인지 모르겠다...!!!\n",
    "    pos = mydata.find(\"_title title NPI=\", pos);\n",
    "    pos = mydata.find(\"title=\", pos+20)\n",
    "    pos2 = mydata.find(\"\\\"\", pos+8)\n",
    "    print \"---\", mydata[pos+7:pos2]\n",
    "    \n",
    "#pos 가 글자수. 그러니까, 문자는 0,1,2  문자가 없으면 - 값이 나온다. pos>0은 결국, 문자가 있으면 이라는 뜻. \n",
    "    \n",
    "print len(mydata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re\n",
    "p=re.compile('title=\".*벚꽃.*\"')\n",
    "res=p.findall(mydata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "title=\"검색어 입력\" value=\"벚꽃\" maxlength=\"50\" accesskey=\"s\"\n",
      "title=\"그녀가 보내준 벚꽃편지\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:1,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:2,i:170969\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃놀이\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:3,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"サクラ色 (Sakura Iro) (벚꽃 색) - Sony 사이버 샷 CM송\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"Sakura (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (MR 트랙)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Feat. 제인제이, 진정민)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (꽃이 지다...)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (꽃이 지다...)\" class=\"_album NPI=a:album,r:9,i:585308\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"Sakura (벚꽃) (DenpO115 동일본 에이어 CM 송)\" ><span class=\"ellipsis\"\n",
      "title=\"1집 Sakurasakumachi Monogatari (벚꽃 피는 거리이야기)\" class=\"_album NPI=a:album,r:12,i:321260\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:13,i:170969\"><span class=\"ellipsis\"\n",
      "title=\"Cherry Blossom (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:17,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Acoustic Ver.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:23,i:625868\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Feat. 강윤희)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃축제\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:27,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:29,i:500208\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Cherry Blossom)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:36,i:374857\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (외발로 살다 OST)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"サクラ (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 하나 (Cherry Blossom) (Feat. MiMi)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Cherry Blossom)\" class=\"_album NPI=a:album,r:45,i:623930\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Acoustic Ver.)\" ><span class=\"ellipsis\"\n",
      "title=\"다시 부르기 곰돌이 첫번째 이야기 - 벚꽃 (Acoustic Ver.)\" class=\"_album NPI=a:album,r:50,i:317230\"><span class=\"ellipsis\"\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## CSSSelector 활용해서 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#노래 제목이 있는 위치\n",
    "# body > wrap > div.fix_conts > container > .container_inner > content\\\n",
    "# > div:nth-child(4) > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack\\\n",
    "# > table tbody > tr:nth-child(2) > td.name > a.title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "html=lxml.html.fromstring(mydata)\n",
    "sel=CSSSelector('#content > div:nth-child(4) \\\n",
    "> div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \\\n",
    "> table > tbody > tr:nth-child(2) > td.name > a.title')\n",
    "results=sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(results) #여기서 오류남. 1이 떠야하는데 0이 뜸.. 위에서 다시 해결하기"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
