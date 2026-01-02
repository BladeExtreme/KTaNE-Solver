from .__basemod__ import BaseSolver

class TWords(BaseSolver):
    NAME = 'T-Words'
    table = [
        ['tautochronous', 'tatterdemalion', 'tauromorphous', 'tellurometer', 'tachygraphy'],
        ['tarantella', 'taphephobia', 'tellurian', 'tachyphrasia', 'tablature'],
        ['tenderometer', 'tachyphrasia', 'taphephobia', 'tabernacular', 'tamandua'],
        ['tellurometer', 'teichoscopy', 'tenderometer', 'tautochronous', 'taphrogenesis'],
        ['tectosphere', 'tenderometer', 'teichoscopy', 'tachygraphy', 'tangoreceptor'],
        ['tessaraglot', 'tautochronous', 'tangoreceptor', 'tellurian', 'taphephobia'],
        ['tamandua', 'taphrogenesis', 'tellurometer', 'tablature', 'tectosphere'],
        ['tabernacular', 'tabernacle', 'tamandua', 'tessaraglot', 'tauromorphous'],
        ['tachygraphy', 'tangoreceptor', 'tachygraphy', 'terpsichorean', 'tessaraglot'],
        ['tangoreceptor', 'tellurian', 'tablature', 'tatterdemalion', 'tachyphrasia'],
        ['tatterdemalion', 'terpsichorean', 'taphrogenesis', 'tamandua', 'tellurometer'],
        ['teichoscopy', 'tellurometer', 'tachyphrasia', 'tenderometer', 'tautochronous'],
        ['terpsichorean', 'tectosphere', 'tatterdemalion', 'tauromorphous', 'tenderometer'],
        ['tellurian', 'tauromorphous', 'tabernacle', 'teichoscopy', 'tarantella'],
        ['taphephobia', 'tablature', 'tectosphere', 'taphrogenesis', 'tabernacle'],
        ['tabernacle', 'tamandua', 'tessaraglot', 'tarantella', 'teichoscopy'],
        ['tachyphrasia', 'tabernacular', 'tarantella', 'tabernacle', 'tatterdemalion'],
        ['tauromorphous', 'tarantella', 'tabernacular', 'tectosphere', 'terpsichorean'],
        ['taphrogenesis', 'tachygraphy', 'terpsichorean', 'taphephobia', 'tellurian'],
        ['tablature', 'tessaraglot', 'tautochronous', 'tangoreceptor', 'tabernacular']
    ]
        
    def display(self):
        words = []
        while True:
            self.local_header()
            print(f"Guide:\n - Each row represent one word on the module, from top to bottom.\n")
            for a in words:
                print(f" > {a.capitalize()}")
            ans = input(f" > ").lower()

            if ans in words: continue
            elif all(ans not in a for a in self.table): continue
            else:
                words.append(ans)
                if len(words)==4:
                    self.words = words
                    break
        
        while True:
            self.local_header()
            print(f"Guide:\n - Each row represent one word on the module, from top to bottom.\n")
            for a in words:
                print(f" > {a.capitalize()}")
            ans = input(f"LED Color: ").lower()

            if not ans.isalpha(): continue
            else:
                self.color = ans
                break

    def _calculate(self):
        col = 0 if self.eg.batt>4 and self.color!='red' else 1 if any(a in ['BOB','FRK','CAR*','IND*'] for a in self.eg.ind) and self.color!='green' else 2 if 'SERIAL' in self.eg.uniqueports and 'DVI-D' in self.eg.uniqueports and self.color!='blue' else 3 if self.color!='orange' and all(a not in 'AIUEO' for a in self.eg.snletter) else 4
        rot_table = self.table.copy()
        for a in range(3):
            rot_table = list(zip(*reversed(rot_table)))
        
        order = {item: i for i, item in enumerate(rot_table[col])}
        return sorted(self.words, key=lambda x: order[x])

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Guide:\n - Each row represent one word on the module, from top to bottom.\n")
        for a in self.words:
            print(f" > {a.capitalize()}")
        print(f"LED Color: {self.color.capitalize()}\n")
        print(f"{self.answer_pretext}{', '.join(a.capitalize() for a in sol)}")