import pandas as pd
import matplotlib.pyplot as plt
##########################################################
plt.rc('font', family='AppleGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'WeatherScatterPlot'
filename = './../makeCSV/2021년weather.csv'
##########################################################
print('스타일 목록')
print(plt.style.available)
print('-'*30)

plt.style.use('bmh')

mpg = pd.read_csv(filename, encoding='utf-8')
print(mpg.columns)
print('-'*30)

xdata = mpg.loc[:, ['humidity']]  # 습도
ydata = mpg.loc[:, ['precipitation']]  # 강수량

labels = mpg['city'].unique()
print(labels)

mycolor = ['blue', 'darkorange', 'yellow', 'slategrey', 'green', 'violet',
            'indigo', 'rosybrown', 'pink', 'peru', 'red', 'black']

plt.figure()
idx = 0
labels_dict = {'강릉':'강릉', '광주':'광주', '대구':'대구', '대전':'대전', '백령도':'백령도', '부산':'부산',
               '서울':'서울', '울릉도':'울릉도', '전주':'전주', '제주':'제주', '청주':'청주', '춘천':'춘천'}

for finditem in labels:
    xdata = mpg.loc[mpg['city'] == finditem, 'humidity']
    ydata = mpg.loc[mpg['city'] == finditem, 'precipitation']
    plt.plot(xdata, ydata, linestyle='None', marker='.', label=labels_dict[finditem], color=mycolor[idx])
    idx += 1

plt.legend()
plt.xlabel('습도(%)')
plt.ylabel('강수량(mm)')
plt.title('산점도 그래프')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')
