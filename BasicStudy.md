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


