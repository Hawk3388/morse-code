from flask import Flask, request, jsonify

app = Flask(__name__)

def check_morse_code(s: str) -> bool:
    return set(s).issubset({'*', '-', '.', '_', ' '})

def check_letter(s: str) -> bool:
    return set(s).issubset(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "))

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

def process_morse_input(input_string):
    full_text = ""
    first = True
    code_split = input_string.split(" ")
    
    for code in code_split:
        if check_morse_code(code) and code != "":
            output = translate_morse(code)
            full_text += output
        elif code == "":
            if first:
                full_text += " "
                first = False
            else:
                first = True
        else:
            return "Invalid Morse Code"
    
    return full_text

def process_text_input(input_string):
    morse_result = ""
    letter_split = list(input_string.upper())
    
    for i, letter in enumerate(letter_split):
        if letter == " ":
            morse_result += "   "
        else:
            morse_code = translate_letter(letter)
            if morse_code == "Invalid Letter":
                return "Invalid Letter"
            morse_result += morse_code
            if i < len(letter_split) - 1 and letter_split[i + 1] != " ":
                morse_result += " "
    
    return morse_result

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Morse Code Translator</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            input { width: 100%; padding: 10px; margin: 10px 0; }
            button { padding: 10px 20px; background: #007cba; color: white; border: none; cursor: pointer; }
            #result { margin: 20px 0; padding: 10px; background: #f0f0f0; white-space: pre-wrap; font-family: monospace; }
        </style>
    </head>
    <body>
        <h1>Morse Code Translator</h1>
        <input type="text" id="input" placeholder="Enter text or morse code">
        <button onclick="doTranslate()">Translate</button>
        <div id="result"></div>
        
        <script>
        function doTranslate() {
            var input = document.getElementById('input').value;
            var resultDiv = document.getElementById('result');
            
            if (!input) {
                resultDiv.innerHTML = 'Please enter some text';
                return;
            }
            
            resultDiv.innerHTML = 'Translating...';
            
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/translate', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var data = JSON.parse(xhr.responseText);
                    resultDiv.innerHTML = data.error || data.result;
                }
            };
            
            xhr.send(JSON.stringify({input: input}));
        }
        </script>
    </body>
    </html>
    '''

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    input_text = data.get('input', '').strip()
    
    if not input_text:
        return jsonify({'error': 'Please enter some text'})
    
    if check_morse_code(input_text):
        result = process_morse_input(input_text)
        return jsonify({
            'result': result,
            'input_type': 'morse',
            'output_type': 'text'
        })
    
    elif check_letter(input_text.upper()):
        result = process_text_input(input_text)
        return jsonify({
            'result': result,
            'input_type': 'text',
            'output_type': 'morse'
        })
    
    else:
        return jsonify({'error': 'Invalid input. Please enter text or morse code.'})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3000)