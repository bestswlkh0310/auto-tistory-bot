from openai import OpenAI
from util.config import gptKey

# 주제를 입력하면 마크다운 형식의 내용을 반환합니디.
def writeContent(title):

  print('generating markdown content...')
  
  client = OpenAI(api_key=gptKey)

  prompt = f"""1. {title}에 대해 3000자 이상으로 작성해줘
2. 그 전체 내용을 markdown형식으로 변환해줘
상
3.체계적으로
4.인간이 쓴 것처럼
5.예시도 넣고, 충분히 구체적으로 작성해줘
6. 그 전체 내용을 markdown형식으로 변환해줘
  """

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "user", "content": prompt},
    ]
  )
  md = response.choices[0].message.content

  return md
