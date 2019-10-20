import os
import wolframalpha
import wikipedia
from dotenv import load_dotenv
load_dotenv()

while True:
    raw_input = input("Whatcha wanna know: ")
    try:
        # wolframalpha
        app_id = os.getenv('WOLFRAM_ID')
        client = wolframalpha.Client(app_id)
        result = client.query(raw_input)
        answer1 = next(result.results).text
        print(answer1, '\n')
    except pass:
        # wikipedia
        lang = input("Which language do you feel comfortable with? ")[
            :2].upper()
        if lang == "":
            wikipedia.set_lang("ES")
        else:
            wikipedia.set_lang(lang)
        answer2 = wikipedia.summary(raw_input, sentences=3)
        print(answer2, '\n')
