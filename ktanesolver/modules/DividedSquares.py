import math
import colorama as c
from itertools import product
from .__basemod__ import BaseSolver

c.init()

class DividedSquares(BaseSolver):
    NAME = 'Divided Squares'
    table = [
        [None, 9, 4, 2, 10, 6],
        [20, None, 13, 7, 19, 22],
        [21, 25, None, 1, 29, 5],
        [14, 24, 16, None, 3, 18],
        [12, 27, 0, 23, None, 26],
        [11, 15, 28, 17, 8, None]
    ]
    column_index = ['red','yellow','green','blue','black','white']

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Number of Squares: ").lower()

            if not ans.isdigit(): continue
            elif not (math.isqrt(int(ans))**2 == int(ans)): continue
            else:
                self.squares = int(int(ans)**0.5)
                break
        
        ctr = 0; self.color = []
        while ctr!=int(self.squares**2):
            self.local_header()
            for a in range(0, len(self.color), self.squares):
                print('\t'.join(map(lambda x: x.capitalize(), self.color[a:a+self.squares])))
            if len(self.color)!=0: print()
            print(f"Number of Squares: {self.squares**2}")
            ans = input(f"Color of Squares in Each Row [Red, Yellow, Green, Blue, Black, White] (Each line represents one row. Each column is separated with Comma Space.): ").lower().split(', ')

            if len(ans)!=self.squares: continue
            elif not all(a in self.column_index for a in ans): continue
            else:
                self.color.extend(ans)
                ctr += self.squares
        
        if len(self.color)!=1: self.color_index, self.init_color = self._calculate(mode=1)
        else: self.color_index = 0; self.init_color = self.color[0]

        while True:
            self.local_header()
            for a in range(self.squares):
                for b in range(self.squares):
                    print((c.Fore.GREEN if (a*self.squares)+b==self.color_index else '')+self.color[(a*self.squares)+b].capitalize(), end="\t")
                print()
            if len(self.color)!=0: print()
            print(f"Number of Squares: {self.squares**2}")
            print(f"Initial Color: {self.init_color.capitalize()}")
            ans = input(f"Tapped Color: ").lower()

            if not ans.isalpha(): continue
            elif ans not in self.column_index: continue
            elif ans==self.init_color: continue
            else:
                self.tap_color = ans
                break
    
    def _calculate(self, mode):
        if mode==1:
            table = [self.color[a:a+self.squares] for a in range(0, len(self.color), self.squares)]
            score_table = [[0 for a in range(self.squares)] for b in range(self.squares)]
            snpos = list(ord(a.upper())-ord('A')+1 for a in self.eg.sn)
            
            for row, col, (dr, dc) in product(range(self.squares), range(self.squares), [(0,1),(1,0)]):
                if row+dr not in range(self.squares) or col+dc not in range(self.squares): continue
                else:
                    n = self.table[self.column_index.index(table[row+dr][col+dc])][self.column_index.index(table[row][col])]
                    if n is None: continue
                    elif n==0 or n>26: continue
                    elif n in snpos:
                        score_table[row][col] += 1
                        score_table[dr+row][dc+col] += 1
            
            flat_score_table = list(a for b in table for a in b)
            return flat_score_table.index(max(flat_score_table)), self.color[flat_score_table.index(max(flat_score_table))]
        elif mode==2:
            return self.table[self.column_index.index(self.tap_color)][self.column_index.index(self.init_color)] + int(self.squares**2) - 1

    def showSolve(self):
        self.local_header()
        print(f"{self.answer_pretext}Tap when the amount of solves is: {self.max_solve}")
        input()

    def solve(self):
        sol = self._calculate(2)

        self.max_solve = sol

        self.local_header()
        for a in range(self.squares):
            for b in range(self.squares):
                print((c.Fore.GREEN if (a*self.squares)+b==self.color_index else '')+self.color[(a*self.squares)+b].capitalize(), end="\t")
            print()
        if len(self.color)!=0: print()
        print(f"Number of Squares: {self.squares**2}")
        print(f"Initial Color: {self.init_color.capitalize()}")
        print(f"Tapped Color: {self.tap_color.capitalize()}")
        print(f"{self.answer_pretext}When solves is: {sol}")
    
    def moduleSolve(self):
        if self.eg.solves==self.max_solve:
            self.showSolve()