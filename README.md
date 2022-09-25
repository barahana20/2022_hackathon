# 해커톤 보고서 - [자유 세션] 대구도시철도 열차정보 Bixby Application
- 팀명
  - 대프리카김밥천국
  
- 제출 세션 및 주제
  - 자유 세션 - 대구도시철도 열차 정보 알리미

- 프로젝트 한 줄 설명
  - 대구도시철도 열차 정보를 빅스비를 이용해 간단하게 확인 가능

- 프로젝트에 대한 설명
  - 저희는 알람을 맞추거나 날씨 정보를 확인할 때 "시리야", "하이 빅스비" 등 음성 인식 AI를 통해 편하게 사용합니다.
  - 하지만 도시철도 도착 시간을 확인하기 위해서는 '지하철종결자', '대구도시철도 앱', '네이버 지도' 등 지하철 관련 어플리케이션을 실행해 일일이 검색해 봐야한다는 불편함이 있었습니다.
  - 저희는 이러한 불편함을 해결하기 위해 삼성 빅스비 AI 응용 서비스를 개발했습니다.
  - 이제는 빅스비를 통해, <u>대구 시민들은 대구도시철도 열차 정보에 대해서 쉽고 편하게 확인</u>할 수 있을 것입니다.

- 프로젝트에 사용된 기술
  - 프론트 엔드(FE) 기술 : Bixby Platform
    - NodeJs 기반 JavaScript와 Bixby 언어를 활용하여, 빅스비를 통해 사용자와 소통할 수 있게 함.
  - 백엔드(BE) 기술 : Python Flask, Bixby AI, AWS
    - Python Flask Framework를 사용하여 API 서버를 구축
    - 24시간 서비스를 위해 AWS EC2 를 이용해 API 서버를 호스팅
    - Bixby AI 에게 많은 Training Data를 학습시켜 사용자 예상 발화를 인지함

- 시연 영상
  - 유튜브 링크
