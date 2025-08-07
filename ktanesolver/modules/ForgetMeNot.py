from .__basemod__ import BaseSolver
from ..edgework import Edgework
import colorama as c

class ForgetMeNot(BaseSolver):
    NAME = 'Forget Me Not'

    def __init__(self, edgework:Edgework):
        self.number = []
        self.eg = edgework

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {len(self.number)} of {self.eg.modules}")
            ans = input(f"Display [0-9]: ").lower()

            if not ans.isdigit(): continue
            elif int(ans) not in range(10): continue
            else:
                self.number.append(int(ans))
                break

    def _calculate(self):
        appender = []
        ans = []

        if 'CAR' in self.eg.unlitind: appender.append(2)
        elif len(self.eg.unlitind)>len(self.eg.litind): appender.append(7)
        elif len(self.eg.unlitind)==0: appender.append(len(self.eg.litind))
        else: appender.append(int(self.eg.sndigit[-1]))

        ans.append((appender[0]+self.number[0])%10)

        if 'SERIAL' in self.eg.uniqueports and len(self.eg.sndigit)>=3: appender.append(3)
        elif ans[0]%2==0: appender.append(ans[0]+1)
        else: appender.append(ans[0]-1)

        ans.append((appender[1]+self.number[1])%10)

        for a in range(2, len(self.number)):
            if 0 in [ans[a-1], ans[a-2]]: appender.append(max([int(a) for a in self.eg.sndigit]))
            elif ans[a-1]%2==0 and ans[a-2]%2==0: appender.append(9 if len([a for a in self.eg.sndigit if int(a)%2==1])==0 else min([int(a) for a in self.eg.sndigit]))
            else: appender.append(int(str(sum([ans[a-1], ans[a-2]]))[0]))

            ans.append((appender[a]+self.number[a])%10)
        return ans

    def error(self):
        print(f"{c.Fore.RED}Forget Me Not has no numbers yet!")
        input()

    def solve(self):
        self.local_header()
        sol = self._calculate()
        print(f"{self.answer_pretext}Sequence of Numbers in Threes:")
        for a in range(0, len(sol), 3):
            try:
                for b in range(3):
                    print(f"{sol[a+b]}", end="")
                print(f" ")
            except: break
        input()