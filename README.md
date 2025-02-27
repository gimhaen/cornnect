# 목차

1. 팀원 정보 및 업무 분담 내역
2. “영화 추천 서비스” 선택 배경
3. 서비스 소개
4. 대표 기능 소개
5. 시연
6. 개발도구
7. 설계
8. 데이터 베이스 모델링 ERD
9. 프로젝트 일정 및 기타 산출물
10. 느낀점 및 후기

---

# 팀원 정보 및 업무 분담 내역

### 김해인 팀장

와이어 프레임 제작

TMDB API 연동 및 ERD 모델링

영화 검색 기능 구현

로그인/로그아웃, 회원가입 기능 구현

### 전온겸 팀원

ERD 설계

뷰 컴포넌트 설계

영화진흥위원회 API 연동

게시글 정렬 및 프로필 관리 기능 구현

# “영화 추천 서비스” 선택 배경

### 영화 추천 서비스 특징

- 콘텐츠 다양성
- 데이터 수집 용이성
- 높은 접근성

# CORNNECT - 소개

![CORNNECT](assets\cornnect.png)

### 팝콘의  ‘corn’과 연결하다의 ‘connect’를 합성한 **’cornnect’**

마치 팝콘처럼 즐거운 영화 소통을 연결하는 플랫폼입니다.

여기서 '콘'은 '팝콘'에서 영감을 받았고, '넥트'는 '연결하다'라는 의미를 담고 있습니다.

"콘넥트"는 사용자들이 함께 영화를 즐기고 소통하는 경험을 제공하며, 영화 커뮤니티를 한 단계 더 활성화시키는 역할을 합니다. 

# 대표 기능 소개

### 메인 페이지

사용자들이 작성한 리뷰 리스트 및 박스오피스 순위 제공

### 영화 검색 페이지

검색에 도움을 주고자 박스오피스 순위를 10위까지 제공

키워드를 검색하면 해당 키워드와 관련된 영화 제공

### 영화 상세 페이지

영화의 리뷰와 톡(가벼운 대화), 영화의 기본정보 제공

# 시연

# 개발 도구

![Tool](assets\tool.png)

# **설계**

### 와이어 프레임

![frame](assets\frame.png)

### **Architecture 설계도**

![Architecture](assets\Architecture.png)

### API 명세서

![API](assets\API.png)

# 데이터 베이스 모델링 ERD

![ERD](assets\ERD.png)

# 프로젝트 일정
### 5.18 
뷰 컴포넌트 작성, 로그인 구현
### 5.17
영화진흥위원회 API 이용하여 박스오피스 구현, 로그아웃 구현
### 5.19
피그마 수정
### 5.20 
ERD 모델링 수정, TMDB API 가져오기
### 5.21
작성하기 모달, 메인 리뷰 생성 및 조회
### 5.22
프로필 모달, 작성하기 검색창 구현
### 5.23 
상세 영화페이지 리뷰, 톡, 기본정보 작성


# 느낀점 및 후기

### 김해인
처음에는 프론트엔드를 맡기로 했다가 예상 외로 백엔드 작업을 많이 하게 되었는데, 백엔드가 어렵다고만 생각했는데 직접 코드를 작성하며 논리 구조를 이해하고 함수가 제대로 수행되는지 중간중간 확인하는 과정에서 재미를 느끼게 되었다. 그러나 작업 중에도 자꾸 백엔드 작업을 하다가도 프론트엔드 쪽에 더 시간을 투자하는 경향이 있었다.  초반에 방향을 잡지 못해서 시간을 효율적으로 사용하지 못한 점이 아쉽지만, 이번 기회를 통해 백엔드와 프론트엔드 모두 경험하면서 각각의 재미를 느끼고 나에게 더 흥미있는 분야를 찾을 수 있어 좋은 경험이었다.
### 전온겸
프론트엔드를 맡게 되어 디자인과 사용자 경험 측면에서 많은 것을 배울 수 있는 유익한 경험이었다.
팀프로젝트를 통해 서로 다른 역할을 맡아 각자의 전문성을 발휘하고 상호 보완하는 과정에서 소통과 협력의 중요성을 더욱 느낄 수 있었다.
특히, 서로의 아이디어를 존중하고 수용하는 과정에서 팀원과의 신뢰와 친밀감이 쌓였다.
영화진흥위원회에서 API를 활용하여 정보를 가져오는 과정은 매우 어려웠지만, 흥미로웠다.
이번 프로젝트를 통해 개발자로서의 역량을 키우는 데 큰 도움이 되었다. 프로젝트를 진행하면서 자신의 역할에 충실하고 끊임없이 노력하는 중요성을 배울 수 있어 뜻 깊은 활동이었다.