# Function to convert text to Morse code
def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        else:
            morse_code += ' '
    
    return morse_code

# Read text from file
with open("predicted_labels.txt", "r") as file:
    text = file.read()

# Convert text to Morse code
morse_code = text_to_morse(text)

# Write Morse code to another file
with open("morse_code_output.txt", "w") as file:
    file.write(morse_code)
