import requests
from bs4 import BeautifulSoup
import csv
from parse import *


base_url = "https://movie.naver.com/movie/running/current.nhn"
# start_num = i
# end_url = "&refresh_start=0"
URL = base_url  #+ str(start_num) + end_url

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(len(soup))

movie_list =[] 

news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > .article > .obj_section > .lst_wrap > ul > li')
for i in news_section:    
    title = i.select_one('dl > dt > a').text    
    code = parse("/movie/bi/mi/basic.nhn?code={}", i.select_one('dl > dt > a')["href"])
    movie_list.append([title, code.fixed])
# print(len(news_section))
print(movie_list)