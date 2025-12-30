from .__basemod__ import BaseSolver

class Alphabet(BaseSolver):
    NAME = 'Alphabet'
    wordbank = ['JQXZ','QEW','AC','ZNY','TJL','OKBV','DFW','YKQ','LXE','GS','VSI','PQJS','VCN','JR','IRNM','OP','QYDX','HDU','PKD','ARGF']

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Letters: ").lower().split(', ')

            if len(ans)!=4: continue
            elif not all(a.isalpha() for a in ans): continue
            elif len(set(ans))!=4: continue
            else:
                self.letters = ans
                break

    def _calculate(self):
        ans = []
        for a in self.wordbank:
            if set([b for b in a])==set([b for b in a if b in self.letters]):
                ans = [b for b in a]
                break
        if len(ans)!=4:
            for a in sorted(self.letters):
                if a not in ans: ans.append(a)
        return ans

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}{', '.join(sol)}")