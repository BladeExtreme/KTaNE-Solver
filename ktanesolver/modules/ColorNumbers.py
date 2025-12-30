from .__basemod__ import BaseSolver

class ColorNumbers(BaseSolver):
    NAME = 'Color Numbers'

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Light Color [Red, Blue, Yellow, Green]: ").lower()

            if ans not in ['red','blue','yellow','green']: continue
            else:
                self.light = ans
                break

    def _calculate(self):
        match self.light:
            case 'red': return 1
            case 'blue': return 2
            case 'yellow': return 3
            case 'green': return 4

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Press {sol}")