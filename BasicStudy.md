# 빅스비 IDE 공부내용(Bixby Develop)


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
