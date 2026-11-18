import requests 
from deep_translator import MyMemoryTranslator 
def requireText():
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
        result = data["text"]
    else:
        print("something went wrong!")
    text = translator.translate(result)
    return text
if __name__ == "__main__":
    requireText()
