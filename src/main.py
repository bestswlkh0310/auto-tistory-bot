from util.gpt.text import writeContent
from util.markdown import markdownToHtml
from util.tistory import post
from datetime import datetime, timedelta

if __name__ == "__main__":
    titles = [
        '클라우드 컴퓨팅의 기초와 활용',
        '머신 러닝의 기초와 실전 응용',
        'UX/UI 디자인의 중요성과 가이드라인',
        '알고리즘과 자료 구조의 이해',
        '최적화된 데이터베이스 설계 방법',
        '개발자를 위한 건강과 스트레스 관리',
        '앱 개발과 사용자 경험 (UX) 설계'
    ]
    for (idx, title) in enumerate(titles):
        md = writeContent(title=title)
        print(md)
        html = markdownToHtml(md)
        
        now = datetime.now()
        published = (now + timedelta(days=idx + 1)).timestamp() * 1000
        print(published)
        response = post(title=title, html=html, published=published)
        print(response)
