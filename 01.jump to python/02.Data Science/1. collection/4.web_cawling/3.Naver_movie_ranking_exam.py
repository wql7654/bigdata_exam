import urllib.request
from bs4 import BeautifulSoup

html=urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup=BeautifulSoup(html,'html.parser')

name_list=[]
up_down_list=[]
up_down_num=[]
all_list=[]
up_downs=''


tags = soup.findAll('div', attrs={'class':'tit3'})
for tag in tags:
    if tag.a.string.find(',')!=-1:
        tag.a.string='"'+tag.a.string+'"'
    name_list.append(tag.a.string)

up_down_info = soup.findAll('img', attrs={'class':'arrow'})
for up_down in up_down_info:
    if up_down.attrs['alt'] == 'na':
        up_downs=''
    elif up_down.attrs['alt'] == 'up':
        up_downs="+"
    elif up_down.attrs['alt'] == 'down':
        up_downs='-'
    up_down_list.append(up_downs)

up_down_rank = soup.findAll('td', attrs={'class':'range ac'})
for up_down in up_down_rank:
    up_down_num.append(up_down.string)


for list_movie in range(0,len(name_list)):
    sel_list = []
    sel_list.append(str(list_movie+1))
    sel_list.append(name_list[list_movie])
    sel_list.append(up_down_list[list_movie]+up_down_num[list_movie])
    all_list.append(sel_list)


re=[]
res=['순위,영화명,변동폭\n']
for i in all_list:
    re=','.join(i)
    re=re+'\n'
    res.append(re)


print(res)


with open("movie_ranking.csv", 'w') as f:
    f.writelines(res)

