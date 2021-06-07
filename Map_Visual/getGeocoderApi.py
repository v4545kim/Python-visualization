import  folium
import pandas as pd
import requests
url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

api_key = '1bd1923d9a6232e5829a4976b85dbe3a'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGeocoder(address) :
    result = ''
    url = url_header + address

    r = requests.get(url, headers=header)

    if r.status_code == 200 :
        try :
            result_address = r.json()["documents"][0]["address"]
            result = result_address['y'], result_address['x']
        except Exception as err :
            return  None
    else :
        result = 'Error[' + str(r.status_code) + ']'
    return result
#end def getGeocoder(address):

def makeMap(city, station, geoInfo) :
    shopinfo = station + '(' + city_dict[city] + ')'
    mycolor = city_color[city]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

    # 마커 그리기
    folium.Marker([latitude, longitude], popup=shopinfo,
                  icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)
# end makeMap(city, station, geoInfo)

city_dict = {'강릉':'강릉', '광주':'광주', '대구':'대구', '대전':'대전', '백령도':'백령도', '부산':'부산',
              '서울':'서울', '울릉도':'울릉도', '전주':'전주', '제주':'제주', '청주':'청주', '춘천':'춘천'}
city_color = {'강릉':'red', '광주':'red', '대구':'red', '대전':'red', '백령도':'red', '부산':'red',
               '서울':'red', '울릉도':'red', '전주':'red', '제주':'red', '청주':'red', '춘천':'red'}

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

csv_file = 'WeatherStation.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
print(myframe.info())

where = '대한민국'

city = '강릉'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData01 = myframe.loc[condition1 & condition2]

city = '광주'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData02 = myframe.loc[condition1 & condition2]

city = '대구'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData03 = myframe.loc[condition1 & condition2]

city = '대전'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData04 = myframe.loc[condition1 & condition2]

city = '백령도'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData05 = myframe.loc[condition1 & condition2]

city = '부산'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData06 = myframe.loc[condition1 & condition2]

city = '서울'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData07 = myframe.loc[condition1 & condition2]

city = '울릉도'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData08 = myframe.loc[condition1 & condition2]

city = '전주'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData09 = myframe.loc[condition1 & condition2]

city = '제주'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData10 = myframe.loc[condition1 & condition2]

city = '청주'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData11 = myframe.loc[condition1 & condition2]

city = '춘천'
condition1 = myframe['country'] == where
condition2 = myframe['city'] == city
mapData12 = myframe.loc[condition1 & condition2]

mylist = []
mylist.append(mapData01)
mylist.append(mapData02)
mylist.append(mapData03)
mylist.append(mapData04)
mylist.append(mapData05)
mylist.append(mapData06)
mylist.append(mapData07)
mylist.append(mapData08)
mylist.append(mapData09)
mylist.append(mapData10)
mylist.append(mapData11)
mylist.append(mapData12)

mapData = pd.concat(mylist, axis=0)
# print(mapData)

ok, notok = 0, 0
for idx in range(len(mapData.index)) :
    city = mapData.iloc[idx]['city']
    station = mapData.iloc[idx]['station']
    geoInfo = getGeocoder(station)

    if geoInfo == None :
        print('낫오케이 : ' + station)
        notok += 1
    else :
        print('오케이 : ' + station)
        ok += 1
        makeMap(city, station, geoInfo)
    print('-'*30)

total = ok + notok
print('ok : ', ok)
print('notok : ', notok)
print('total : ', total)

filename = '/Users/gimsunseob/Java Test/pythonProject/기상관측소.html'
mapObject.save(filename)
print('파일 저장 완료')

