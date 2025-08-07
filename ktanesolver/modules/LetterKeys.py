from .__basemod__ import BaseSolver

class LetterKeys(BaseSolver):
    NAME = 'Letter Keys'

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Number: ").lower()

            if not ans.isdigit(): continue
            if int(ans) not in range(100): continue
            else:
                self.number = int(ans)
                break
    
    def _calculate(self):
        if self.number==69: return 'D'
        elif self.number%6==0: return 'A'
        elif self.eg.batt>=2 and self.number%3==0: return 'B'
        elif any(a in 'CE3' for a in self.eg.sn) and self.number in range(22, 80): return 'B'
        elif any(a in 'CE3' for a in self.eg.sn): return 'C'
        elif self.number<46: return 'D'
        else: return 'A'

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Number: {str(self.number)}")
        print(f"{self.answer_pretext}Letter: {sol}")