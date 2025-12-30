import colorama as c #type: ignore
from .__basemod__ import BaseSolver

c.init(autoreset=True)

class DoubleOh(BaseSolver):
    NAME = 'Double-Oh'
    table = [
        [
            [
                [60,'0X',15],[88,46,31],[74,27,53]
            ],[
                [57,36,83],[70,22,64],['0X',41,18]
            ],[
                [48,71,24],['0X',55,13],[86,30,62]
            ]
        ],[
            [
                [52,10,'0X'],[33,65,78],[47,81,26]
            ],[
                [43,85,37],[21,0,56],[68,14,72]
            ],[
                [61,28,76],[12,44,87],[50,'0X',35]
            ]
        ],[
            [
                ['0X',38,42],[25,73,67],[11,54,80]
            ],[
                [84,63,20],[16,58,'0X'],[32,77,45]
            ],[
                [75,17,51],[34,82,40],[23,66,'0X']
            ]
        ]
    ]
    goal = False

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Number on Display Screen: ")

            if not ans.isdigit(): continue
            elif len(ans)!=2: continue
            elif '9' in ans or ans[0]=='0': continue
            else:
                self.number = int(ans)
                break

    def _calculate(self):
        flatten_list = [a for d in self.table for c in d for b in c for a in b]
        a = flatten_list.index(self.number)
        xs, ys, xb, yb = [a%3, (a//3)%3, (a//9)%3, (a//27)]
        
        def check():
            if self.table[yb][xb][ys][xs] == 0:
                self.goal = True

        if xb!=1:
            tempura = []
            for a in range(3): tempura.append(str(self.table[yb][a][ys][xs]).zfill(2))
            if '0X' not in tempura: 
                check()
                return tempura
        if yb!=1:
            ebi = []
            for a in range(3): ebi.append(str(self.table[a][xb][ys][xs]).zfill(2))
            if '0X' not in ebi:
                check()
                return ebi
        if xs!=1:
            tori = []
            for a in range(3): tori.append(str(self.table[yb][xb][ys][a]).zfill(2))
            if '0X' not in tori:
                check()
                return tori
        if ys!=1:
            salmon = []
            for a in range(3): salmon.append(str(self.table[yb][xb][a][xs]).zfill(2))
            if '0X' not in salmon:
                check()
                return salmon

    def solve(self):
        self.ultra_ans = []
        while self.number!=0:
            sol_t = self._calculate()
            if self.number==0: break
            
            sol = sol_t.copy()
            for a in range(len(sol)):
                if a==1: sol[a] = c.Fore.GREEN+c.Style.BRIGHT+sol_t[a]+'*'+c.Style.RESET_ALL
            self.ultra_ans.append([self.number, sol])
            self.number = int(sol_t[1]); self._calculate()

        self.local_header()
        print(f"Guide:\n - There will be 1-4 rows with 4 numbers on each row. These row will explain the path to reach the target (which is 00).")
        print(f" - For each row, the leftmost number (before the vertical bar) is the number where your current location to find the list of numbers on the right.")
        print(f" - The numbers after the vertical bar represent the list of numbers you need to find to move towards the highlighted (green colored with asterisk) number to move.\n")
        print(f"{self.answer_pretext}")
        for a in self.ultra_ans:
            print('\t| '.join([str(a[0]).zfill(2), ', '.join(a[1])]))