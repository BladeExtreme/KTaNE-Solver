from .__basemod__ import BaseSolver

class Listening(BaseSolver):
    NAME = 'Listening'
    bank = {
        'taxi dispatch':        '&&&**',
        'cow':                  '&$#$&',
        'extractor fan':        '#$#*&',
        'train station':        '#$$**',
        'arcade':               '$#$#*',
        'casino':               '**$*#',
        'supermarket':          '#$$&*',
        'soccer match':         '##*$*',
        'tawny owl':            '$#*$&',
        'sewing machine':       '#&&*#',
        'thrush nightingale':   '**#**',
        'car engine':           '&#**&',
        'reloading glock 19':   '$&**#',
        'oboe':                 '&#$$#',
        'saxophone':            '$&&**',
        'tuba':                 '#&$##',
        'marimba':              '&*$*$',
        'phone ringing':        '&$$&*',
        'tibetan nuns':         '#&&&&',
        'throat singing':       '**$$$',
        'beach':                '*&*&&',
        'dial-up internet':     '*#&*&',
        'police radio scanner': '**###',
        'censorship bleep':     '&&$&*',
        'medieval weapons':     '&$**&',
        'door closing':         '#$#&$',
        'chainsaw':             '&#&&#',
        'compressed air':       '$$*$*',
        'servo motor':          '$&#$$',
        'waterfall':            '&**$$',
        'tearing fabric':       '$&&*&',
        'zipper':               '&$&##',
        'vacuum cleaner':       '#&$*&',
        'ballpoint pen writing':'$*$**',
        'rattling iron chain':  '*#$&&',
        'book page turning':    '###&$',
        'table tennis':         '*$$&$',
        'squeaky toy':          '$*&##',
        'helicopter':           '#&$&&',
        'firework exploding':   '$&$$*',
        'glass shattering':     '*$*$*'
    }

    def display(self):
        while 1:
            submit = False; play = False
            self.local_header()
            for y in range(11):
                for x in range(4):
                    try:
                        text = f"{str((y+1)+(x*11)).zfill(2)}. {list(self.bank.keys())[(y+1)+(x*11)]}"
                        print(text, end=" "*(30-len(text)))
                    except: pass
                print()
            print()
            print(f"Enter Command:\n - Input 'Submit #' with # substituted with a number from the options above to submit the audio\n - Input 'Play #' with # substituted with a number from the options above to play an audio using pygame.")
            ans = input(f"cmd/Listening > ").lower().split(' ')

            if len(ans)!=2: continue
            elif ans[0] not in ['submit', 'play']: continue
            elif not ans[1].isdigit(): continue
            elif int(ans[1]) not in range(1, len(self.bank)+1): continue
            else:
                if ans[0]=='submit':
                    self.answer = list(self.bank.keys())[int(ans[1])]
                    break
                else:
                    self.playAudio()
        
    def _calculate(self):
        return self.bank[self.answer]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        for y in range(11):
            for x in range(4):
                try:
                    text = f"{str((y+1)+(x*11)).zfill(2)}. {list(self.bank.keys())[(y+1)+(x*11)]}"
                    print(text, end=" "*(30-len(text)))
                except: pass
            print()
        print()
        print(f"Enter Command:\n - Input 'Submit #' with # substituted with a number from the options above to submit the audio\n - Input 'Play #' with # substituted with a number from the options above to play an audio using pygame.")
        print(f"cmd/Listening > submit {str(list(self.bank.keys()).index(self.answer))}")
        print(f"{self.answer_pretext}{sol}")
    
    def playAudio(self):
        pass