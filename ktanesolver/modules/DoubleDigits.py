from .__basemod__ import BaseSolver

class DoubleDigits(BaseSolver):
    NAME = 'Double Digits'

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Screen's Digit (First number is left side, second number is right. Space differentiate between 2 numbers): ").lower().split(' ')

            if len(ans)!=2: continue
            elif any(not a.isdigit() for a in ans): continue
            elif not all(int(a) in range(0,10) for a in ans): continue
            else:
                self.numbers = [int(a) for a in ans]
                break

    def _calculate(self):
        table = [
            [8,5,8,3,4,1,1,9,8,3,5,9,9,5,5,9,3,8,9,2],
            [9,7,4,1,5,2,1,4,4,2,6,7,9,6,8,8,7,5,9,7],
            [1,8,6,1,4,6,6,8,9,4,8,1,3,1,8,1,9,1,7,2],
            [1,8,7,5,1,6,5,5,7,5,9,8,8,8,1,7,9,5,5,5],
            [9,5,3,6,4,3,7,2,7,2,9,2,5,4,6,9,2,5,7,3],
            [1,1,8,8,6,3,1,7,7,6,9,2,5,7,6,2,2,5,7,3]
        ]
        row = self.eg.batt if self.eg.batt<5 else -1
        n1 = table[row][self.numbers[0]]
        n2 = table[row][self.numbers[1]+10]

        return (n1*n2)%10

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Press when timer's second last digit is {sol}")