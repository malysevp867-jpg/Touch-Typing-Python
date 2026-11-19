import customtkinter as ctk
import pyglet
from pathlib import Path

def mainGui(text,):
    chars = list(text)
    mainFile = Path(__file__).resolve().parent
    fontFile = mainFile / "fonts" / "RubikGlitch-Regular.ttf"
    pyglet.font.add_file(str(fontFile))
    app = ctk.CTk()
    app.title("Touch Typing")
    app.geometry('1200x700')
    app.configure(fg_color="#000d21")
    customFont = ctk.CTkFont(family="Poppins",size=20)
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
    app.mainloop()
if __name__ == "__main__":
    mainGui(text)