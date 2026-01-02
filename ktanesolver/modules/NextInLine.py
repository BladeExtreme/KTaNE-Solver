from .__basemod__ import BaseSolver

class NextInLine(BaseSolver):
    NAME = 'Next in Line'
    wire = None; table = [
        ["blue","gray","orange","yellow","red","green","black","white"],
        ["yellow","red","gray","blue","orange","white","green","black"],
        ["orange","green","blue","black","white","gray","yellow","red"],
        ["green","white","black","gray","yellow","orange","red","blue"],
        ["white","black","green","orange","gray","red","blue","yellow"],
        ["black","yellow","white","red","green","blue","gray","orange"],
        ["gray","blue","red","white","black","yellow","orange","green"]
    ]; iteration = 1; curr_wire = 'red'
    
    def display(self):
        while True:
            self.local_header()
            print(f"ITERATION: {self.iteration}")
            ans = input(f"Current Wire Color: ").lower()

            if ans not in ['red','orange','yellow','green','blue','black','white','gray']: continue
            else:
                self.wire = ans
                break

    def _calculate(self):
        col = ['red','orange','yellow','green','blue','black','white','gray'].index(self.curr_wire)
        row = self.iteration-2

        if self.iteration==1:
            self.curr_wire = self.wire
            return 'Cut'
        if self.table[row][col]==self.wire:
            self.curr_wire = self.wire
            return 'Cut'
        else: return 'Don\'t Cut'

    def solve(self):
        for a in range(8):
            sol = self._calculate()
            self.local_header()
            print(f"ITERATION: {self.iteration}")
            print(f"Current Wire Color: {self.wire.capitalize()}")
            print(f"{self.answer_pretext}{sol}")
            self.iteration+=1
            if self.iteration!=9:
                input()
                self.display()