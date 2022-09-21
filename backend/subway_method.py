# -*- coding: utf-8 -*- 
import numpy as np
import pandas as pd
from datetime import datetime

class SubwayMethod:
    def __init__(self):
        self.df = [pd.read_csv('대구도시철도공사_1호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_2호선 열차시각표_20220430.csv'), pd.read_csv('대구도시철도공사_3호선 열차시각표_20220430.csv')]
        self.line = [['안심', '각산', '반야월', '신기', '율하', '용계', '방촌', '해안', '동촌', '아양교', '동구청', '동대구', '신천', '칠성시장', '대구역', '중앙로', '반월당', '명덕', '교대', '영대병원', '현충로', '안지랑', '대명', '서부정류장', '송현', '월촌', '상인', '월배', '진천', '대곡', '화원', '설화명곡'], ['영남대', '임당', '정평', '사월', '신매', '고산', '대공원', '연호', '담티', '만촌', '수성구청', '범어', '대구은행', '경대병원', '반월당', '청라언덕', '반고개', '내당', '두류', '감삼', '죽전', '용산', '이곡', '성서산단', '계명대', '강창', '대실', '다사', '문양'], ['용지', '범물', '지산', '수성못', '황금', '어린이회관', '수성구민운동장', '수성시장', '대봉교', '건들바위', '명덕', '남산', '청라언덕', '서문시장', '달성공원', '북구청', '원대', '팔달시장', '만평', '공단', '팔달', '매천시장', '매천', '태전', '구암', '칠곡운암', '동천', '팔거', '학정', '칠곡경대병원']]
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
        subway_df = ''
        for subway in self.df:
            if subwayname in subway.values:
                subway_df = subway
                break
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = self.return_week_day()
       
        arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
        if arrival_time.empty:
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '출발')]
            if arrival_time.empty:
                arrival_time = None
            
        departure_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
        if departure_time.empty:
            departure_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '출발')]
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
                    up_left_time = (upsubwaytime - now).seconds//60
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
                    down_left_time = (downsubwaytime - now).seconds//60
                    break
            downsubwaytime = downsubwaytime.strftime("%H:%M:%S")

        return (upsubwaytime, up_left_time, downsubwaytime, down_left_time)
    def return_first_last_train_time(self, subwayname, subwaydir):
        subway_df = ''
        first_train_time = None
        last_train_time = None
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        weekday = self.return_week_day()
        line = self.line[subway_index]
        if line.index(subwayname) < line.index(subwaydir):
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
        else:
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
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
    def three(self, subwayname):
        subway_df = ''
        left_first_train_time = None
        left_last_train_time = None
        for subway in self.df:
            if subwayname in subway.values:
                subway_df = subway
                break
        weekday = self.return_week_day()
        left_arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
        right_arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
        if not left_arrival_time.empty:
            for i in left_arrival_time:
                if type(left_arrival_time[i].values[0]) == str and ':' in left_arrival_time[i].values[0]:
                    subwaytime = str(left_arrival_time[i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                left_first_train_time = subwaytime.strftime("%H:%M:%S")
                break
            for i in left_arrival_time.loc[:, ::-1]:
                if type(left_arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in left_arrival_time.loc[:, ::-1][i].values[0]:
                    subwaytime = str(left_arrival_time.loc[:, ::-1][i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                left_last_train_time = subwaytime.strftime("%H:%M:%S")
                break
        if not right_arrival_time.empty:
            for i in right_arrival_time:
                if type(right_arrival_time[i].values[0]) == str and ':' in right_arrival_time[i].values[0]:
                    subwaytime = str(right_arrival_time[i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                right_first_train_time = subwaytime.strftime("%H:%M:%S")
                break
            for i in right_arrival_time.loc[:, ::-1]:
                if type(right_arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in right_arrival_time.loc[:, ::-1][i].values[0]:
                    subwaytime = str(right_arrival_time.loc[:, ::-1][i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                right_last_train_time = subwaytime.strftime("%H:%M:%S")
                break
        return (left_first_train_time, left_last_train_time, right_first_train_time, right_last_train_time)
    def two(self, subwayname, subwaydir):
        subwaytime1 = None
        left_time1 = None
        subway_df = ''
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = self.return_week_day()
        line = self.line[subway_index]
        if line.index(subwayname) < line.index(subwaydir):
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
        else:
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
        if not arrival_time.empty:
            for i in arrival_time:
                if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                    subwaytime1 = str(arrival_time[i].values[0])
                else:
                    continue
                subwaytime1 = datetime.strptime(subwaytime1, "%H:%M:%S")
                
                if now < subwaytime1:
                    left_time1 = (subwaytime1 - now).seconds//60
                    try:
                        if type(arrival_time[str(int(i)+1)].values[0]) == str and ':' in arrival_time[str(int(i)+1)].values[0]:
                            subwaytime2 = str(arrival_time[str(int(i)+1)].values[0])
                        else:
                            continue
                    except:
                        break
                    subwaytime2 = datetime.strptime(subwaytime2, "%H:%M:%S")
                    left_time2 = (subwaytime2 - now).seconds//60
                    return (subwaytime1.strftime("%H:%M:%S"), left_time1, subwaytime2.strftime("%H:%M:%S"), left_time2)
            subwaytime1 = subwaytime1.strftime("%H:%M:%S")
        return (subwaytime1, left_time1, None, None)
        
        
    
if __name__ == '__main__':
    subwaymethod = SubwayMethod()
    print(subwaymethod.one('영남대'))