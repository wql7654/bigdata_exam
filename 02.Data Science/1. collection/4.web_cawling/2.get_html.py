import requests
from bs4 import BeautifulSoup


response =requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup=BeautifulSoup(response.content,'html.parser')

table=soup.find('table', {'class':'table_develop3'})
data=[]

def data_correction(org_text):
    if org_text == '\xa0':
        return 'N/A'
    return org_text

for tr in table.find_all('tr'):
    tds=list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point =data_correction(td.find('a').text)
            cloud = data_correction(tds[1].text)
            visibility = data_correction(tds[2].text)
            temperature=data_correction(tds[5].text)
            wd_temp=data_correction(tds[7].text)

            humidity=data_correction(tds[10].text)
            wdirection_wind=data_correction(tds[11].text)
            wind_speed=data_correction(tds[12].text)
            wind_speed=wind_speed.split("'")[1]

            data.append([point, cloud,visibility,temperature,wd_temp,humidity,wdirection_wind,wind_speed])

print(data)
