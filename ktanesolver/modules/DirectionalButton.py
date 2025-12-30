from .__basemod__ import BaseSolver

class DirectionalButton(BaseSolver):
    NAME = 'Directional Button'
    stage = 1; table = [
        [[1, 'Down'], [2, 'Down'], [4, 'Up']],
        [[3, 'Up'], [2, 'Down'], [3, 'Up']]
    ]

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {self.stage}")
            ans = input("Button Color [Blue, Red, White]: ").lower()
            if not ans.isalpha(): continue
            elif ans not in ['blue','red','white']: continue
            else:
                self.color = ans
                break
        
        while 1:
            self.local_header()
            print(f"STAGE {self.stage}")
            print(f"Button Color: {self.color.capitalize()}")
            ans = input("Button Label [Detonate,Abort]: ").lower()
            if not ans.isalpha(): continue
            elif ans not in ['detonate', 'abort']: continue
            else:
                self.label = ans
                break

    def _calculate(self):
        row = 0 if self.label=='Detonate' else 1
        col = ['blue','red','white'].index(self.color)
        return self.table[row][col]

    def solve(self):
        for a in range(3):
            sol = self._calculate()
            self.local_header()
            print(f"STAGE {self.stage}")
            print(f"{self.answer_pretext}Press the main button {sol[0]} times, and then press the {sol[1]} arrow.")
            if self.stage==3: break
            input(); self.stage+=1; self.display()