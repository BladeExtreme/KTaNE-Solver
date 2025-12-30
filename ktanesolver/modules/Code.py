from .__basemod__ import BaseSolver

class Code(BaseSolver):
    NAME = 'The Code'

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Display Code: ")

            if not ans.isdigit(): continue
            elif len(ans)!=4: continue
            else:
                self.code = ans
                break

    def _calculate(self):
        if self.eg.sndigit[0]==self.eg.sndigit[-1] and self.eg.batt==0: return self.code
        elif any(a in self.eg.ind for a in ['CLR','CLR*']): return self.code//8
        elif any(a in self.eg.snletter for a in 'XYZ'): return self.code//20
        elif len(a for b in self.eg.ports for a in b)>=5: return self.code//30
        elif self.eg.batt==0: return self.code//42
        elif len(self.eg.litind)>len(self.eg.unlitind): return self.code//69
        else:
            return self.code//3

    def solve(self):
        sol = self._calculate()
        print(f"{self.answer_pretext}{sol}")