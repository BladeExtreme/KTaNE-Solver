from .__basemod__ import BaseSolver
from ..edgework import Edgework
import colorama as c

class Troll(BaseSolver):
    NAME = 'The Troll'

    def __init__(self, edgework:Edgework, state=0, amount_of_trolls=1, unsolved_Trolls=0):
        self.eg = edgework
        self.amount = amount_of_trolls
        self.unsolved = unsolved_Trolls
        self.state = state
        self.stage = c.Fore.RED+'DORMANT' if self.state==0 else c.Fore.YELLOW+'PREPPED' if self.state==1 else c.Fore.GREEN+'ACTIVATED'
        self.track = 0

    def display(self):
        self.local_header()
        print(f"STAGE - {self.stage}")
    
    def _calculate(self):
        if self.state==0:
            self.display()
            ans = (self.eg.modules-self.amount)%13 + (self.eg.solves-self.unsolved)%7 + 1
            self.state = 1
            return ' '+str(ans)+' times'
        elif self.state==1:
            self.display()
            return ' Nothing'
        elif self.state==2:
            self.display()
            self.state = 3
            return f' when last digit of timer is {self.eg.batt%10}'

    def solve(self):
        sol = self._calculate()
        print(f"{self.answer_pretext}Tap{sol}")
        self.stage = c.Fore.RED+'DORMANT' if self.state==0 else c.Fore.YELLOW+'PREPPED' if self.state==1 else c.Fore.GREEN+'ACTIVATED'
        input()
    
    def moduleSolve(self):
        self.track+=1
        if self.track==2:
            self.state += 1
            self.stage = c.Fore.RED+'DORMANT' if self.state==0 else c.Fore.YELLOW+'PREPPED' if self.state==1 else c.Fore.GREEN+'ACTIVATED'