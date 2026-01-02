from .__basemod__ import BaseSolver

class TwoPersuasiveButtons(BaseSolver):
    NAME = 'T-Words'
    table = [
        [0,1,1,0,0],
        [0,1,0,1,1],
        [1,1,1,0,0],
        [0,1,0,1,0],
        [1,1,0,1,0]
    ]
    stage = 1
        
    def display(self):
        while True:
            self.local_header()
            print(f"STAGE {self.stage}")
            ans = input(f"Two Buttons (seperate with comma space, drop the \"me\"): ").lower().split(', ')

            if len(ans)!=2: continue
            elif not all(a in ['push','click','select','tap','press'] for a in ans): continue
            else:
                self.row = ans[0]
                self.col = ans[1]
                break

    def _calculate(self):
        buttons = ['push','click','select','tap','press']
        return self.table[buttons.index(self.row)][buttons.index(self.col)]

    def solve(self):
        for a in range(3):
            sol = self._calculate()
            self.local_header()
            print(f"STAGE {self.stage}")
            print(f"Two Buttons: {self.row.capitalize()}, {self.col.capitalize()}")
            print(f"{self.answer_pretext}{'Left' if sol==0 else 'Right'} Button")
            if self.stage!=3:
                self.stage+=1
                input()
                self.display()