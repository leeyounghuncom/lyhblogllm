# 프로젝트 제목
LLM OpenAI GPTs 블로그 업로더 (이영훈닷컴 LLM)
<br>
# 프로젝트 소개
이 프로젝트는 OpenAI의 GPTs 모델을 활용하여 자동으로 블로그 글을 생성하고 업로드하는 시스템입니다. 사용자는 주제를 입력하면, GPTs 모델이 관련 내용의 블로그 글을 작성하고, 이를 웹사이트에 자동으로 업로드할 수 있습니다.
<br>
# 개발 기간
2024.09.02.~2024.09.05
<br>

# 주요 기능
**블로그 글 생성:** 사용자가 제공한 주제에 대해 GPTs를 사용하여 상세한 블로그 글을 생성합니다.<br>
**자동 업로드:** 생성된 블로그 글을 사용자의 웹사이트에 자동으로 업로드합니다.<br>
<br>

# 기술 스택
**언어:** Python 3.12.X<br>
**프레임워크:** Django 4.2 DRF  (웹 서버 관리), GPTs OpenAI (블로그 글 생성)<br>
기타 도구: HTML5/CSS3 (프론트엔드 디자인)
<br>
# ERD
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/erd.png?raw=true)
<br>
# RESTful API 명세서
 명칭      | Endpoint        | Method      
|---------|-----------------|-------------|
 리스트,글등록 | docs/           | GET, POST   
 글수정,삭제  | docs/<int:pk>   | PUT, DELETE 
 상세페이지   | <slug:doc_name> | GET        

# 설치 및 실행 방법
* pip install -r requirements.txt
* .env 확인
* python manage.py migrate
* python manage.py runserver


# GPTS 스키마 적용 방법
1. GPTS -> 작업 -> 설명 
2. 스키마 클릭 
3. api.yaml 내용 복사
4. 스키마 붙여 넣기 


# 시연 영상 링크
https://www.dropbox.com/scl/fi/txngyhrlv3rp9k2oeuxaw/LLM-2.mp4?rlkey=8p54wtk9022bzb450lk6sryls&st=6h1yarj8&dl=0

# 프론트엔드 캡쳐
## 와이어프레임
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/20240909_173848.jpg?raw=true)
## 목록
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/LLM02.png?raw=true)
## 상세
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/LLM03.png?raw=true)
## GPT 프롬프트
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/LLM01.png?raw=true)

# 연락처
**이메일:** dosiraklab@gmail.com
**연락처:** 010-5659-7567
