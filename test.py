import requests 
import time
from deep_translator import MyMemoryTranslator 
from pynput import keyboard

translator = MyMemoryTranslator (source="ru-RU",target="en-GB")
url = "https://fish-text.ru/get"
params = {
    "type": "sentence",
    "number": 1,
    "format": "json"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    text = data["text"]
else:
    print("something went wrong!")

result = translator.translate(text)
print(result)
#print(text)

chars = list(result)
deleted_chars = {',',"'"}
chars = [c for c in chars if c not in deleted_chars]
print(chars)
"""
def on_press(key):
    print(f'You pressed: {key.char}')
def on_release(key):
    print(f'You pressed: {key}')
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
"""