import numpy as np
import pandas as pd
from datetime import datetime

class SubwayMethod:
    def __init__(self):
        pass
    def get_left_time(self, arrival_time):
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        for i in arrival_time:
            try:
                subwaytime = arrival_time[i].values[0]
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
            except:
                continue
            if now < subwaytime:
                left_time = subwaytime.minute - now.minute
                break
        return left_time
    def return_left_time(self, subwayname):
        df = [pd.read_csv('대구도시철도공사_1호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_2호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_3호선 열차시각표_20220430.csv')]
        subway_df = ''
        for subway in df:
            if subwayname in subway.values:
                subway_df = subway
                break
        left_direction_arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == '평일(상)')]
        right_direction_arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == '평일(하)')]
        left_direction_left_time = self.get_left_time(left_direction_arrival_time)
        right_direction_left_time = self.get_left_time(right_direction_arrival_time)
        print(left_direction_left_time, right_direction_left_time)
        

if __name__ == '__main__':
    subwaymethod = SubwayMethod()
    subwaymethod.return_left_time('범어')