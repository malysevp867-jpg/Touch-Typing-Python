from pathlib import Path
import customtkinter as ctk
import pyglet
from require import requireText
import json
import time

def mainGui(text=None, language="en"):
    if text is None:
        text = requireText(language)
    mainFile = Path(__file__).resolve().parent
    fontFile = mainFile / "fonts" / "RubikGlitch-Regular.ttf"
    pyglet.font.add_file(str(fontFile))
    app = ctk.CTk()
    app.title("Touch Typing")
    app.geometry("1200x700")
    app.configure(fg_color="#000d21")
    customFont = ctk.CTkFont(family="Poppins", size=32)
    app.resizable(False, False)

    # Creat a text box
    textBox = ctk.CTkTextbox(
        app,
        width=900,
        height=400,
        fg_color="#00183c",
        activate_scrollbars=False,
        font=customFont,
        wrap="word",
        padx=30,
        pady=30,
    )
    textBox.tag_config("center", justify="center")
    textBox.insert("1.0", text, "center")
    textBox.configure(state="disabled")
    textBox.pack(pady=30)
    textBox.tag_config("correct", foreground="#00ff4c")
    textBox.tag_config("wrong", foreground="#ff0000")


    # Module to check keys
    numberOfLetter = 0
    numberOfErrors = 0
    chars = list(text)
    startTime = None

    timeTypingLabel = ctk.CTkLabel(app, text="", font=customFont)
    timeTypingLabel.pack(padx=10)
    def timeLabel(timeOfTyping):
        if language == "en":
            labelText= f"Time of typing: {timeOfTyping}"
        elif language == "ru":
            labelText = f"Время печатанья: {timeOfTyping}" 
        timeTypingLabel.configure(text=labelText)
        

    def checkKey(event):
        nonlocal numberOfLetter, numberOfErrors, startTime
        if not event.char:
            return
        if startTime is None:      
            startTime = time.time()
        if len(chars) > 0:
            letterNow = chars[0]
            userPressed = event.char
            startPpos = f"1.0 + {numberOfLetter}c"
            endPos = f"1.0 + {numberOfLetter + 1}c"
            if letterNow == userPressed:
                textBox.tag_remove("wrong", startPpos, endPos)
                textBox.tag_add("correct", startPpos, endPos)
                numberOfLetter += 1
                print("Correct!")
                chars.pop(0)
            else:
                textBox.tag_add("wrong", startPpos, endPos)
                print("Wrong!")
                numberOfErrors += 1
        if len(chars) == 0:
            timeOfTyping = round(time.time() - startTime, 1)
            timeLabel(timeOfTyping)
            print(timeOfTyping)
            precentOfErrors()
            loadNewText(language)

    app.bind("<Key>", checkKey)

    def loadNewText(language):
        nonlocal text, chars, numberOfLetter, numberOfErrors, startTime
        text = requireText(language)
        chars = list(text)
        numberOfLetter = 0
        numberOfErrors = 0
        startTime = None
        textBox.configure(state="normal")
        textBox.delete("1.0", "end")
        textBox.insert("1.0", text, "center")
        textBox.configure(state="disabled")

    def switchLanguage():
        nonlocal language
        with open("userSettings.json", "r", encoding="utf-8") as file:
            loadedData = json.load(file)
            language = loadedData["language"]
        if language == "en":
            loadedData["language"] = "ru"
            with open("userSettings.json", "w", encoding="utf-8") as file:
                json.dump(loadedData,file, ensure_ascii=False, indent=4)
            language = "ru"
            loadNewText(language)
            switch.configure(text="Язык: Русский")
        elif language == "ru":
            loadedData["language"] = "en"
            with open("userSettings.json", "w", encoding="utf-8") as file:
                json.dump(loadedData,file, ensure_ascii=False, indent=4)
            language = "en"
            loadNewText(language)
            switch.configure(text="Language: English")
        else:
            print("Something went wrong!")


    precentLabel = ctk.CTkLabel(app, text="", font=customFont)
    precentLabel.pack(padx=30)
    def precentOfErrors():
        totalChars = len(text)
        precent = round((numberOfErrors / totalChars) * 100, 1)
        if language == "en":
            precentLabel.configure(text=f"Percent of errors: {precent}%")
        elif language == "ru":
            precentLabel.configure(text=f"Процент ошибок: {precent}%")
        else:
            print("Something went wrong!")

    if language == "en":
        switchText = "Language: English"
    elif language == "ru":
        switchText = "Язык: Русский"
    else:
        print("Something went wrong!")
    switchVar = ctk.StringVar(value="off")
    switch = ctk.CTkSwitch(
        app,
        text=switchText,
        command=switchLanguage,
        variable=switchVar,
        onvalue="on",
        offvalue="off",
    )
    switch.pack(padx=10)

    app.mainloop()
if __name__ == "__main__":
    mainGui()
