from .__basemod__ import BaseSolver

class AMistake(BaseSolver):
    NAME = 'A Mistake'

    def display(self):
        pass
    
    def _calculate(self):
        pass

    def solve(self):
        ans = self._calculate()
        self.local_header()
        print(f"1st Tap - Any\n2nd Tap - when the last second digit is {self.eg.sndigit[-1]}\n3rd Tap - when the seconds are {str(sum(int(a) for a in self.eg.sndigit))}")