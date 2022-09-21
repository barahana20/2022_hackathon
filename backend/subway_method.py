import numpy as np
import pandas as pd
from datetime import datetime

class SubwayMethod:
    def __init__(self):
        pass
    def return_left_time(self, subwayname):
        df = [pd.read_csv('대구도시철도공사_1호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_2호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_3호선 열차시각표_20220430.csv')]
        subway_df = ''
        for subway in df:
            if subwayname in subway.values:
                subway_df = subway
                break
        timeschedule = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == '평일(상)')]
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

if __name__ == '__main__':
    subwaymethod = SubwayMethod()
    subwaymethod.return_left_time('범어')