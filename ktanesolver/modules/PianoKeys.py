from .__basemod__ import BaseSolver

class PianoKeys(BaseSolver):
    NAME = 'Piano Keys'
    symbollist = '𝄬𝄴𝄰𝄯𝄐𝄵𝆗𝄡~'
    symboltable = {
        '𝄬': 'flat',
        '𝄴': 'common time', '𝄰': 'sharp',
        '𝄯': 'natural', '𝄐': 'fermata',
        '𝄵': 'cut time', '𝆗': 'turn',
        '𝄡': 'clef', '~': 'mordent'
    }

    def display(self):
        while 1:
            self.local_header()
            for a in range(5):
                for b in range(2):
                    try:
                        print(f"{str((a+1)+(5*(b))).zfill(2)}. {self.symbollist[a+(5*b)]}",end="\t\t")
                    except:
                        continue
                print()
            print()
            ans = input(f"Symbols (use number matching with the table above, separate with comma space): ").lower().split(', ')

            if len(ans)!=3: continue
            elif not all(a.isdigit() for a in ans): continue
            elif not all(int(a)-1 in range(9) for a in ans): continue
            elif len(set([int(a)-1 for a in ans]))!=3: continue
            else:
                self.symbols = [self.symbollist[int(a)-1] for a in ans]
                self.symbolsdict = [self.symboltable[self.symbollist[int(a)-1]] for a in ans]
                break
    
    def _calculate(self):
        if 'flat' in self.symbolsdict and int(self.eg.sndigit[-1])%2 == 0: return ['A#','A#','A#','A#','F#','G#','A#','G#','A#']
        elif ('common time' in self.symbolsdict or 'sharp' in self.symbolsdict) and self.eg.hold >= 2: return ['D#','D#','D','D','D#','D#','D','D#','D#','D','D','D#']
        elif ('natural' in self.symbolsdict and 'fermata' in self.symbolsdict): return ['E','F#','F#','F#','F#','E','E','E']
        elif ('cut time' in self.symbolsdict or 'turn' in self.symbolsdict) and any('STEREO RCA' in a for a in self.eg.uniqueports): return ['A#','A','A#','F','D#','A#','A','A#','F','D#']
        elif ('clef' in self.symbolsdict) and any('SND*'in a for a in self.eg.litind): return ['E','E','E','C','E','G','G']
        elif ('mordent' in self.symbolsdict or 'fermata' in self.symbolsdict or 'common time' in self.symbolsdict) and self.eg.batt >= 3: return ['C#','D','E','F','C#','D','E','F','A#','A']
        elif ('flat' in self.symbolsdict and 'sharp' in self.symbolsdict): return ['G','G','C','G','G','C','G','C']
        elif ('cut time' in self.symbolsdict or 'mordent' in self.symbolsdict) and any(numb in self.eg.sndigit for numb in ['3', '7', '8']): return ['A','E','F','G','F','E','D','D','F','A']
        elif ('flat' in self.symbolsdict or 'turn' in self.symbolsdict or 'clef' in self.symbolsdict): return ['G','G','G','D#','A#','G','D#','A#','G']
        else: return ['B','D','A','G','A','B','D','A']

    def solve(self):
        sol = self._calculate()
        
        self.local_header()
        for a in range(5):
            for b in range(2):
                try:
                    print(f"{str((a+1)+(5*(b))).zfill(2)}. {self.symbollist[a+(5*b)]}",end="\t\t")
                except:
                    continue
            print()
        print()
        print(f"Symbols: {', '.join([a.capitalize() for a in self.symbols])}")
        print(f"{self.answer_pretext}Music: {', '.join(sol)}")