from .__basemod__ import BaseSolver

class LEDGrid(BaseSolver):
    NAME = 'LED Grid'
    
    def display(self):
        colors = []
        while True:
            self.local_header()
            print(f"Guide:\n - Each row represents a row from the LED Grid, starting from the topmost row to lowermost row.\n - Each row should have three colors (White, Red, Blue, Yellow, Green, Orange, Pink, Purple, Black)\n")
            print(f"Grid: ")
            for a in colors:
                print(f" > {', '.join([b.capitalize() for b in a])}")
            ans = input(f" > ").lower().split(', ')

            if len(ans)!=3: continue
            elif not all(a in ['white', 'red', 'blue', 'yellow', 'green', 'orange', 'pink', 'purple', 'black'] for a in ans): continue
            else:
                colors.append(ans)
                if len(colors)==3:
                    self.grid = [a for b in colors for a in b]
                    break

    def _calculate(self):
        off = self.grid.count('black')
        if off==0:
            if self.grid.count('orange'): return ['C','D','A','B']
            elif self.grid.count('red')>=3: return ['D','A','C','B']
            elif len([a for a in self.grid if self.grid.count(a)==2])>=2: return ['B','A','C','D']
            elif self.grid[6]==self.grid[7]==self.grid[8]: return ['A','C','D','B']
            else: return ['B','C','D','A']
        elif off==1:
            if len(set(self.grid))==len(self.grid): return ['D','C','B','A']
            elif self.grid[0]==self.grid[1]==self.grid[2]: return ['B','C','A','D']
            elif self.grid.count('red')==3 or self.grid.count('pink')==3 or self.grid.count('purple')==3: return ['C','B','A','D']
            elif self.grid.count('white')==1 or self.grid.count('blue')==2 or self.grid.count('yellow')==3: return ['B','A','D','C']
            else: return ['D','B','A','C']
        elif off==2:
            if self.grid.count('purple')>=3: return ['A','D','C','B']
            elif len([a for a in self.grid if self.grid.count(a)==2])==2: return ['B','C','A','D']
            elif self.grid.count('white')>=1 and self.grid.count('orange')>=1 and self.grid.count('pink')>=1: return ['D','B','C','A']
            elif self.grid.count('green')==1 or self.grid.count('yellow')==2 or self.grid.count('red')==3 or self.grid.count('blue')==4: return ['C','A','D','B']
            else: return ['C','D','B','A']
        elif off==3:
            if self.grid.count('orange')==2: return ['B','D','A','C']
            elif len([a for a in self.grid if self.grid.count(a)==2])>1: return ['C','A','D','B']
            elif self.grid.count('purple')==0: return ['D','C','A','B']
            elif self.grid.count('red')>=1 and self.grid.count('yellow')>=1: return ['A','C','D','B']
            else: return ['B','D','C','A']
        elif off==4:
            if self.grid[3]==self.grid[4]==self.grid[5]: return ['B','C', 'D','A']
            elif self.grid.count('green')>=2: return ['A','B','D','C']
            elif len([a for a in self.grid if self.grid.count(a)==2])==2: return ['C','B','D','A']
            elif self.grid.count('pink')==0: return ['D','A','B','C']
            else: return ['A','B','C','D']

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Guide:\n - Each row represents a row from the LED Grid, starting from the topmost row to lowermost row.\n - Each row should have three colors (White, Red, Blue, Yellow, Green, Orange, Pink, Purple, Black)\n")
        print(f"Grid: ")
        for a in range(0, len(self.grid), 3):
            print(f" > {', '.join([b.capitalize() for b in self.grid[a:a+3]])}")
        print(f"\n{self.answer_pretext}{', '.join(sol)}")