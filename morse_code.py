# Python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

# Function to encrypt the string according to the morse code chart
def text_to_morse(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' '
    return cipher

# Function to decrypt the string from morse to english
def morse_to_text(morse):
    morse += ' '  # Extra space added at the end to access the last morse code
    decipher = ''
    citext = ''
    for letter in morse:
        if (letter != ' '):
            i = 0
            citext += letter  # Storing morse code of a single character
        else:
            i += 1
            if i == 2:
                decipher += ' '  # Adding space to separate words
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def main():
    print("Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    choice = input("Choose your option (1/2): ")
    if choice == '1':
        text = input("Enter text to convert to Morse Code: ")
        result = text_to_morse(text)
        print("Morse Code: " + result)
    elif choice == '2':
        morse = input("Enter Morse Code to convert to text: ")
        result = morse_to_text(morse)
        print("Text: " + result)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()