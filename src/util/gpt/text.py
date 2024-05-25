from openai import OpenAI
from util.config import gptKey

def writeContent(title):

  print('generating markdown content...')
  
  client = OpenAI(api_key=gptKey)

  prompt = f"""1. {title}을 주제로 3000자로 작성
2. 사람이 쓴 블로그 글처럼 자연스럽게 작성
3. 예시도 넣고, 충분히 구체적으로 작성
4. 그 전체 내용을 마크다운 형식으로 변환
"""

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "user", "content": prompt},
    ]
  )
  md = response.choices[0].message.content

  return md