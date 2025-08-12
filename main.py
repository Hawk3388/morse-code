import pyttsx3
import simpleaudio as sa
from pydub import AudioSegment
from pydub.generators import Sine

def check_morse_code(s: str) -> bool:
    return set(s).issubset({'*', '-', '.', '_', ' '})

def check_letter(s: str) -> bool:
    return set(s).issubset(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "))

def say_text(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def create_morse_audio(morse: list[str]) -> None:
    audio = AudioSegment.silent(duration=100)
    silence = AudioSegment.silent(duration=100)
    short_beep = Sine(440).to_audio_segment(duration=100)
    long_beep = Sine(440).to_audio_segment(duration=300)

    for code in morse:
        for char in code:
            if char == '*':
                audio += short_beep + silence
            elif char == '-':
                audio += long_beep + silence
            elif char == '.':
                audio += short_beep + silence
            elif char == '_':
                audio += long_beep + silence
            elif char == ' ':
                audio += AudioSegment.silent(duration=300)

    raw_audio = audio.raw_data
    sample_rate = audio.frame_rate
    num_channels = audio.channels
    sample_width = audio.sample_width

    play_obj = sa.play_buffer(raw_audio, num_channels, sample_width, sample_rate)
    play_obj.wait_done()

def translate_morse(morse: str) -> str:
    code_len = len(morse)
    if morse[0] in ('*', '.'):
        if code_len == 1:
            return "E"
        elif morse[1] in ('*', '.'):
            if code_len == 2:
                return "I"
            elif morse[2] in ('*', '.'):
                if code_len == 3:
                    return "S"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "H"
                    elif morse[4] in ('*', '.'):
                        if code_len == 5:
                            return "5"
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "4"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        return "V"
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "3"
            elif morse[2] in ('-', '_'):
                if code_len == 3:
                    return "U"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "F"
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "4"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        pass
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "2"
        elif morse[1] in ('-', '_'):
            if code_len == 2:
                return "A"
            elif morse[2] in ('-', '_'):
                if code_len == 3:
                    return "W"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        return "J"
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "1"     
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "P"          
            elif morse[2] in ('*', '.'):
                if code_len == 3:
                    return "R"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "L"
    elif morse[0] in ('-', '_'):
        if code_len == 1:
            return "T"
        elif morse[1] in ('-', '_'):
            if code_len == 2:
                return "M"
            elif morse[2] in ('-', '_'):
                if code_len == 3:
                    return "O"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        pass
                    elif morse[4] in ('-', '_'):
                        if code_len == 5:
                            return "0"   
                    elif morse[4] in ('*', '.'):
                        if code_len == 5:
                            return "9"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        pass
                    elif morse[4] in ('*', '.'):
                        if code_len == 5:
                            return "8"
            elif morse[2] in ('*', '.'):
                if code_len == 3:
                    return "G"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        return "Q"
                
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "Z"
                    elif morse[4] in ('*', '.'):
                        if code_len == 5:
                            return "7"          
        elif morse[1] in ('*', '.'):
            if code_len == 2:
                return "N"
            elif morse[2] in ('*', '.'):
                if code_len == 3:
                    return "D"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "B"
                    elif morse[4] in ('*', '.'):
                        if code_len == 5:
                            return "6"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        return "X"            
            elif morse[2] in ('-', '_'):
                if code_len == 3:
                    return "K"
                elif morse[3] in ('-', '_'):
                    if code_len == 4:
                        return "Y"
                elif morse[3] in ('*', '.'):
                    if code_len == 4:
                        return "C"
                    
    return "Invalid Morse Code"
                    
def translate_letter(letter: str) -> str:
    morse_dict = {
        'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*',
        'F': '**-*', 'G': '--*', 'H': '****', 'I': '**', 'J': '*---',
        'K': '-*-', 'L': '*-**', 'M': '--', 'N': '-*', 'O': '---',
        'P': '*--*', 'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-',
        'U': '**-', 'V': '**-*', 'W': '*--', 'X': '-**-', 'Y': '-*--',
        'Z': '--**',
        '0': '-----', '1': '*----', '2': '**---', '3': "***--", 
        '4': "****-",  '5': "*****",  '6': "-****",  '7': "--***", 
        '8': "---**",  '9': "----*"
    }
    return morse_dict.get(letter, "Invalid Letter")

def main():
    while True:
        first = True
        input_string = input("Enter letters or morse code: ")
        if input_string.lower() == "quit":
            break
        elif check_morse_code(input_string):
            full_text = ""
            code_split = input_string.split(" ")
            for code in code_split:
                if check_morse_code(code) and code != "":
                    output = translate_morse(code)
                    print(output, end="")
                    full_text += output
                elif code == "":
                    if first:
                        print(" ", end="")
                        first = False
                        full_text += " "
                    else:
                        first = True
                else:
                    print("Invalid Morse Code")
            print("")
            say_text(full_text)
        
        elif check_letter(input_string.upper()):
            morse = []
            letter_split = list(input_string.upper())
            for letter in letter_split:
                if letter == " ":
                    print("   ", end="")
                    morse.append("   ")
                else:
                    morse_code = translate_letter(letter)
                    print(morse_code, end=" ")
                    morse.append(morse_code + " ")
            print("")
            create_morse_audio(morse)
        
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()