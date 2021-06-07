import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'
weatherList = ['2019년weather', '2020년weather', '2021년weather',]

newframe = DataFrame()

for onestore in weatherList:
    filename = onestore + '.csv'
    myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)

    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)

print(newframe.info())

totalfile = 'allweather.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + '파일이 저장됨')
