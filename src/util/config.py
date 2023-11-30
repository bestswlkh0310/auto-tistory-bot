
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

print('loading config...')

gptKey = os.environ.get('gpt-key')
blogName = os.environ.get('blog-name')
tistoryKey = os.environ.get('tistory-key')