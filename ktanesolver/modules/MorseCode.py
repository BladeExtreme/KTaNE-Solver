from .__basemod__ import BaseSolver
import colorama as c
from ..tools.morse import translate

class MorseCode(BaseSolver):
    NAME = 'Morse Code'

    def __init__(self, edgework):
        self.bad = False
        self.bank = {
            "beats": '3.600',
            "bistro": '3.552',
            "bombs": '3.565',
            "boxes": '3.535',
            "break": '3.572',
            "brick": '3.575',
            "flick": '3.555',
            "halls": '3.515',
            "leaks": '3.542',
            "shell": '3.505',
            "slick": '3.522',
            "steak": '3.582',
            "sting": '3.592',
            "strobe": '3.545',
            "trick": '3.532',
            "vector": '3.595'
        }
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def display(self):
        while 1:
            self.local_header()
            if self.bad: print(c.Fore.RED+"NO SOLUTION"+c.Style.RESET_ALL+' - Try inputting the morse code correctly to find the correct solution')
            ans = input("Morse Code (. or -, each code seperated by space): ").lower().split(' ')
            if not all(all([b in ['.', '-'] for b in a]) for a in ans): continue
            elif not all(translate(a) != -1 for a in ans): continue
            else:
                self.ans = ans
                break
    
    def _calculate(self):
        translated = ''.join([translate(a) for a in self.ans]); ans = []
        for a in self.bank.keys():
            if translated in (a+a): ans.append([a.capitalize(), self.bank[a]])
        if len(ans)==0: return -1
        return ans

    def solve(self):
        ans = self._calculate()

        while ans==-1:
            self.bad = True
            self.display()
            ans = self._calculate()

        self.local_header()
        print(f"Morse Code: {' '.join(self.ans)}")
        if len(ans)==1: print(f"{self.answer_pretext}Correct Transmission: {ans[0][1]}")
        else:
            print(f"{self.answer_pretext}Possible Transmissions: ")
            for x in range(len(ans)):
                print(f"> {ans[x][0]}: {ans[x][1]}")