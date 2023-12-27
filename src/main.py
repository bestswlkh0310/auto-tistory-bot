from util.gpt.text import writeContent
from util.markdown import markdownToHtml
from util.tistory import post
from datetime import datetime, timedelta

if __name__ == "__main__":
    titles = [
    # "[파이썬] 파이썬 기초 문법과 활용",
    # "[파이썬] 파이썬 데이터 타입: 세트",
    # "[파이썬] 파이썬 데이터 타입: 딕셔너리",
    # "[파이썬] 파이썬 함수 기초",
    # "[파이썬] 파이썬 클래스와 객체지향 프로그래밍",
    # "[파이썬] 파일 입출력",
    # "[파이썬] 예외 처리",
    # "[파이썬] 모듈과 패키지",
    # "[파이썬] 가상 환경(Virtual Environment) 설정",
    # "[파이썬] 파이썬에서의 문자열 다루기",
    "[파이썬] 정규 표현식(Regular Expressions)",
    "[파이썬] 파이썬과 데이터베이스 연동",
    "[파이썬] 웹 스크래핑(Web Scraping)",
    "[파이썬] 데이터 시각화 - Matplotlib",
    "[파이썬] 데이터 시각화 - Seaborn",
    "[파이썬] 데이터 분석 - Pandas",
    "[파이썬] 머신러닝 기초 - scikit-learn",
    "[파이썬] 딥러닝 기초 - TensorFlow",
    "[파이썬] 딥러닝 기초 - PyTorch",
    "[파이썬] Flask를 활용한 웹 개발",
    "[파이썬] Django를 활용한 웹 개발",
    "[파이썬] 웹 개발에서의 보안 이슈",
    "[파이썬] RESTful API 개발 - Flask",
    "[파이썬] 자동화 스크립트 작성",
    "[파이썬] 데이터베이스 마이그레이션 - Alembic",
    "[파이썬] 웹 프레임워크 비교: Flask vs. Django",
    "[파이썬] 비동기 프로그래밍 - asyncio",
    "[파이썬] 유닛 테스트와 테스트 주도 개발(TDD)",
    "[파이썬] 코드 품질 검사와 정적 분석",
    "[파이썬] 파이썬에서의 다국어 지원",
    "[파이썬] 데이터베이스 연동 패턴",
    "[파이썬] 웹 보안 기초",
    "[파이썬] 웹 개발에서의 성능 최적화",
    "[파이썬] 데이터베이스 모델링",
    "[파이썬] ORM(Object-Relational Mapping) 개념과 활용",
    "[파이썬] 비동기 웹 프레임워크 비교: FastAPI vs. Quart",
    "[파이썬] AWS Lambda를 활용한 서버리스 개발",
    "[파이썬] 파이썬으로 간단한 블록체인 구현",
    "[파이썬] 데이터 사이언스와 머신러닝",
    "[파이썬] Jupyter Notebooks 사용법",
    "[파이썬] 파이썬에서의 함수형 프로그래밍",
    "[파이썬] 멀티스레딩과 멀티프로세싱",
    "[파이썬] 파이썬 코드 최적화 방법",
    "[파이썬] 웹 개발에서의 캐싱 전략",
    "[파이썬] 웹 개발에서의 로깅과 디버깅",
    "[파이썬] 파이썬 코드 리뷰 방법",
    "[파이썬] 데이터베이스 성능 최적화",
    "[파이썬] 웹 개발에서의 세션 관리",
    "[파이썬] 웹 개발에서의 JWT 인증",
    "[파이썬] 파이썬에서의 메모리 관리",
    "[파이썬] 웹 개발에서의 CSRF 방어 방법",
    "[파이썬] 웹 개발에서의 미들웨어 개념",
    "[파이썬] 파이썬으로 간단한 게임 만들기"
    ]
    for (idx, title) in enumerate(titles):
        md = writeContent(title=title)
        print(md)
        html = markdownToHtml(md)
        
        now = datetime.now()
        published = (now + timedelta(days=idx + 10)).timestamp()
        print(published)
        response = post(title=title, html=html, published=published)
        print(response)
