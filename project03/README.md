# 03 - Web(HTML/CSS를 활용한 웹 사이트 구성)

## 요구사항

* HTML/CSS를 활용해 웹 사이트의 레이아웃을 구성합니다.

1. `header`

   로고 이미지와 네비게이션 바를 구성합니다.

    * 속성

      	* 헤더는 항상 상단에 유지 됩니다.
         	* 다른 영역보다 우선하여 볼 수 있습니다.

      ```CSS
      header {
        /* 상단에 고정시키며(sticky) */
        /* position: sticky; */
        position: fixed;
        top: 0;
        /*다른 영역보다 우선하여 볼 수 있도록 작성하세요. */
        /* 1같은 값보다 큰 수를 주는 것이 좋음 */
        /* z-index: -1;  => 겹쳤을 때 가려지는 것 확인! */
        z-index: 1000;
      }
      ```

      * `sticky` vs `fixed`?
        * sticky는 자신의 위치를 가지고 있어서 margin을 0으로 줘야 공백이 생기지 않는다.

   * 네비게이션 바(`nav`)

     * 네비게이션 바의 항목은 우측에 배치합니다.

     ```css
     nav {
       /* navigation 항목을 오른쪽으로 정렬 시키세요.*/
       float: right;
     }
     ```

     * 총 4개의 항목을 배치합니다.

     ```css
     .nav-items > li {
       /* navigation 항목을 한 줄로 만들어 주세요. */
       display: inline-block;
       /* 좌우 여백을 지정하세요. */
       /* 상하 / 좌우 */
       margin: 0px 8px;
       /* li 태그의 bullet point를 제거 해주세요. */
       list-style: none;
     }
     
     .nav-items > li > a {
       /* a tag는 링크를 나타내며, 기본적으로 글자 색상이 파란색입니다. 원하는 색상으로 바꿔보세요. */
       color: #555555;
     }
     
     .nav-items > li > a:hover {
       /* hover는 마우스 오버시 모습입니다. 
       이때 하이라이트 되도록 다른 색상으로 바꿔보세요. */
       color: #850000;
       /* a tag를 마우스 오버하면 밑줄이 나타납니다.
       text를 꾸며주고 있는 밑줄을 없애보세요. */
       text-decoration: none;
     }
     ```

       * `display: inline-block`: inline 형태의 한줄
       * `line-style: none`: bullet point 제거
       * `text-decoration: none`: 밑줄 제거

2. title `section`

   서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다.

   * 속성

     * 수직 정렬을 통해 중앙으로 일치시킵니다.
     * 배경 이미지는 적절하게 삽입하고, 이미지에 맞게 사이즈와 위치를 조절합니다.

     ```css
     /* title section */
     #section-title {
       /* 배경 이미지를 적용 해보세요. (이미지는 images/background.jpg) */
       background-image: url("./images/background.jpg");
       /* 텍스트를 가운데 정렬 해보세요. */
       text-align: center;
       /* 텍스트를 수직 가운데 정렬 해보세요. (section-title은 높이가 300px) */
       line-height: 300px;
     }
     
     .section-title-heading {
       /* font size를 적절하게 조정 해주세요. (h1 기본 2rem) */
       font-size: 4rem;
     }
     ```
     
     * `background-image: url("이미지주소")`: 배경 이미지 넣기
     
     * `text-align: center`: 텍스트 가운데 정렬
     
     * `line-height: 크기`: 지정된 크기내에서 수직 가운데 정렬
     
       **주의 글씨 길어지면 넘어가버린다. 이런 점도 생각해주기!**

3. `aside`

   좌측 레이아웃에 장르 목록을 구성합니다.

   * 속성

     * 좌측에 위치하며, 상위 div 요소(#content)의 상단에 고정시킵니다.
     * 개별 장르는 `ul`태그를 활용하되 기본 안쪽 여백을 제거합니다.

     ```CSS
     /* aside */
     aside {
       /* aside를 부모인 div#content의 영역에 위치시키세요.
       div#content는 position: relative 입니다.
       */
       /* position: absolute; */
       position: absolute;
       top: 0;
     }
     
     .aside-items {
       /* ul 태그의 자동으로 적용된 padding을 제거 해주세요. */
       padding: 0;
     }
     
     .aside-items > li {
       /* li 태그의 bullet point를 제거 해주세요. */
       list-style-type: none;
     }
     ```

     * `position: absolute`: static을 제외한 가장 가까이 있는 조상요소 `div#content`(position: relative)에 위치하게 된다.

4. movie `section`

   우측 레이아웃에 제공된 영화 포스터를 활용하여 실시간 영화 순위 목록을 구성합니다.

5. `footer`

   연도와 이름이 작성된 푸터를 구성합니다.

   * 속성

     * 푸터는 항상 하단에 유지됩니다.
     * 높이는 40px이며, 모든 내용을 수직/수평 가운데 정렬합니다.
     * 적절한 배경 색상을 적용시킵니다.

     ```css
     /* footer */
     footer {
       /* footer는 항상 바닥에 위치하도록 position을 설정 해주세요. */
       position: fixed;
       bottom: 0;
       /* 텍스트를 가운데 정렬 해주세요. */
       text-align: center;
       /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 40px) */
       line-height: 40px;
     }
     ```

     

* 소스보기
  * [index.html](./index.html)
  * [reboot.css](reboot.css)
  * [style.css](style.css)
  * [layout.css](./layout.css)

* 결과 스크린샷

  ![결과화면1](./images/결과화면1.png)

  ![결과화면2](./images/결과화면2.png)

  

  