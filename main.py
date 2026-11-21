#Texts taken from the fish-text.ru
from gui import mainGui
from require import requireText
import json
with open("userSettings.json", "r", encoding="utf-8") as file:
    loadedData = json.load(file)
    language = loadedData["language"]
text = requireText(language)
mainGui(text, language)

