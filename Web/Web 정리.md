# HTML and WEB

### HTML 기본구조

1. html : 문서의 최상위 요소
2. head : 문서 메타데이터 요소, 제목, 인코딩, 스타일, 외부 파일 로딩 등
   - title : 브라우저 상단 타이틀
   - link : 외부 리소스 연결
   - style :  CSS 직접 작성
3. body : 문서 본문 요소, 실제 화면 관련된 내용



### HTML 기본

- 요소(element)
  - 항상 여는 태그와 닫는 태그 안에 내용이 들어간다 <>content</>
  - 내용이 없는 태그들 br, hr, img, input, link, meta
  - 텍스트 요소
    - a : href속성을 활용하여 다른 URl로 연결하는 하이퍼 링크 생성
    - b, strong : 굵은 글씨 요소, 후자는 시스템 내에서 더 강조됨
    - i, em : 기울임 글씨 요소, 후자는 시스템 내에서 더 강조됨
    - img : src 속성을 활용하여 이미지 표현
    - spn : 의미 없는 인라인 컨테이너
  - 그룹 컨텐츠
    - p : 하나의 문단 (paragraph)
    - hr : 주제를 분리하기 위한 수평선
    - div : 의미 없는 블록 레벨 컨테이너
    - ul, ol, dl : 목록을 만들어 준다. 내용물은 li, list-style-type: none;으로 불릿 없애기 가능.
  - form, input
    - form : 사용자의 정보를 제출하기 위한 영역, action은 처리할 서버의 url, method 는 제출시 사용할 HTTP 메서드 (GET 혹은 POST)
    - input : 입력 데이터 유형과 위젯이 제공됨, name은 form control에 적용되는 이름, value는 form control에 적용되는 값
    - input type으로 test, password, email, number, file등 속성을 정할 수있다.
    - input label : label을 클릭하여 input의 초점을 맞추거나 활성화 시킬 수 있음. input에 id속성을  label에는 for속성을 활용하여 상호 연관을 시킨다. <b>label에 for이다!!</b>
    - label로 checkbox : 다중 선택, radio : 단일 선택으로 항목으로 선택할 수 있는 input 제공
    - 그 외에 다양하게 많음.
- 속성(attribute)
  - \<a href = ""> 에서 href 처럼 태그별로 사용할 수 있는 속성과 속성값이 있다.
  - 태그에 부가적인 정보를 설정할 수 있다.
  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 -> id, class, style
- 구조
  - header, section, footer 외에도 구조 나눠서 할 수 있다.



### CSS (Cascading Style Sheets)

- 스타일을 씌우는 방법
  - 인라인 (Inline)
  - 내부 참조 \<style>
  - 외부 참조 CSS파일 - head 내에서 \<link rel="stylesheet" href="css파일 주소"> 로 참조
- 선택자 (Selector)
  - 기본선택자
    - 전체 선택자 : * { 전체에 속성부여 }
    - 요소 선택자 : 요소 { 특정 요소에 속성 부여 }
    - 클래스 선택자 : .클래스 { 특정 클래스에 속성 부여 }
    - id 선택자 : #id { 특정 id에 속성 부여 }
    - 속성 선택자 : [속성] { 특정 속성을 가진 요소에 속성 부여 }
  - 결합자
    * 자식 결합자 : 선택 > 선택 { 직계 자식에게 속성 부여 }
    * 자손 결합자 : 선택 선택 { 그냥 포함되어 있는 자손에게 속성 부여 }
- CSS 적용 우선순위 (cascading order)
  - !importtance 사용시 무조건 1순위
  - 인라인 > id > class, 속성 > 요소
- CSS 상속
  - 속성을 통해서 부모 요소의 속성을 자식에게 상속한다.
  - 상속 되는 것 : Text 관련 요소 (font, color, text-align) , opactiy, visibility 등
  - 상속 되지 않는 것 : Box model 관련 요소 (width, height, margin, padding, border, box-sizing, display), , position (position, top/right,/bottom/left, z-index)  관련 요소 등

