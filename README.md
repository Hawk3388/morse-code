# Morse-Code

A Python program to convert text to Morse code and vice versa, including audio playback.

## Features

- Translates letters and numbers to Morse code
- Translates Morse code back to letters/numbers
- Speech output of the translated text
- Audio playback of Morse code
- Supports different Morse code symbols: `*`, `.`, `-`, `_`
- Stop the program by typing `quit`

## Requirements

- Python 3.x
- Dependencies:
  - `pyttsx3`
  - `pydub`
  - `simpleaudio`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Start the program with:

```bash
python main.py
```

Enter either a letter/text or Morse code. The program will automatically detect your input and output the translation.

## Notes

- For audio playback, a working audio output is required.
- Supports both uppercase and lowercase letters.

## License

This project is licensed under the MIT License.
