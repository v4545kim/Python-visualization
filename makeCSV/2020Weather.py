from weatherUtil import Weather
##########################################################
year = '2020년'
base_url = 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
##########################################################
def getData():
    savedData = []  # 엑셀로 저장될 리스트

    for day in range(1, 32):
        url = base_url
        url += '?auto_man=m&stn=0&type=t99&reg=100'
        url += '&tm=2020.5.%s' % str(day)
        url += '.12%3A00&x=0&y=0'

        weatherAvg = Weather(year, url)
        soup = weatherAvg.getSoup()

        mytoday = day
        mytbody = soup.find('tbody')

        for mytrs in mytbody.findAll('tr'):

            mytr = mytrs.select_one('td:nth-of-type(1)').string

            if mytr == '강릉' or mytr == '광주' or mytr == '대구' or mytr == '대전' \
                    or mytr == '백령도' or mytr == '부산' or mytr == '서울' or mytr == '울릉도' \
                    or mytr == '전주' or mytr == '제주' or mytr == '청주' or mytr == '춘천':

                city = mytrs.select_one('td:nth-of-type(1)').string  # 도시명
                nowTemp = mytrs.select_one('td:nth-of-type(6)').string  # 현재 기온
                sensTemp = mytrs.select_one('td:nth-of-type(8)').string  # 체감 온도
                humidity = mytrs.select_one('td:nth-of-type(10)').string  # 습도
                precipitation = mytrs.select_one('td:nth-of-type(9)').string  # 강수량
                weatherInfo = mytrs.select_one('td:nth-of-type(2)').string  # 기상정보
                savedData.append([year, mytoday, city, nowTemp, sensTemp, humidity, precipitation, weatherInfo])

    weatherAvg.save2Csv(savedData)
    weatherAvg.replacePrecipitation(year)

print(year + ' 날씨 크롤링 시작')
getData()
print(year + ' 날씨 크롤링 끝')