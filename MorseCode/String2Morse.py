import json
import tkinter
import customtkinter

# Appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = tkinter.Tk()
app.geometry("720x480")
app.title("Morse Decoder")
app.configure(bg="#212121")


def load_data():
    with open("MorseDictionary.json", "r") as f:
        data: dict = json.load(f)
        return data


def generate_code_from_string(data, text):
    the_morse_code = ' '.join([data[char] if char in data else char for char in text])
    return the_morse_code


def morse_encode():
    try:
        input_str = morse_code.get()
        data = load_data()
        your_code_is.configure(text=" Your Morse Code is: ",text_color="#DAFFFB")
        string_encoded.configure(text="", text_color="#14FFEC")
        encoded_code = generate_code_from_string(data, input_str)
        string_encoded.configure(text=encoded_code, text_color="#14FFEC")
    except:
        string_encoded.configure(text="Oops Invalid Input")


title = customtkinter.CTkLabel(app, text=" Feed me your desired string to encode into morse code  ", text_color="#14FFEC")
title.pack(padx=10, pady=10)


code = tkinter.StringVar()
morse_code = customtkinter.CTkEntry(app, width=350, height=50, textvariable=code, fg_color="#323232", text_color="#14FFEC")
morse_code.pack()


encode = customtkinter.CTkButton(app, text=" Encode ", text_color="#323232", command=morse_encode, fg_color="#14FFEC", hover_color="#0D7377")
encode.pack(padx=10, pady=10)

your_code_is = customtkinter.CTkLabel(app,text="",text_color="#DAFFFB")
your_code_is.pack()


string_encoded = customtkinter.CTkLabel(app, text="", text_color="#14FFEC")
string_encoded.pack()

app.mainloop()
