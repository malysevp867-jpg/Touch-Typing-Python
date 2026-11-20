#Texts taken from the fish-text.ru
from gui import mainGui
from require import requireText
language = "en"
text = requireText(language)
mainGui(text, language)

