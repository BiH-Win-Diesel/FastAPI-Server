import speech_recognition as sr
import re
from deep_translator import GoogleTranslator

def extract_information(text):
    description_pattern = re.compile(r'([a-zA-Z]+)\s*')
    quantity_pattern = re.compile(r'(\d+)\s*(?:unit|units|packet|pack)\s*')
    price_pattern = re.compile(r'(\d+(\.\d{1,2})?)')

    description_match = description_pattern.search(text)
    quantity_match = quantity_pattern.search(text)
    price_matches = price_pattern.findall(text)

    description = description_match.group() if description_match else None
    quantity = quantity_match.group(1) if quantity_match else None
    price = price_matches[-1] if price_matches else None

    return description, quantity, price

r = sr.Recognizer()
translator = GoogleTranslator()

# with sr.Microphone() as source:
#     print("Speak:")
#     audio = r.listen(source)
#     try:
#         txt = r.recognize_google(audio)
#         print("Original Text:", txt)

#         translated_text = GoogleTranslator(source='auto', target='en').translate(txt)
#         print("Translated Text:", translated_text)

#         description, quantity, price = extract_information(translated_text)

#         print("Description:", description)
#         print("Quantity:", quantity)
#         print("Price:", price[0])

#     except sr.UnknownValueError:
#         print("Error: Unable to recognize speech")
#     except sr.RequestError as e:
#         print("Error: Could not request results; {0}".format(e))


# def recognise_speech():
#     with sr.AudioFile("./captured_voice.mp3") as source:
#         audio = r.listen(source)
#         try:
#             txt = r.recognize_google(audio)
#             print("Original Text:", txt)
#         except sr.UnknownValueError:
#             print("Error: Unable to recognize speech")
#         except sr.RequestError as e:
#             print("Error: Could not request results; {0}".format(e))



# recognise_speech();