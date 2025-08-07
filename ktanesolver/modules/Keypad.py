from .__basemod__ import BaseSolver

class Keypad(BaseSolver):
    NAME = 'Keypad'
    symbollist = ['Ϙ', 'Ӭ', '©', 'б', 'Ψ', 'Ѧ', 'Ѽ', '¶', 'ټ', 'ƛ', 'Ͽ', 'Ҩ', 'Ѣ', '҂', 'Ϟ', 'Җ', 'Ѭ', 'Ͼ', 'æ', '☆', 'Ԇ', 'ϗ', '¿', 'Ѯ', 'Ҋ', '★', 'Ω']
    symboltable = [
	    ['Ϙ', 'Ѧ', 'ƛ', 'Ϟ', 'Ѭ', 'ϗ', 'Ͽ'],
	    ['Ӭ', 'Ϙ', 'Ͽ', 'Ҩ', '☆', 'ϗ', '¿'],
	    ['©', 'Ѽ', 'Ҩ', 'Җ', 'Ԇ', 'ƛ', '☆'],
	    ['б', '¶', 'Ѣ', 'Ѭ', 'Җ', '¿', 'ټ'],
	    ['Ψ', 'ټ', 'Ѣ', 'Ͼ', '¶', 'Ѯ', '★'],
	    ['б', 'Ӭ', '҂', 'æ', 'Ψ', 'Ҋ', 'Ω']
    ]

    def display(self):
        self.symbols = []
        while 1:
            self.local_header()
            for a in range(7):
                for b in range(4):
                    try:
                        print(f"{str((a+1)+(7*(b))).zfill(2)}. {self.symbollist[a+(7*b)]}",end="\t\t")
                    except: break
                print()
            
            print()
            ans = input(f"Symbols (use number matching with the table above, separate with comma space): ").lower().split(', ')

            if len(ans)!=4: continue
            elif not all([a.isdigit() for a in ans]): continue
            elif not all([int(a)-1 in range(27) for a in ans]): continue
            elif len(set([int(a)-1 for a in ans]))!=4: continue
            else:
                self.symbols = [self.symbollist[int(a)-1] for a in ans]
                break
    
    def _calculate(self):
        s = self.symboltable
        for a in s:
            if all([b in a for b in self.symbols]): return [x for x in a if x in self.symbols]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        for a in range(7):
            for b in range(4):
                try:
                    print(f"{str((a+1)+(7*(b))).zfill(2)}. {self.symbollist[a+(7*b)]}",end="\t\t")
                except: break
            print()
        print()
        print(f"Symbols: {', '.join(self.symbols)}")
        print(f"{self.answer_pretext}Press in the order of: {', '.join(sol)}")