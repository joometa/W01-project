import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.movie

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://movie.naver.com/movie/running/current.nhn',
                    headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

lis = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul> li')
# print(trs)
for li in lis:
    href = base_url = 'https://movie.naver.com' + li.select_one('dt > a')['href'] + '"target="_blank"'
    # print(href)
    name = li.select_one('dt > a').text
    # print(name)
    img = li.select_one('div > a > img')['src']
    # print(img)
    num = li.select_one('span.num').text
    # print(num)
    # star = li.select_one('dl.info_exp > dd > div', attrs={'num', 'txt'}).text.strip()
    # print(star)
    director = li.select_one('dl > dd:nth-child(3) > dl > dd:nth-child(4) >  span > a').text
    # print(director)
    genre = li.select_one('span > a').text
    # print(genre)
    print(href, name, img, num, director, genre)
    doc = {
        'name': name,
        'num': num,
        'href': href,
        'img': img,
        'director': director,
        'genre': genre,
        'like' : 0
    }
    db.movies.insert_one(doc)






# content > div.article > div:nth-child(1) > div.lst_wrap > ul

# lis = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
# for li in lis:
#     image = li.select_one('div > a > img')['src']
#     title = li.select_one('dl > dt > a').text
#     star = li.select_one('dl > dd.star > dl.info_star > dd > div > a > span.num').text
#
#     print(image,title,star)
