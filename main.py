def check_morse_code(s: str) -> bool:
    return set(s).issubset({'*', '-', '.', '_', ' '})

def translate_morse(morse: str) -> str:
    code_len = len(morse)
    if morse[0] == ('*' or '.'):
        if code_len == 1:
            return "E"
        elif morse[1] == ('*' or '.'):
            if code_len == 2:
                return "I"
            elif morse[2] == ('*' or '.'):
                if code_len == 3:
                    return "S"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "H"
                    elif morse[4] == ('*' or '.'):
                        if code_len == 5:
                            return "5"
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "4"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        return "V"
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "3"
            elif morse[2] == ('-' or '_'):
                if code_len == 3:
                    return "U"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "F"
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "4"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        pass
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "2"
        elif morse[1] == ('-' or '_'):
            if code_len == 2:
                return "A"
            elif morse[2] == ('-' or '_'):
                if code_len == 3:
                    return "W"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        return "J"
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "1"     
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "P"          
            elif morse[2] == ('*' or '.'):
                if code_len == 3:
                    return "R"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "L"
    elif morse[0] == ('-' or '_'):
        if code_len == 1:
            return "T"
        elif morse[1] == ('-' or '_'):
            if code_len == 2:
                return "M"
            elif morse[2] == ('-' or '_'):
                if code_len == 3:
                    return "O"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        pass
                    elif morse[4] == ('-' or '_'):
                        if code_len == 5:
                            return "0"   
                    elif morse[4] == ('*' or '.'):
                        if code_len == 5:
                            return "9"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        pass
                    elif morse[4] == ('*' or '.'):
                        if code_len == 5:
                            return "8"
            elif morse[2] == ('*' or '.'):
                if code_len == 3:
                    return "G"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        return "Q"
                
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "Z"
                    elif morse[4] == ('*' or '.'):
                        if code_len == 5:
                            return "7"          
        elif morse[1] == ('*' or '.'):
            if code_len == 2:
                return "N"
            elif morse[2] == ('*' or '.'):
                if code_len == 3:
                    return "D"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "B"
                    elif morse[4] == ('*' or '.'):
                        if code_len == 5:
                            return "6"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        return "X"            
            elif morse[2] == ('-' or '_'):
                if code_len == 3:
                    return "K"
                elif morse[3] == ('-' or '_'):
                    if code_len == 4:
                        return "Y"
                elif morse[3] == ('*' or '.'):
                    if code_len == 4:
                        return "C"
                    
    return "Invalid Morse Code"
                    

def main():
    first = True
    input_string = input("Enter a letter or morse code: ")
    if check_morse_code(input_string):
        code_split = input_string.split(" ")
        for code in code_split:
            if check_morse_code(code) and code != "":
                output = translate_morse(code)
                print(output, end="")
            elif code == "":
                if first:
                    print(" ", end="")
                    first = False
                else:
                    first = True
            else:
                print("Invalid Morse Code")

if __name__ == "__main__":
    main()