from fastapi import FastAPI,Request
from fastapi import WebSocket
import speech_recognition as sr
import re
from deep_translator import GoogleTranslator
import requests
import tempfile
from extractor import extract_information
from urllib.parse import unquote

r = sr.Recognizer()
translator = GoogleTranslator()

app = FastAPI()


def handling_url(url):
    url=unquote(url)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tmp_file.write(response.content)
            tmp_file_name = tmp_file.name

        with sr.AudioFile(tmp_file_name) as source:
            audio = r.record(source)

            try:
                txt = r.recognize_google(audio)
                print("Original Text:", txt)

                translated_text = translator.translate(txt, source='auto', target='en')
                print("Translated Text:", translated_text)

                description, quantity, price = extract_information(translated_text)

                print("Description:", description)
                print("Quantity:", quantity)
                print("Price:", price[0] if price else None)

                dict = {
                    "description" : description,
                    "quantity" : quantity,
                    "price" : price[0] if price else None   
                }

                return dict

            except sr.UnknownValueError:
                print("Error: Unable to recognize speech")
            except sr.RequestError as e:
                print("Error: Could not request results; {0}".format(e))
    else:
        print("Failed to download MP3 file")

@app.get("/voice/")
async def handling_voice_url(req: Request):
    url = req.query_params.get("url")
    data = handling_url(url)
    return data
