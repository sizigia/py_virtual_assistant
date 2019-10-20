import os
import wolframalpha
import wikipedia
from dotenv import load_dotenv
load_dotenv()

raw_input = input("Whatcha wanna know: ")
app_id = os.getenv('WOLFRAM_ID')
client = wolframalpha.Client(app_id)

result = client.query(raw_input)
# answer1 = next(result.results).text
answer2 = wikipedia.summary(raw_input)

# print(answer1)
print(answer2)
