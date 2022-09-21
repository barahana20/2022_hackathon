import numpy as np
import pandas as pd
from datetime import datetime

class SubwayMethod:
    def __init__(self):
        self.df = [pd.read_csv('대구도시철도공사_1호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_2호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_3호선 열차시각표_20220430.csv')]
        pass
    def return_week_day(self):
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = now.weekday()
        if weekday == 5:
            weekday = '토요일'
        elif weekday == 6:
            weekday = '휴일'
        else:
            weekday = '평일'
        return weekday
    def one(self, subwayname):
        downsubwaytime = None
        upsubwaytime = None
        down_left_time = None
        up_left_time = None
        self.subway_df = ''
        for subway in self.df:
            if subwayname in subway.values:
                self.subway_df = subway
                break
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = self.return_week_day()
        arrival_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}(상)') & (self.subway_df['구분'] == '도착')]
        if arrival_time.empty:
            arrival_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}(하)') & (self.subway_df['구분'] == '출발')]
            if arrival_time.empty:
                arrival_time = None
            
        departure_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}(하)') & (self.subway_df['구분'] == '도착')]
        if departure_time.empty:
            departure_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}(상)') & (self.subway_df['구분'] == '출발')]
            if departure_time.empty:
                departure_time = None
        if arrival_time is not None:
            for i in arrival_time:
                
                if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                    upsubwaytime = str(arrival_time[i].values[0])
                else:
                    continue
                upsubwaytime = datetime.strptime(upsubwaytime, "%H:%M:%S")
                if now < upsubwaytime:
                    up_left_time = (upsubwaytime - now).min
                    break
            upsubwaytime = upsubwaytime.strftime("%H:%M:%S")
        if departure_time is not None:
            for i in departure_time:
                
                if type(departure_time[i].values[0]) == str and ':' in departure_time[i].values[0]:
                    downsubwaytime = str(departure_time[i].values[0])
                else:
                    continue
                downsubwaytime = datetime.strptime(downsubwaytime, "%H:%M:%S")
                if now < downsubwaytime:
                    down_left_time = (downsubwaytime - now).min
                    break
            downsubwaytime = downsubwaytime.strftime("%H:%M:%S")

        return (upsubwaytime, up_left_time, downsubwaytime, down_left_time)
    def return_first_last_train_time(self, subwayname, subwaydir):
        self.subway_df = ''
        first_train_time = None
        last_train_time = None
        for subway in self.df:
            if subwayname in subway.values:
                self.subway_df = subway
                break
        weekday = self.return_week_day()
        arrival_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}({subwaydir})') & (self.subway_df['구분'] == '도착')]
        for i in arrival_time:
            if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                subwaytime = str(arrival_time[i].values[0])
            else:
                continue
            subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
            first_train_time = subwaytime.strftime("%H:%M:%S")
            break
        for i in arrival_time.loc[:, ::-1]:
            if type(arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in arrival_time.loc[:, ::-1][i].values[0]:
                subwaytime = str(arrival_time.loc[:, ::-1][i].values[0])
            else:
                continue
            subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
            last_train_time = subwaytime.strftime("%H:%M:%S")
            break
        return (first_train_time, last_train_time)
    def two(self, subwayname, subwaydir):
        subwaytime1 = None
        left_time1 = None
        self.subway_df = ''
        for subway in self.df:
            if subwayname in subway.values:
                self.subway_df = subway
                break
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = self.return_week_day()
        arrival_time = self.subway_df.loc[(self.subway_df['역명'] == subwayname) & (self.subway_df['요일별'] == f'{weekday}({subwaydir})') & (self.subway_df['구분'] == '도착')]
        if not arrival_time.empty:
            for i in arrival_time:
                if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                    subwaytime1 = str(arrival_time[i].values[0])
                else:
                    continue
                subwaytime1 = datetime.strptime(subwaytime1, "%H:%M:%S")
                
                if now < subwaytime1:
                    left_time1 = (subwaytime1 - now).min
                    try:
                        if type(arrival_time[str(int(i)+1)].values[0]) == str and ':' in arrival_time[str(int(i)+1)].values[0]:
                            subwaytime2 = str(arrival_time[str(int(i)+1)].values[0])
                        else:
                            continue
                    except:
                        break
                    subwaytime2 = datetime.strptime(subwaytime2, "%H:%M:%S")
                    left_time2 = (subwaytime2 - now).min
                    return (subwaytime1.strftime("%H:%M:%S"), left_time1, subwaytime2.strftime("%H:%M:%S"), left_time2)
            subwaytime1 = subwaytime1.strftime("%H:%M:%S")
        return (subwaytime1, left_time1, None, None)
        
        
    
if __name__ == '__main__':
    subwaymethod = SubwayMethod()
    print(subwaymethod.two('동대구', '상'))