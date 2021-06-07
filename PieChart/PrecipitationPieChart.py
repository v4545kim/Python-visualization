import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
###############################################################################
plt.rc('font', family='AppleGothic')
matplotlib.rcParams['axes.unicode_minus'] = False
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'PrecipitationpieChart'
filename1 = './../makeCSV/2019년weather.csv'
filename2 = './../makeCSV/2020년Weather.csv'
filename3 = './../makeCSV/2021년weather.csv'
###############################################################################
def MakePieChart(filename,titlename):
    data = pd.read_csv(filename, index_col='city')
    print(data.columns)
    print('-'*30)

    my_concern = [item for item in data.index if item in ['강릉', '광주', '대구', '대전', '백령도', '부산',
                                                          '서울', '울릉도', '전주', '제주', '청주', '춘천']]
    print(my_concern)

    data = data.loc[my_concern]

    raindata = data['precipitation']

    print(raindata)
    print('-'*30)

    print(type(raindata))
    print('-'*30)

    totalPrecipitation = raindata.groupby(level=0).sum()

    mylabel = totalPrecipitation.index

    print(mylabel)
    print('-'*30)

    mycolors = ['blue', 'darkorange', 'yellow', 'slategrey', 'lime', 'violet',
                'linen', 'rosybrown', 'pink', 'peru', 'red', 'cyan']

    plt.figure()

    plt.pie(totalPrecipitation, labels=mylabel, shadow=False,
            colors=mycolors, autopct='%1.1f%%', startangle=90, counterclock=False)

    plt.grid(True)
    plt.legend(bbox_to_anchor=(1, 1), fontsize='small')
    plt.xlabel('도시')
    # plt.ylabel("발생 건수")
    plt.title(titlename)

    global cnt
    cnt += 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')
MakePieChart(filename1, '2019년 5월 강수량 비율')
MakePieChart(filename2, '2020년 5월 강수량 비율')
MakePieChart(filename3, '2021년 5월 강수량 비율')
###############################################################################
print('finished')
