import os
import wolframalpha
import wikipedia
from dotenv import load_dotenv
load_dotenv()

while True:
    raw_input = input("Whatcha wanna know: ")
    app_id = os.getenv('WOLFRAM_ID')
    client = wolframalpha.Client(app_id)
    result = client.query(raw_input)
    # answer1 = next(result.results).text
    lang = input("Which language do you feel comfortable with? ")
    wikipedia.set_lang(lang[:2].upper())
    answer2 = wikipedia.summary(raw_input, sentences=3)
    # print(answer1)
    print(answer2)
