import ssl, datetime
import time
import urllib.request
from pandas import DataFrame

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

class Weather():
    def getWebDriver(self, cmdJavaScript):
        # cmdJavaScript : 문자열로 구성된 자바 스크립트 커맨드
        print(cmdJavaScript)
        self.driver.excute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

    def save2Csv(self, result):
        mycolumn = ['year', 'mytoday', 'city', 'nowTemp', 'sensTemp', 'humidity', 'precipitation', 'weatherInfo']
        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.year + 'weather.csv', encoding='utf-8', index=True)
        print(self.year + ' 날씨 파일이 생성됨')

    def getSoup(self):
        if self.soup == None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')

    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)

            return response
        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url %s' % (now, self.url)
            print(msg)
            return None

    def __init__(self, year, url):
        self.year = year
        self.url = url

        self.soup = self.get_request_url()

    def replacePrecipitation(self, year):
        weather = [year]

        newframe = DataFrame()

        for yearWeather in weather:
            filename = yearWeather + 'weather.csv'
            myframe = pd.read_csv(filename, index_col=0, encoding='utf-8')

            myframe = myframe.replace(' ', '0.0')  # 강수량에 있는   값을 0으로 치환

            newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)

        totalfile = year + 'weather.csv'
        newframe.to_csv(totalfile, encoding='utf-8')
        print(myframe.head())
        print(totalfile + '파일이 치환됨')
