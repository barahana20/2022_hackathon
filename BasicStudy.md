# 빅스비 IDE 공부내용(Bixby Develop)


### 1. Introduction 
+ Capsule : 빅스비 서비스를 제공하기 위해서, 빅스비 플랫폼 서버에서 실행되는 최소 단위의 빅스비 서버 어플리케이션. 빅스비 서비스를 개발한다고 하는 것은 빅스비 캡슐을 개발한다고 생각하면 된다.

+ 캡슐 안의 기능 
  - 최상단 제일왼쪽 버튼 : Workspace를 가져올 수 있다. Existing Capsule과 같은 기능.혹은 Capsule을 하나 생성할 수 있다.
  -  Capsule ID 생성하는 규칙 : (namespace.capsuleName)
    - example.~~~~~ 혹은, playground.XXXXX , 혹은 자신만의 namespace.OOOO
    
    - example 이라고 해 놓으면, Bixby Developer Center 또는 Developer들을 위한 github에서 example들을 다운로드하면, example 을 가진 ID를 가진 경우가 대부분이라고 한다.
    - playground 라고 하면,  이 캡슐은 개발시에 테스트, 코드, 시뮬레이션, 디버깅 가능하나, 이것을 빅스비 public, private submission을 통해 단말에서 테스트하는 것이 불가능하다.
    - "what" 처럼 독특한 namespace를 사용하려고 하면, Bixby Developer Center의 메인스페이스와 캡슐 name을 등록해야 한다. 
    - 내가 이 개발환경에서 개발하여, bixby platform 에서 private 혹은 public submission 을 통해서 실제적으로 사용자들에게 제공할 것임을 의미한다. (필요!)

  - Submission  하는 방법 
    -  VIew 에서 Submission 하면, 실제 빅스비 서비스에 등록될 수 있다. 

+ 추가적인 IDE 기능
  - Open Debug Console : 코드에 대한 디버깅 가능.
  - Open Simulation Debugging 
    - 어떤 사용자의 말에 반응하도록 트레이닝하는지 : resource.training으로 만든다. 사용자가 어떤 말을 했을 때 어떻게 트레이닝하는지 내용이다. 
    - ex) 버거 둘 콜라 하나 주문해줘 라고 보냈을 때, NL 모델에 complie 되는지 처리함. 시뮬레이터 실행할려면 open in simulator 화면에다가 처리한다. 

  - Command Palette : 팔레트 창을 통해서 쉽게 실행가능하다. 


### 2. Simulation & Debugging

+ Bixby Capsule 구조 : 크게 3가지 부분에 대해서 개발이 진행되고, 한개의 training이 진행된다



  - code & models
    - 사용자가 빅스비에게 어떤 말을 했을 때, 사용자가 한 말이 어떤 의미를 가지는지, 그중에 중요하게 생각해야 되는 명령은 무엇인지 등 빅스비가 사용자의 말을 쪼개어 분석하고, 어떤 일을 하고싶은지를 분석하는 부분.이 부분에 대한 설계 및 구현은, models라고 하는 folder에서 진행된다. code 아래의 models folder 에서 처리된다.

    - models에서 사용자의 말을 분석했을 때, 그 분석된 내용을 알아내게 된다면, code의 내용을 통해서 빅스비가 실제로 그 일을 처리할 수 있도록 처리된다. 
  
  - resources
    - 만약 code에서 결과가 다 처리되게 된다면, 이것은 resource folder 내의 layout 구성을 통해서 더 이쁘게 처리될 수 있다(안해도 괜찮기는 한데, UI를 더 이쁘게 할거면 하면 된다.)
    - 코드가 모두 완성되면, 사용자 말을 조금 더 잘 알아듣게 하기 위해서, 트레이닝 기능을 이용해 bixby에게 사용자 말을 더 잘 알아듣게 하는 기능이 들어감. training, 실행에 대한 기능이 주로 들어간다. (with resource folder)

  - capsule.bxb : 캡슐에 대한 설정파일. 타겟이 어떤 단어인지 설정할 수도 있다. 트레이닝 언어 선택 가능.


+ 그럼 어떻게 flow가 흘러가는데?
  - ko-KR 안에서의 traning 에서, training 을 만들어서 트레이닝 시킬 수 있다. 시킨 뒤 시뮬레이터 버튼을 통해 시뮬레이팅할 수 있다. 왼쪽 하단의 핸드폰 버튼도 같은 시뮬레이터 버튼이다. 
  - 이때 캡슐이 어떻게 실행시켰는지 궁금할 때, 거미처럼 생긴 디버깅 버튼을 클릭하거나, View-Open Debug Console 에 들어가면 어떻게 처리되는지 알 수 있다.

  - 그래피컬한 그림이 나오면서 확인이 가능하다. 
  - 사용자 말을 어떻게 받아들였는지 파악이 가능하다. 

  - 사용자 말에서 중요하게 생각되어야 하는 내용들이 들어가서 진행됨을 알 수 있었다. 
  - 비즈니스 로직은, code에서 js 파일을 이용해 짤 수 있다. 

