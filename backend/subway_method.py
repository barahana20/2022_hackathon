# -*- coding: utf-8 -*- 
import numpy as np
import pandas as pd
from datetime import datetime
# LeftDirectionArrivalTime: 왼쪽 방향 열차도착시간
# LeftDirectionLeftTime: 왼쪽방향 열차도착까지 남은 시간
# RightDirectionArrivalTime: 오른쪽 방향 열차도착시간
# RightDirectionLeftTime: 오른쪽 방향 열차도착까지 남은 시간
# RightFirstTime: 오른쪽 방향 열차 첫 차 시간
# LeftFirstTime: 왼쪽 방향 열차 첫 차 시간
# RightLastTime: 오른쪽 방향 열차 마지막 차 시간
# LeftLastTime: 왼쪽 방향 열차 마지막 차 시간
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
        leftDirectionArrivalTime = None
        leftDirectionLeftTime = None
        rightDirectionArrivalTime = None
        rightDirectionLeftTime = None
        subway_df = ''
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        
        subwayLine = subway_index+1
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
                    leftDirectionLeftTime = str(arrival_time[i].values[0])
                else:
                    continue
                leftDirectionLeftTime = datetime.strptime(leftDirectionLeftTime, "%H:%M:%S")
                if now < leftDirectionLeftTime:
                    rightDirectionLeftTime = (leftDirectionLeftTime - now).seconds//60
                    break
            leftDirectionLeftTime = leftDirectionLeftTime.strftime("%H:%M:%S")
        if departure_time is not None:
            for i in departure_time:
                
                if type(departure_time[i].values[0]) == str and ':' in departure_time[i].values[0]:
                    leftDirectionArrivalTime = str(departure_time[i].values[0])
                else:
                    continue
                leftDirectionArrivalTime = datetime.strptime(leftDirectionArrivalTime, "%H:%M:%S")
                if now < leftDirectionArrivalTime:
                    rightDirectionArrivalTime = (leftDirectionArrivalTime - now).seconds//60
                    break
            leftDirectionArrivalTime = leftDirectionArrivalTime.strftime("%H:%M:%S")

        return (leftDirectionLeftTime, rightDirectionLeftTime, leftDirectionArrivalTime, rightDirectionArrivalTime, subwayLine)
    
    def two(self, subwayname, subwaydir):
        firstArrivalTime = None
        firstLeftTime = None
        subway_df = ''
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        subwayLine = subway_index+1
        now = datetime.strptime(datetime.now().strftime('%H:%M:%S'), "%H:%M:%S")
        weekday = self.return_week_day()
        subway_line = self.line[subway_index]
        if subway_line.index(subwayname) < subway_line.index(subwaydir):
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
        else:
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
        if not arrival_time.empty:
            for i in arrival_time:
                if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                    firstArrivalTime = str(arrival_time[i].values[0])
                else:
                    continue
                firstArrivalTime = datetime.strptime(firstArrivalTime, "%H:%M:%S")
                
                if now < firstArrivalTime:
                    firstLeftTime = (firstArrivalTime - now).seconds//60
                    try:
                        if type(arrival_time[str(int(i)+2)].values[0]) == str and ':' in arrival_time[str(int(i)+2)].values[0]:
                            secondArrivalTime = str(arrival_time[str(int(i)+2)].values[0])
                        else:
                            continue
                    except:
                        break
                    secondArrivalTime = datetime.strptime(secondArrivalTime, "%H:%M:%S")
                    secondLeftTime = (secondArrivalTime - now).seconds//60
                    return (firstArrivalTime.strftime("%H:%M:%S"), firstLeftTime, secondArrivalTime.strftime("%H:%M:%S"), secondLeftTime, subwayLine)
            firstArrivalTime = firstArrivalTime.strftime("%H:%M:%S")
        return (firstArrivalTime, firstLeftTime, None, None, subwayLine)
    def three(self, subwayname):
        subway_df = ''
        leftFirstTime = None
        leftLastTime = None
        rightFirstTime = None
        rightLastTime = None
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        subwayLine = subway_index+1
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
                leftFirstTime = subwaytime.strftime("%H:%M:%S")
                break
            for i in left_arrival_time.loc[:, ::-1]:
                if type(left_arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in left_arrival_time.loc[:, ::-1][i].values[0]:
                    subwaytime = str(left_arrival_time.loc[:, ::-1][i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                leftLastTime = subwaytime.strftime("%H:%M:%S")
                break
        if not right_arrival_time.empty:
            for i in right_arrival_time:
                if type(right_arrival_time[i].values[0]) == str and ':' in right_arrival_time[i].values[0]:
                    subwaytime = str(right_arrival_time[i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                rightFirstTime = subwaytime.strftime("%H:%M:%S")
                break
            for i in right_arrival_time.loc[:, ::-1]:
                if type(right_arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in right_arrival_time.loc[:, ::-1][i].values[0]:
                    subwaytime = str(right_arrival_time.loc[:, ::-1][i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                rightLastTime = subwaytime.strftime("%H:%M:%S")
                break
        return (leftFirstTime, leftLastTime, rightFirstTime, rightLastTime, subwayLine)
    
    def four(self, subwayname, subwaydir):
        subway_df = ''
        firstTrainTime = None
        lastTrainTime = None
        beforeLastTrainTime = None
        for idx, subway in enumerate(self.df):
            if subwayname in subway.values:
                subway_df = subway
                subway_index = idx
                break
        subwayLine = subway_index+1
        weekday = self.return_week_day()
        subway_line = self.line[subway_index]
        if subway_line.index(subwayname) < subway_line.index(subwaydir):
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상)') & (subway_df['구분'] == '도착')]
            if arrival_time.empty:
                arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(상))') & (subway_df['구분'] == '출발')]
        else:
            arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '도착')]
            if arrival_time.empty:
                arrival_time = subway_df.loc[(subway_df['역명'] == subwayname) & (subway_df['요일별'] == f'{weekday}(하)') & (subway_df['구분'] == '출발')]
        if not arrival_time.empty:
            for i in arrival_time:
                if type(arrival_time[i].values[0]) == str and ':' in arrival_time[i].values[0]:
                    subwaytime = str(arrival_time[i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                firstTrainTime = subwaytime.strftime("%H:%M:%S")
                break
            for i in arrival_time.loc[:, ::-1]:
                if type(arrival_time.loc[:, ::-1][i].values[0]) == str and ':' in arrival_time.loc[:, ::-1][i].values[0]:
                    subwaytime = str(arrival_time.loc[:, ::-1][i].values[0])
                else:
                    continue
                subwaytime = datetime.strptime(subwaytime, "%H:%M:%S")
                lastTrainTime = subwaytime.strftime("%H:%M:%S")
                try:
                    if type(arrival_time.loc[:, ::-1][str(int(i)-2)].values[0]) == str and ':' in arrival_time.loc[:, ::-1][str(int(i)-2)].values[0]:
                        beforeLastTrainTime = str(arrival_time.loc[:, ::-1][str(int(i)-2)].values[0])
                    else:
                        break
                except:
                    break
                break
        return (firstTrainTime, lastTrainTime, beforeLastTrainTime, subwayLine)
        
    
if __name__ == '__main__':
    subwaymethod = SubwayMethod()
    print(subwaymethod.two('동대구', '안심'))