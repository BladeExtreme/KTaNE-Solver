from .__basemod__ import BaseSolver
import random as r
from .ForgetMeNot import ForgetMeNot 

class SevenWires(BaseSolver):
    NAME = 'Seven Wires'

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Number: ")
            
            if not ans.isdigit(): continue
            elif len(ans)>=3: continue
            else:
                self.number = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"Number: {self.number}")
            ans = input("Wire Colors (Each wire is separated by a comma space) [Blue, Red, Yellow, Black]: ").lower().split(', ')
            if not all(a.isalpha() for a in ans): continue
            elif len(ans)!=7: continue
            elif not all(a in ['blue','red','yellow', 'black'] for a in ans): continue
            else:
                self.wire_list = ans
                break
    
    def _calculate(self):
        if 'FRK*' in self.eg.litind and 'CLR*' in self.eg.litind: return 2
        elif any(isinstance(m, ForgetMeNot) for m in self.eg.solved_modules): return 6
        elif len([a for a in self.eg.snletter if a in 'AIUEO'])!=len(self.eg.snletter) and len(self.eg.sndigit)>0: return 1 if int(self.eg.sndigit[-1])%8==0 else int(self.eg.sndigit[-1])%8
        elif self.number in [4, 8, 15, 16, 23, 42]: return 4
        elif self.number == 0: return 6
        elif self.eg.solves>=2 and self.eg.solves%6==0: return 1
        elif self.eg.batt==4 and self.eg.hold==2 and 'BOB*' in self.eg.litind: return r.randint(1,7)
        elif self.eg.batt>5: return 5
        elif len([a for a in self.wire_list if a in ['yellow','blue']]): return 5
        elif self.number%20==0: return 7
        elif 'Y' in self.eg.snletter or '0' in self.eg.sndigit: return 3
        elif 'IND*' in self.eg.litind: return 5
        elif self.wire_list.count('red')>=2: return 6
        elif self.number%7 == 0: return 7
        # elif two factor doesn't get included
        elif int(self.eg.sndigit[-1])%2==0: return 3
        else: return 4

    def solve(self):
        ans = self._calculate()
        self.local_header()
        print(f"Number: {self.number}")
        print(f"Wire Colors: {', '.join([a.capitalize() for a in self.wire_list])}")
        print(f"{self.answer_pretext}Cut the {ans+1}{'st' if ans==0 else 'nd' if ans==1 else 'rd' if ans==2 else 'th'} wire")