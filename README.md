# 이영훈닷컴 LLM

# 프로젝트 소개
이영훈닷컴 블로그를 !<br>

# 개발 기간
2024.09.02.~2024.09.05<br>

# 개발 환경
**Python** : Django DRF<br>
**DB** : SQlite<br>

# ERD
![image](https://github.com/leeyounghuncom/lyhblogllm/blob/main/etc/erd.png?raw=true)

# RESTful API 명세서
 명칭      | Endpoint        | Method      
|---------|-----------------|-------------|
 리스트,글등록 | docs/           | GET, POST   
 글수정,삭제  | docs/<int:pk>   | PUT, DELETE 
 상세페이지   | <slug:doc_name> | POST        

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
