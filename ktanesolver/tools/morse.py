morsedict = {
    ".-": 'a',
    "-...": 'b',
    "-.-.": 'c',
    "-..": 'd',
    ".": 'e',
    "..-.": 'f',
    "--.": 'g',
    "....": 'h',
    "..": 'i',
    ".---": 'j',
    "-.-": 'k',
    ".-..": 'l',
    "--": 'm',
    "-.": 'n',
    "---": 'o',
    ".--.": 'p',
    "--.-": 'q',
    ".-.": 'r',
    "...": 's',
    "-": 't',
    "..-": 'u',
    "...-": 'v',
    ".--": 'w',
    "-..-": 'x',
    "-.--": 'y',
    "--..": 'z',
    "-----": '0',
    ".----": '1',
    "..---": '2',
    "...--": '3',
    "....-": '4',
    ".....": '5',
    "-....": '6',
    "--...": '7',
    "---..": '8',
    "----.": '9'
}

def translate(m):
    if isinstance(m, str):
        t = morsedict.get(m)
        if t == None: return -1
    elif isinstance(m, list):
        t = []
        for a in range(len(m)):
            t.append(morsedict.get(m[a]))
        if None in t: return -1
    return t

def reverseTranslate(m):
    __reversemorsedict = {b:a for a,b in morsedict.items()}
    if isinstance(m, str):
        t = __reversemorsedict.get(m.lower())
        if t == None: return -1
    elif isinstance(m, list):
        t = []
        for a in range(len(m)):
            t.append(__reversemorsedict.get(m[a].lower()))
        if None in t: return -1
    return t