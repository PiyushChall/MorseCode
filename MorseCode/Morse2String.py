import json


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


def main():
    data = load_data()
    input_string = input("Enter your MorseCode: ")
    value = generate_string_from_code(data, input_string)
    print(value)


if __name__ == "__main__":
    main()
