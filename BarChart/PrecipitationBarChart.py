import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

###############################################################################
plt.rc('font', family='AppleGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'PrecipitationBarChart'
filename1 = './../makeCSV/2019년weather.csv'
filename2 = './../makeCSV/2020년Weather.csv'
filename3 = './../makeCSV/2021년weather.csv'
###############################################################################
data1 = pd.read_csv(filename1, index_col='city')
data2 = pd.read_csv(filename2, index_col='city')
data3 = pd.read_csv(filename3, index_col='city')

raindata1 = data1['precipitation']
avgPrecipitation1 = raindata1.groupby(level=0).sum()

raindata2 = data2['precipitation']
avgPrecipitation2 = raindata2.groupby(level=0).sum()

raindata3 = data3['precipitation']
avgPrecipitation3 = raindata3.groupby(level=0).sum()
###############################################################################
def MakeBarChart01(x, y, color, xlabel, ylabel, title):
    plt.figure()
    plt.bar(x, y, color=color, alpha=0.7)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.grid(True)

    YTICKS_INTERVAL = 10

    maxlim = (int(y.max() / YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
    print(maxlim)

    values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)

    plt.yticks(values, ['%s' % format(val, ',') for val in values])

    # 그래프 위에 건수와 비율 구하기
    ratio = 100 * y / y.sum()
    print(ratio)
    print('-' * 40)

    plt.rc('font', size=6)
    for idx in range(y.size):
        value = '%.2f mm' % (y[idx])  # 예시 : 60.99mm
        ratioval = '%.1f%%' % (ratio[idx])  # 예시 : 2.5%
        # 그래프의 위에 "누적 강수량" 표시
        plt.text(x=idx, y=y[idx] + 1, s=value, horizontalalignment='center')
        # 그래프의 중간에 비율 표시
        plt.text(x=idx, y=y[idx] / 2, s=ratioval, horizontalalignment='center')

    # 평균 값을 수평선으로 그리기
    meanval = y.mean()
    print(meanval)
    print('-' * 40)

    average = '평균 : %.2f mm' % meanval
    plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
    plt.text(x=y.size - 1, y=meanval + 1, s=average, horizontalalignment='center')

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')
    print(type(y))
# def MakeBarChart01
###############################################################################
'''
그래프에 대한 색상을 지정하는 리스트입니다.
예시에서 "w"는 흰색이라서 제외하도록 합니다.
'''
colors = ['blue', 'darkorange', 'yellow', 'slategrey', 'lime', 'violet',
            'linen', 'rosybrown', 'pink', 'peru', 'red', 'cyan']

mycolor = colors[0:len(avgPrecipitation1)]

'''
데이터 프레임을 이용하여 막대 그래프를 그려 주는 함수를 호출합니다.
'''
MakeBarChart01(x=avgPrecipitation1.index, y=avgPrecipitation1, color=mycolor, xlabel='도시', ylabel='누적 강수량 비율', title='2019년 5월 누적 강수량')
MakeBarChart01(x=avgPrecipitation2.index, y=avgPrecipitation2, color=mycolor, xlabel='도시', ylabel='누적 강수량 비율', title='2020년 5월 누적 강수량')
MakeBarChart01(x=avgPrecipitation3.index, y=avgPrecipitation3, color=mycolor, xlabel='도시', ylabel='누적 강수량 비율', title='2021년 5월 누적 강수량')
###############################################################################
'''
데이터 프레임을 사용하여 막대 그래프를 그려 주는 함수입니다.
'''

def MakeBarChart02(chartdata, rotation, title, ylim=None, stacked=False, yticks_interval = 10):
    plt.figure()
    # 범례에 제목을 넣으려면 plot() 메소드의 legend 옵션을 사용해야 합니다.
    chartdata.plot(kind='bar', rot=rotation, title=title, legend=True, stacked=stacked)

    plt.legend(bbox_to_anchor=(1.1, 1), fontsize='small')

    print('chartdata')
    print(chartdata)

    if stacked == False :
        # max(chartdata.max())은 항목들 값 중에서 최대 값을 의미합니다.
        maxlim = (int(max(chartdata.max()) / yticks_interval) + 1) * yticks_interval
        print('maxlim : ', maxlim)
        values = np.arange(0, maxlim + 1, yticks_interval)
        plt.yticks(values, ['%s' % format(val, ',') for val in values])
    else : # 누적 막대 그래프
        # 국가별 누적 합인 chartdata.sum(axis=1))의 최대 값에 대한 연산이 이루어 져야 합니다.
        maxlim = (int(max(chartdata.sum(axis=1)) / yticks_interval) + 1) * yticks_interval
        print('maxlim : ', maxlim)
        values = np.arange(0, maxlim + 1, yticks_interval)
        plt.yticks(values, ['%s' % format(val, ',') for val in values])

    # y축의 상하한 값이 주어 지는 경우에만 설정합니다.
    if ylim != None :
        plt.ylim(ylim)

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')
# def MakeBarChart02
###############################################################################
'''
이번 예시에서는 특정 국가별 특정 일자에 대한 다변량 막대 그래프를 그려 보고자 합니다.
'''
filename = 'DailyPrecipitation.csv'
data = pd.read_csv(filename, index_col='city')
print(data.columns)
print('-' * 30)

COUNTRY = ['19년서울', '19년부산', '20년서울', '20년부산', '21년서울', '21년부산']
WHEN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
data = data.loc[COUNTRY, WHEN]

print(data)
print('-'*30)

data.index.name = '도시명'
data.columns.name = '강수량'

MakeBarChart02(chartdata=data, rotation=0, title='(19,20,21)년도 5월 일별 강수량' )
###############################################################################
dataT = data.T
ymax = dataT.sum(axis=1)
ymaxlimit = ymax.max() + 40

MakeBarChart02(chartdata=data, rotation=0, title='(19,20,21)년도 5월 일별 걍수량(누적)', ylim=[0, ymaxlimit], stacked=True, yticks_interval=10)
###############################################################################
data = pd.read_csv(filename, index_col='city')

six = [item for item in data.index if item in ['19년서울', '19년부산', '20년서울', '20년부산', '21년서울', '21년부산']]
print(six)

data = data.loc[six]

print(data)
print('-' * 30)

column_names = data.columns.tolist()
print('column_names')
print(column_names)

# 도시별 numpy 배열을 저장하고 있는 사전
chartdata = {}

for row in data.index:
    # print(data.loc[row])
    # print(type(row))
    chartdata[row] = data.loc[row].values

# print('chartdata')
# print(chartdata)

def MakeBarChart03(chartdata, column_names):
    labels = list(chartdata.keys())
    data = np.array(list(chartdata.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max()+5)

    for i, (colname, color) in enumerate(zip(column_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)

        r, g, b, _ = color
    ax.legend(bbox_to_anchor=(1.1, 1), fontsize='small')

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')

    return fig, ax
# end def MakeBarChart03
MakeBarChart03(chartdata, column_names)
###############################################################################
