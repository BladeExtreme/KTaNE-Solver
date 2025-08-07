from .__basemod__ import BaseSolver
from ..tools.semaphore import sematranslate, semadict

class Semaphore(BaseSolver):
    NAME = 'Semaphore'
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    def display(self):
        ans_list = []
        while 1:
            self.local_header()
            print(f"Direction Diagram")
            print(f"\t        N      ")
            print(f"\t    NW     NE   ")
            print(f"\t W             E")
            print(f"\t    SW     SE   ")
            print(f"\t        S      ")
            
            print()
            print(f"Flag Direction (In any order. Seperate with comma space. Enter '-' to stop inputting): ")

            for a in ans_list:
                print(f"> {', '.join(a)}")

            ans = input(f"> ").lower().split(', ')

            if ans[0]=='-' and len(ans_list)>1: break
            elif len(ans)!=2: continue
            elif not ans[0].isalpha() or not ans[1].isalpha(): continue
            elif ans[0]==ans[1]: continue
            elif not all(a.upper() in self.directions for a in ans): continue
            elif tuple(sorted([a.upper() for a in ans])) not in semadict.keys(): continue
            elif len(ans_list)==0 and tuple(sorted([a.upper() for a in ans])) not in [tuple(sorted(['N','NE'])), tuple(sorted(['N','E']))]: continue
            else:
                ans_list.append(tuple(sorted([a.upper() for a in ans])))
        self.flags = ans_list
        print(len(ans_list), len(self.flags))
        input()
    
    def _calculate(self):
        state = self.flags[0]

        if state==tuple(sorted(['N','NE'])): state = 1
        elif state==tuple(sorted(['N','E'])): state = 0

        for a in self.flags:
            if state==0 and a==tuple(sorted(['N','E'])): state = 1
            elif state==1 and a==tuple(sorted(['N','NE'])): state = 0
            else:
                if sematranslate(a, state) not in [self.eg.snletter, self.eg.sndigit][state]: return ', '.join(a)

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Direction Diagram")
        print(f"\t        N      ")
        print(f"\t    NW     NE   ")
        print(f"\t W             E")
        print(f"\t    SW     SE   ")
        print(f"\t        S      ")
        
        print()
        print(f"Flag Directions: ")

        for a in self.flags:
            print(f"> {', '.join(a)}")
        print(len(self.flags))
        print(f"{self.answer_pretext}Submit: {sol}")