from .__basemod__ import BaseSolver

class CombinationLock(BaseSolver):
    NAME = 'Combination Lock'

    def _calculate(self):
        n = []
        n.append((int(self.eg.sndigit[-1])+self.eg.solves+self.eg.batt)%20)
        n.append((self.eg.modules+self.eg.needy+self.eg.solves)%20)
        n.append(sum(n[0:])%20)
        return n

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Rotate: {', '.join(list(map(lambda x: str(x), sol)))}")