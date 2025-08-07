from .__basemod__ import BaseSolver

class SimonSays(BaseSolver):
    NAME = 'Simon Says'

    def __init__(self, edgework):
        self.STAGE = 0
        self.store = []
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE+1}")
            ans = input(f"Flashes [Red, Blue, Yellow, Green]: ").lower()

            if not ans.isalpha(): continue
            elif ans not in ['red', 'blue', 'yellow', 'green']: continue
            else:
                self.store.append(ans)
                self.STAGE+=1
                break
    
    def _calculate(self):
        trades = {}
        vowel = any([a in 'AIUEO' for a in self.eg.snletter])
        
        match self.eg.strikes:
            case 0:
                if vowel: trades = {'red':'blue', 'blue':'red', 'yellow':'green', 'green':'yellow'}
                else: trades = {'red':'blue', 'blue':'yellow', 'yellow':'red', 'green':'green'}
            case 1:
                if vowel: trades = {'red':'yellow', 'blue':'green', 'yellow':'red', 'green':'blue'}
                else: trades = {'red':'blue', 'blue':'yellow', 'yellow':'red', 'green':'green'}
            case strikes if strikes >= 2:
                if vowel: trades = {'red':'green', 'blue':'red', 'yellow':'blue', 'green':'yellow'}
                else: trades = {'red':'yellow', 'blue':'green', 'yellow':'red', 'green':'blue'}
        
        returns = []

        for a in self.store:
            returns.append(trades[a])
        return returns

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"STAGE {self.STAGE+1}")
        print(f"Flashes: {', '.join([a.capitalize() for a in self.store])}")
        print(f"{self.answer_pretext}Respond Sequences: {', '.join([a.capitalize() for a in sol])}")
        input()
        
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE+1}")
            print(f"Flashes (- to stop the input sequence): {', '.join([a.capitalize() for a in self.store])}, ", end="")
            ans = input().lower()

            if not ans.isalpha() and ans!='-': continue
            elif ans=='-':
                print(f"{self.answer_pretext}End")
                break
            elif ans not in ['red', 'blue', 'yellow', 'green']: continue
            else:
                self.store.append(ans)
                self.STAGE+=1
            
                sol = self._calculate()
                print(f"{self.answer_pretext}Respond Sequences: {', '.join(sol)}")
                input()