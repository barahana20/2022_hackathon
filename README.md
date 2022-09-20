# 대구지하철 열차정보 Bixby Application 

<center>by 남동우(WhalesBob) & 이주형(Barahana20)</center>

<br>
<a href="https://knuackr-my.sharepoint.com/:w:/g/personal/barahana10_knu_ac_kr/EbICyawTQSlBqL_vOaKbE7sBf9B10W5Q-NhaCcg8_8gVxw?rtime=HolbYPua2kg">공유문서 바로가기</a>

### User Requrement

1. 빅스비로 "대구 지하철" 실행.
2. 빅스비가 질문하기
3. "~~역 ~~방면 가르쳐 줘!"
4. 빅스비의 대답
    - 해당 역 열차 도착시간(몇분 남았는지) 알려주기
    - 혹은 해당 역 첫차/막차 시간 알려주기
    - 소요시간(importance : Low)
  
### System Requirement 

1. "대구 지하철" 발화 시 Bixby Application 실행
2. Bixby 질문하기 
3. 사용자의 발화
     1. "~~역 (가르쳐 줘)!"
        - 양 방향 도착정보 1개씩(몇분 남았는지), with 첫차막차 시간 대답으로 띄우기
     2. "~~역 ~~방향(가르쳐 줘)" 
        - 1개 방면 도착정보 2개씩(몇분 남았는지), with 첫차막차 시간 대답으로 띄우기
     3. "~~역 첫차" or "~~역 막차" (둘다 말했을 때도 대응시키기)
        - 2개 방면 첫차 or 막차 시간 알려주기

     4. "~~역 ~~방향 첫차 or 막차" 
        - 해당 방면 첫차 or 막차 시간 알려주기
        
 4. About View
    - 추후 고려해서 채워넣기(Like Azile)