#### Tip : Resource 소개

+ Bixby Developer Center : Getting Started 부터 Sample까지, bixbydevelopers.com 에서 공부할 수 있는 내용이 있다. 구글링을 하는 것도 좋지만, 여기서 확인해 보는것도 좋을 것이다. 

+ Bixby Developer Github : 샘플코드들을 모아놓은 Repo들이다. 한국 샘플들도 많으니 참고하면 될듯하다. 깃헙에서 코드 많이 찾아보는것도 좋을 것 같다. 

+ More info : 
  - support@bixbydevelopers.com 
  - support.bixbydevelopers.com


### 3. 빅스비 캡슐 구조

+ 메인이 되는 Architecture는 Client - Server Architecture이다. 
  - 그렇다면, 빅스비 플랫폼에서는 빅스비를 어떻게 동작시키며 개발되어야 하는 것은 무엇인가?

+ Bixby Service Architecture 
  - 음성 인식과 자연어 이해
  - 음성인식(ASR) : 발화를 문자로 변환하는 기술 
  - 자연어이해(NLU) : 인간이 말하는 자연어가 어떻게 되는지 이해하는 기술
  -  ex) 오늘 서울 날씨 알려줘 
    -  날짜 : 오늘/지역 : 서울/action : 날씨 알려줘
  - 서버 side에서 동작한다 

+ 어떤 flow로 동작하는지?
  1. 빅스비 실행됨
  2. 사용자 발화 발생
  3. 음성파일이 빅스비 서버 도착
  4. ASR모듈을 통한, 문자 변환 및 오늘날씨 알려줘에서 NLU모델로 어디로 가야되는지 알려줌(날씨캡슐)
  5. 해당 발화가 어떤 의도이며, 동작하기 위해 필요한 값이 어떤 것인지 분석
  6. Intent : 날씨 정보 / 필요값 : 오늘,서울
  7. 빅스비 플랫폼 자체기술로, 실행 절차를 나타내는 플랜그래프 생성(플랜은, 결과값을 생성하기 위해 할 일을 순서도처럼 나타낸 것)
  8. 실제 개발자가 구현한 자바스크립트 파일 실행. 
    8.1 외부 서버 연동이 필요하면, 외부 API 호출해 결과 받거나, 결과를 위한 연산 실행
    8.2 서버로부터 클라로 전달. 그래서 사용자에게 보여지게 된다. 

+ 플랜은 무엇을 기준으로 생성되는가 ? : 개발할 캡슐을 기반으로 생성된다. 
  - 동작을 실행하기 위한 계획을 가장 효율적인 방법으로 재구성한 것이 플랜그래프이다. 
  - 서비스를 잘 구현하기 위해서는, 캡슐만 잘 만들면 되지만, 캡슐을 잘 만들어야 한다. 캡슐을 잘 만들어야만, 캡슐이 잘 분류되고, 발화의 의도를 잘 파악할 수 있다.. 여기에 집중해야 함. 

+ Bixby 캡슐 구조(4가지 영역)
  - 어떤 서비스를 실행시킬지에 대한 모델링
    - 모델링 영역의 두가지 Component : 
      - Concept : 사용자 발화 인식/리턴할 때 필요한 값. ex) 햄버거 두개 : 햄버거(종류)/두개(갯수)
      - Action : 캡슐이 사용자의 원하는 작업을 이해할 수 있도록 수행할 동작을 정의 
      
  - 모델링한 계획을 코딩하는 비즈니스 로직 : 사용자가 원하는 작업을 실제 수행하는 코드. 서비스 API를 실행하기도 한다. JS기준
   
  - 어떻게 보여줄지 UI/UX :  
    - Bixby Views(사용자에게 보여주는 Layout)
    - Dialog : 사용자에게 되묻거나 결과를 응답해주는 응답문을 생성해 줌
   
  - Capsule이 잘 동작하도록, 처리할 수 있는 바로하를 생성하고, 자연어 트레이닝을 진행
    - 발화 Training : 사용자가 똑같은 말을 하는 것이 아니므로, 추가적인 자연어 트레이닝을 진행
    - 디버깅 : 개발한 캡슐이 잘 동작하는지 테스팅하는 디버깅 부분. 



