## 바로인턴 백엔드 과제(Python)
본 프로젝트는 Django와 JWT를 활용한 인증 시스템 구현 과제입니다.
Pytest 기반 테스트와 Swagger 문서화, 그리고 AWS EC2 배포까지 완료된 상태입니다.

## 사용 기술
- Python 3.12
- Django 4.2
- djangorestframework
-drf-yasg (Swagger)
- Pytest
- AWS EC2 (ubuntu 22.04)
- MobaXterm (접속 중)

## 주요 기능

- 회원가입 (username, password, nickname)
- 로그인 (JWT 토큰 발급)
-  인증 실패 예외 처리
- Swagger API 문서화 `/swagger/`
- Pytest를 통한 기능별 테스트 코드 작성
- EC2 배포 및 외부 접속 확인

## 배포 주소
http://43.202.46.113:8000


> `/signup/`, `/login/`, `/swagger/` 엔드포인트 접속 가능
---

## 🧪 실행 방법 (로컬 개발용)

```bash
git clone https://github.com/yourusername/intern-assignment.git
cd intern-assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
![Swagger_페이지](![Image](https://github.com/user-attachments/assets/6705850c-2a7f-4926-ac7e-d7ae9843989d))
