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
    with open("ReversedMorseDictionary.json", "r") as f:
        data = json.load(f)
        return data


def generate_string_from_code(data, input_string):
    decoded_string = ' '
    words = input_string.split('  ')
    for word in words:
        characters = word.split()
        for char in characters:
            decoded_string += data.get(char, '?')
        decoded_string += ' '

    return decoded_string.strip()


def morse_decode():
    try:
        input_str = morse_code.get()
        data = load_data()
        your_code_is.configure(text=" Decoded Morse Code is: ",text_color="#DAFFFB")
        string_decoded.configure(text="",text_color="#14FFEC")
        decoded_code = generate_string_from_code(data, input_str)
        string_decoded.configure(text=decoded_code, text_color="#14FFEC")

    except:
        string_decoded.configure(text="Oops Invalid Input")


title = customtkinter.CTkLabel(app, text=" Insert Morse Code here ", text_color="#14FFEC")
title.pack(padx=10, pady=10)


code = tkinter.StringVar()
morse_code = customtkinter.CTkEntry(app, width=350, height=50, textvariable=code, fg_color="#323232",text_color="#14FFEC",corner_radius=15)
morse_code.pack()


decode = customtkinter.CTkButton(app, text=" Decode ",text_color="#323232", command=morse_decode, fg_color="#14FFEC", hover_color="#0D7377", corner_radius=20)
decode.pack(padx=10, pady=10)

your_code_is = customtkinter.CTkLabel(app,text="",text_color="#DAFFFB")
your_code_is.pack()


string_decoded = customtkinter.CTkLabel(app, text="", text_color="#14FFEC")
string_decoded.pack()

app.mainloop()

