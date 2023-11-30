from util.gpt.text import writeContent
from util.markdown import markdownToHtml
from util.tistory import post
from datetime import datetime, timedelta

if __name__ == "__main__":
    titles = [
        '[kotlin] if문과 when문에 대해 알아보자',
        '[python] if문을 알아보자',
        '[pytohn] 3.10버전에 추가된 match-case 문',
        '[python] 리스트와 튜블에 대해 알아보자',
        '[python] 딕셔너리에 대해 알아보자',
        '[python] for문과 while문을 알아보자'
    ]
    for (idx, title) in enumerate(titles):
        md = writeContent(title=title)
        print(md)
        html = markdownToHtml(md)

        now = datetime.now()
        published = now + timedelta(days=idx + 1)
        response = post(title=title, html=html, published=published)
        print(response)
