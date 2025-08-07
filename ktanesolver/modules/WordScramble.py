from .__basemod__ import BaseSolver

class WordScramble(BaseSolver):
    NAME = 'Word Scramble'
    wordlist = ['banana', 'attack', 'damage', 'napalm', 'ottawa', 'kaboom', 'blasts',
              'charge', 'archer', 'casing', 'cannon', 'keypad', 'disarm', 'flames',
              'kevlar', 'weapon', 'sapper', 'mortar', 'button', 'robots', 'bursts',
              'device', 'rocket', 'defuse', 'widget', 'module', 'letter', 'semtex',
              'person', 'wiring']

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Letters (Seperated with Comma Space): ").lower().split(', ')

            if len(ans)!=6: continue
            elif not all(a.isalpha() for a in ans): continue
            elif sorted(set(ans)) not in [sorted(set(a)) for a in self.wordlist]: continue
            else:
                self.letter = ans
                break
    
    def _calculate(self):
        sol = list(map(lambda a: sorted(set(a)), self.wordlist)).index(sorted(set(self.letter)))
        return self.wordlist[sol].upper()

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Letters: {', '.join(self.letter)}")
        print(f"{self.answer_pretext}Word: {sol}")