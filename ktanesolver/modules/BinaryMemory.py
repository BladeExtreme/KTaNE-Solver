from .__basemod__ import BaseSolver
from ..edgework import Edgework
import colorama as c

class BinaryMemory(BaseSolver):
    NAME = 'Binary Memory'
    bank = [
        ['1342', '4231', '4231', '3412', '3421', '1432', '2341', '1234', '1423', '2134'],
        ['3412', '3214', '2314', '3142', '4132', '2134', '1342', '2314', '1423', '4123'],
        ['3412', '1234', '3124', '1234', '1234', '3421', '2143', '3412', '4132', '4132'],
        ['4231', '1324', '3412', '3124', '1324', '4123', '2143', '3421', '4132', '1342'],
        ['1423', '4213', '3142', '1342', '2413', '2314', '1234', '1324', '4213', '3412']
    ]

    def __init__(self, edgework:Edgework):
        self.number = []
        self.eg = edgework
        # self.condition = 0 if len(self.eg.ports) > 2 else 1 if len(self.eg.snletter)==3 else 2 if self.eg.hold==1 else 3 if self.eg.modules>=29 else 4
        self.condition = 3
        self.display()

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {len(self.number)}")
            ans = input(f"Color [red, green]: ").lower()

            if not ans.isalpha(): continue
            elif ans not in ['red','green']: continue
            else:
                self.number.append(0 if 'red' else 1)
                break
        self.number = [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]

    def _calculate(self):
        pressed = []
        for a in range(len(self.number)):
            initial = len(pressed)
            for b in range(4):
                if [self.bank[self.condition][a%10][b], self.number[a]] not in pressed:
                    pressed.append([self.bank[self.condition][a%10][b], self.number[a]])
                    break
                elif len([z for z in pressed if z[0]==self.bank[self.condition][a%10][b]])>=1:
                    if([z for z in pressed if z[0]==self.bank[self.condition][a%10][b]][-1][1]!=self.number[a]):
                        pressed.append([self.bank[self.condition][a%10][b], self.number[a]])
                        break
            if len(pressed)==initial: pressed.append([1, self.number[a]])    
        return ''.join(map(lambda x: x[0], pressed))

    def error(self):
        print(f"{c.Fore.RED}Binary Memory has no numbers yet!")
        input()

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Sequence of Numbers in Fours:")
        print(f" ", end="")
        for a in range(len(sol)):
            print(f"{sol[a]}", end="" if a%4!=3 else " ")
        input()