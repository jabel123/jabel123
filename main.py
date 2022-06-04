import feedparser, datetime

velog_blog_rss_uri="http://honeyinfo7.tistory.com/rss"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """
**Backend Engineer 주현태**

:octocat: **경력사항**

1. [11번가](https://11st.co.kr/) (2022.04 ~ 현재)  
2. [위메프](http://www.wemakeprice.com) (2020.02 ~ 2022.03)  
3. [유한화학](http://www.yuhanchem.co.kr) (2017.03 ~ 2019.08)  
4. [데이타솔루션](http://www.datasolution.kr/) (2014.12 ~ 2016.10)    

:octocat: **개인프로젝트**

1. [중고책팔기](https://play.google.com/store/apps/details?id=com.copocalypse.bookseller)
2. [웃긴유머모음](https://play.google.com/store/apps/details?id=com.copocalypse.humorcrCrawlingWeb)
3. [공부타이머](https://play.google.com/store/apps/details?id=com.tistory.mythinkwrite.studytimer)
4. [금연도우미](https://play.google.com/store/apps/details?id=com.tistory.honeyinfo7.stopsmoking)

:octocat: **블로그**
1. [tistory 블로그](https://honeyinfo7.tistory.com/)
2. [네이버 블로그](https://blog.naver.com/jabel123)

:octocat: **관심있는 기술**
- Spring
- Oracle
- Git
- Docker
- Kafka
- Elasticsearch

안녕하세요 주현태입니다.   
2022년의 목표는 다음과 같습니다.
1. [tistory 블로그](https://honeyinfo7.tistory.com/)의 1일방문자가 1000명이 넘는것
2. 관심있는 기술에 대해 더욱 성숙해지기
3. 매일 한번은 스스로 생각을 조금이라도 하는 코드를 작성하기. (새로운 기술을 써보거나, 알고리즘 쉬운문제라도 매일 풀어보기)
4. 매주 블로그글 1회 작성하기

![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=jabel123&show_icons=true&theme=radical)
[![Tech Blog Badge](http://img.shields.io/badge/-Tech%20blog-black?style=flat-square&logo=github&link=https://honeyinfo7.tistory.com/)](https://honeyinfo7.tistory.com/)  


### ✍ Recent blog posts 
""" # list of blog posts will be appended here

j=0
MAX_POST=10
for i in feed['entries']:
    j+= 1
    if j > MAX_POST:
        break
    else:
        # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
        # dt = i['published']
        # markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
        # markdown_text += f"[{i['title']}]({i['link']}) <br>\n"
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()  
