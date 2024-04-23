import json


def load_data():
    with open("MorseDictionary.json", "r") as f:
        data: dict = json.load(f)
        return data


def generate_morse_code_from_string(data, text):
    morse_code = ' '.join([data[char] if char in data else char for char in text])
    return morse_code


def main():
    data = load_data()
    input_string = input("Enter your desires to convert into MorseCode: ").lower()
    code = generate_morse_code_from_string(data, input_string)
    print(code)


if __name__ == "__main__":
    main()
