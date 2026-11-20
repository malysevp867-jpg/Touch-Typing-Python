import customtkinter as ctk
import pyglet
from pathlib import Path

def mainGui(text, language):
    mainFile = Path(__file__).resolve().parent
    fontFile = mainFile / "fonts" / "RubikGlitch-Regular.ttf"
    pyglet.font.add_file(str(fontFile))
    app = ctk.CTk()
    app.title("Touch Typing")
    app.geometry('1200x700')
    app.configure(fg_color="#000d21")
    customFont = ctk.CTkFont(family="Poppins",size=20)
    app.resizable(False, False)

    textBox = ctk.CTkTextbox(
        app,
        width=700,
        height=200,
        fg_color="#00183c",
        activate_scrollbars=False,
        font=customFont,
        wrap="word",        
        padx=30,           
        pady=30,   
    )
    textBox.tag_config("center", justify="center")
    textBox.insert("1.0",text,"center")
    textBox.configure(state="disabled")
    textBox.pack(pady=30)
    textBox.tag_config("correct", foreground = "#00ff4c")
    textBox.tag_config("wrong", foreground = "#ff0000")

    numberOfLetter = 0
    chars = list(text)
    def checkKey(event):
        nonlocal numberOfLetter
        if not event.char:
            return
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
    app.bind("<Key>", checkKey)

    switchText = "Language: "
    def switchToggle():
        nonlocal language
        if language == "en":
            language = "ru"
            switch.configure(text="Язык: Русский") 
        elif language == "ru":
            switch.configure(text="Language: English") 
            language = "en"
        else:
            print("Something went wrong!")
    switchVar = ctk.StringVar(value="off")
    switch = ctk.CTkSwitch(
        app,
        text=switchText,
        command=switchToggle, 
        variable=switchVar, 
        onvalue="on", 
        offvalue="off")
    switch.pack(padx=10)

    app.mainloop()
if __name__ == "__main__":
    mainGui()