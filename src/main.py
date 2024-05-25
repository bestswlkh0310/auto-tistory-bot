from util.gpt.text import writeContent
# from util.markdown import markdownToHtml
# from util.tistory import post
# from datetime import datetime, timedelta

if __name__ == "__main__":
    titles = [
        '원하는 목표 이루는 방법'
    ]
    for (idx, title) in enumerate(titles):
        md = writeContent(title=title)
        print(md)
        # html = markdownToHtml(md)
        # now = datetime.now()
        # published = (now + timedelta(days=idx + 10)).timestamp()
        # print(published)
        # response = post(title=title, html=html, published=published)
        # print(response)