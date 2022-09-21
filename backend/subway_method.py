import numpy as np
import pandas as pd
from datetime import datetime

df1 = pd.read_csv('대구도시철도공사_1호선 열차시각표_20220430.csv')
# time = datetime.datetime.strptime("8:04:40", '%H:%M:%S') # 시간을 datetime 형식으로 변환
timeschedule = df1.loc[(df1['역명'] == '안심') & (df1['요일별'] == '평일(상)')]
now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
for i in timeschedule:
    try:
        subwaytime = timeschedule[i].values[0]
        subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
    except:
        continue
    if now < subwaytime:
        print(subwaytime.minute - now.minute)
        break