- Box model
  - Box는 margin, border, padding, content로 구성되어 있다.
  - margin : 테두리 바깥의 외부 여백, 배경색 지정 불가
  - border : 테두리 영역
  - padding : 테두리 안쪽의 내부 여백
  - content : 실제 내용
  - margin, padding의 경우 top, right, bottom, left로 각각 값을 할당 할 수 있으며, 그냥 값을 적을 경우 상하좌우 전부 할당. 혹은 shorthand로 위에서부터 시계방향으로 할당 되는 듯, 3개면 상 우 하, 좌는 우랑 같음.
  - border-width : 하면 테두리 길이 상하좌우로 적용. 이것도 두께 속성 색깔로  shorthand 가능.
  - box-sizing : content-box (콘텐트 영역), border-box (테두리 기준), initial (기본값), inherit (상속)
  - 부모 상대적 크기 조절 : w-auto, h-auto
  - 뷰포트 상대적 크기 조절 : min-vw-auto, max-vh-auto
- Display
  - block과 inline 설정 가능하다.
  - text-align으로 정렬 할 때, iline이 아닌 block에 정렬해 줘야함.
  - inline-block을 ㅇㅇㅇ쓰면 linine처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성가짐.
  - none : 화면에 표시하지 않고, 공간 부여안됨. visibility : hidden은 공간차지하고 표시 안됨.
- Position
  - static : 모든 태그의 기본 값. 일반적인 요소의 배치 순서에 따름. 부모 요소 내에서 배치시 부모 요소의 위치 기준으로 배치됨
  - relative, absolute, fixed, sticky는 property(top, bottom, left, right)를 사용하여 배치 가능
  - relative : normal flow 유지하고 static위치를 기준으로 이동
  - absolute : normal flow에서 벗어나 가장 가까이 있는 부모/ 조상요소를 기준으로 이동 ( 없는경우 body )
  - fixed : normal flow에서 벗어나 viewport를 기준으로 이동
  - sticky : 스크롤에 따라 static에서 fixed로 변경.
- Layout
  - Float 속성 : left 왼쪽으로 띄움, right 오른쪽으로 띄움, Normal Flow에서 벗어난 레이아웃 구성 가능.
  - Flexbox : Normal flow를 벗어난 구성을 하기 위해, float 혹은 position을 사용했지만 flex가 더 용이.
    - display : flex 혹은 inline-flex로 지정하여 형성. flex-container, flex-items
    - flex-direction : row, row-reverse, column, column-reverse 가능. 축방향 바뀌니 주의.
    - flex-wrap : 컨테이너를 벗어나는 경우 줄바꿈해서 배치. wrap이 줄바꿈 해주는 것.
    - flex-flow : direction과 wrap의 shorthand 가능.
    - justify-content : flex-start, flex-end, center, space-between, space-around, space-evenly 축정렬.
    - align-content : 위와 같으나 축의 수직방향으로 정렬. around는 둘러싼 영역을 균일하게, evenly는 아이쳄간 간격을 균일하게 분배하여 정렬.
    - align-items : stretch, flex-start, flex-end, center, baseline. flex 내부의 items의 정렬 가능.
    - align-self : 개별 아이템을 축의 수직 기준으로 정렬.
    - flex-grow : 남은 영역을 아이템에 분배
    - order : 배치 순서

- Bootstrap

  - Spacing
    - CDN을 활용하여 쉽게 스타일 적용 가능.
    - rem은 폰트 사이즈에 비례해서 크기가 조절된다. 기본은 16px.
    - mx 는 margin left와 right를 동시에 적용 가능. 따라서 mx-auto는 평 중앙 정렬.
    - py 는 padding top와 bottom을 동시에 적용 가능. 

  - Color
    - primary, secondary, success, info, warning, danger, light, dark 등등.. bg, text와 조합.
  - Hiding
    - d-xs, sm, md, lg, xl-none or block 을 이용해서 화면 크이게 따른 숨기기 가능.
  - 반응형 웹 디자인
    - Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag 등 이용해서 구현.

- Grid system

  - 기본 요소
    - Column : 실제 컨텐츠를 포함하는 부분, 총합은 12개.
    - Gutter : 칼럼과 칼럼 사이의 공간
    - Container : Column들을 담고 있는 공간
    - container > row > col 같은 형식으로 사용.
    - offset-breakpoints-col 을 이용해서 옆에 공백 삽입 가능.
  - Available break points
    - 576px < sm < 768px < md < 992 < lg < 1200 < xl < 1400 < xxl