import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##########################################################
plt.rc('font', family='AppleGothic')
plt.rcParams['figure.figsize'] = [10, 5]
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'TemperatureBrokenLineChart'
filename1 = './../makeCSV/2019년weather.csv'
filename2 = './../makeCSV/2020년Weather.csv'
filename3 = './../makeCSV/2021년weather.csv'
##########################################################
data1 = pd.read_csv(filename1, index_col='city')
data2 = pd.read_csv(filename2, index_col='city')
data3 = pd.read_csv(filename3, index_col='city')
##########################################################

def MakeBarChart01():

    tempdata = data1['nowTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='blue', linestyle='solid', marker='o', label='2019년 5월')

    tempdata = data2['nowTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='red', linestyle='solid', marker='o', label='2020년 5월')

    tempdata = data3['nowTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='green', linestyle='solid', marker='o', label='2021년 5월')
    plt.legend()

    YTICKS_INTERVAL = 5
    maxlim = (int(avgTempdata.max()/YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
    print(maxlim)

    values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
    print(values)

    plt.yticks(values, ['%s' % format(val, ',') for val in values])
    plt.grid(True)
    plt.xlabel('도시')
    plt.ylabel('기온')
    plt.title('전국 5월 낮 평균 기온')

    global  cnt
    cnt += 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + '파일 저장됨')
############################################################################################
def MakeBarChart02():
    plt.figure()

    tempdata = data1['sensTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='blue', linestyle='solid', marker='o', label='2019년 5월')

    tempdata = data2['sensTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='red', linestyle='solid', marker='o', label='2020년 5월')

    tempdata = data3['sensTemp']

    avgTempdata = tempdata.groupby(level=0).mean()

    plt.plot(avgTempdata, color='green', linestyle='solid', marker='o', label='2021년 5월')
    plt.legend()

    YTICKS_INTERVAL = 5
    maxlim = (int(avgTempdata.max()/YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
    print(maxlim)

    values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
    print(values)

    plt.yticks(values, ['%s' % format(val, ',') for val in values])
    plt.grid(True)
    plt.xlabel('도시')
    plt.ylabel('기온')
    plt.title('전국 5월 낮 평균 체감온도')

    global cnt
    cnt += 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + '파일 저장됨')
    print('finished')

MakeBarChart01()
MakeBarChart02()