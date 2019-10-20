import os
import wolframalpha
from dotenv import load_dotenv
load_dotenv()

raw_input = input("Whatcha wanna know: ")
app_id = os.getenv('WOLFRAM_ID')
client = wolframalpha.Client(app_id)

result = client.query(raw_input)
answer = next(result.results).text

print(answer)
