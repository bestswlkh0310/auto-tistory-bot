import markdown

# markdown텍스트를 html형식으로 변환합니다
def markdownToHtml(md):
    html = markdown.markdown(md)
    return html
