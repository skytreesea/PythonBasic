논문 크롤링 개발 중 by 김창현

<요약>
'23.2.6. 현재 '마이라이브러리'를 개발 중 아직까지는 저자 이름으로 논문 제목을 찾아 저장하는 초보적인 수준임, 
- 결정사항
1) 국내/국외 논문, 특허정보(추후)를 같은 로직으로 찾을 것인지? 
2) 국내 학위논문과 학술지논문에만 한정한다면 현재로서는 Riss 정보만으로 추출 가능(하지만 사이트 개선/개발 시 코드가 무력해질 가능성)
3) 궁극적으로 구글 스콜라를 크롤링하는 것이 최종 목적임(현재 공인된 api는 제공하지 않고 있으며, 사재 api는 무척 비쌈)

1. 국회도서관 api를 활용한 크롤링 사례
https://github.com/skytreesea/PythonBasic/blob/master/crawling/paper%20search/paper_crawling_v1.py

- 개발개요: 국회도서관 api key를 받아 사용(누구나 key를 금방 받을 수 있음)
- 개발단계: 제목 정도는 프린트 해서 보여줄 수 있는 단계(특정 키워드로 개인 정보를 세밀하게 파고드는 코드를 작성하는 데에는 시간 필요)
- 개발언어: Python
- 장점: 정상적으로 작동하는 코드
- 단점: 필드 값이 <name>과 <value>로만 되어 있어 논문이나 저서를 구별하는 로직을 별도로 개발해야 함, 어렵지는 않으나 약간의 시간이 소요됨 

* 같은 원리로 루비(Ruby on rails)로도 코드를 짰음
https://github.com/skytreesea/PythonBasic/blob/master/crawling/paper%20search/nokogiri_pure_test.rb

2. 구글 스콜라를 쌩 크롤링 
https://github.com/skytreesea/PythonBasic/blob/master/crawling/paper%20search/paper_crawling_python%20google%20test.py

- 개발개요: 구글에서 수집해준 자료를 다시 한 번 크롤링하는 단계 
- 개발단계: 아직 쌩 초보 단계, 개발에 시간 필요, 가능해보임 
- 개발언어: Python
- 장점: 여러 방법을 활용해봤지만, 구글 스콜라의 기능이 현재로서 가장 정확하게 크롤링 가능, 국내 국외 모두 개발 가능
- 단점: 구글 스콜라는 공식 api를 제공하지 않음, 쉽게 크롤링할 수 있는 api는 유료로 구매해야 함 
* 특이사항: scholarly 와 같은 라이브러리가 있음 

3. 리스(Riss)
https://github.com/skytreesea/PythonBasic/blob/master/crawling/paper%20search/riss/riss.py

- 개발개요: RISS 학술정보 사이트에서 get 방식으로 데이터를 입력해서 필요한 데이터를 클립보드로 옮겨주는 단계
- 개발단계: 예전 개발 코드, 바로 결과값 출력 가능한 상태 
- 개발언어: Python
- 장점: 국내 학위논문은 거의 다 추출 가능, 어느 정도 검증된 코드(2년 전 짜놓았는데 아직까지 working함)
- 단점: Riss는 국내 논문만 신뢰성 있음, 해외 논문 코드는 별도로 개발해야 함

