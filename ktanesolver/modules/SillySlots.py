from .__basemod__ import BaseSolver

class SillySlots(BaseSolver):
    NAME = 'Silly Slots'
    table = {
        'sassy': {'blue': 'sassy', 'red': 'silly', 'green': 'soggy', 'cherry': 'sally', 'grape': 'simon', 'bomb': 'sausage', 'coin': 'steven'},
        'silly': {'blue': 'sassy', 'green': 'silly', 'red': 'soggy', 'coin': 'sally', 'bomb': 'simon', 'grape': 'sausage', 'cherry': 'steven'},
        'soggy': {'green': 'sassy', 'blue': 'silly', 'red': 'soggy', 'coin': 'sally', 'cherry': 'simon', 'bomb': 'sausage', 'grape': 'steven'},
        'sally': {'red': 'sassy', 'blue': 'silly', 'green': 'soggy', 'grape': 'sally', 'cherry': 'simon', 'bomb': 'sausage', 'coin': 'steven'},
        'simon': {'red': 'sassy', 'green': 'silly', 'blue': 'soggy', 'bomb': 'sally', 'grape': 'simon', 'cherry': 'sausage', 'coin': 'steven'},
        'sausage': {'red': 'sassy', 'blue': 'silly', 'green': 'soggy', 'grape': 'sally', 'bomb': 'simon', 'coin': 'sausage', 'cherry': 'steven'},
        'steven': {'green': 'sassy', 'red': 'silly', 'blue': 'soggy', 'cherry': 'sally', 'bomb': 'simon', 'coin': 'sausage', 'grape': 'steven'}
    }

    def display(self):
        temp = []; self.history = []
        while True:
            self.local_header()
            ans = input(f"Display: ").lower()

            if ans not in self.table: continue
            else:
                self.code_disp = ans
                break

        while True:
            self.local_header()
            print(f"Display: {self.code_disp}")
            print(f"Symbol and Color (Each line represents a column, indicated by the 'left', 'middle', 'right'. Separate color and object with a space. e.g. Red Bomb, Blue Coin, Green Cherry)): "); a = 0
            for _ in range(len(temp)):
                print(f" {'Left  : ' if a==0 else 'Middle: ' if a==1 else 'Right : '}{' '.join(map(lambda x:x.capitalize(), temp[a]))}")
                a+=1
            ans = input(f" {'Left  : ' if a==0 else 'Middle: ' if a==1 else 'Right : '}").lower().split(' ')

            if len(ans)!=2: continue
            elif not ans[0].isalpha() and ans[1].isalpha(): continue
            elif not ans[0] in ['red','blue','green']: continue
            elif not ans[1] in ['cherry','bomb','grape','coin']: continue
            else:
                temp.append(ans)
                if len(temp)==3: break
        
        self.history.append(list(map(lambda x: [self.table[self.code_disp][x[0]], self.table[self.code_disp][x[1]]], temp)))

    def _calculate(self):
        if self.history[-1].count(['silly','sausage'])==1: return -1
        if self.history[-1].count(['sassy','sally'])==1:
            pos = self.history[-1].index(['sassy','sally'])
            if len(self.history)>2 and 'soggy' not in self.history[-3][pos][0]:
                return -1
        if self.history[-1].count(['soggy','steven'])>=2: return -1
        if len([a for a in self.history[-1] if 'simon' in a and 'sassy' not in a])==3: return -1
        
        for i in range(3):
            if 'sausage' in self.history[-1][i]:
                adjacent = []
                if i>0: adjacent.append(i-1)
                if i<2: adjacent.append(i+1)
                for j in adjacent:
                    if 'sally' in self.history[-1][j] and 'soggy' not in self.history[-1][j]: return -1
        
        if len([a for a in self.history[-1] if 'silly' in a])==2:
            if not all('steven' in a for a in self.history[-1] if 'silly' in a): return -1
        
        if len([a for a in self.history[-1] if 'soggy' in a])==1:
            if len(self.history)>2 and not any('sausage' in a for a in self.history[-3]): return -1
        
        if len(set(map(tuple, self.history[-1])))==1:
            if len(self.history) > 1 and ['soggy','sausage'] not in self.history[-2]:
                return -1
        
        if len(list(set(a[0] for a in self.history[-1])))==1:
            if not any('sally' in a for a in self.history[-1]) and not (len(self.history)>1 and ['silly','steven'] in self.history[-2]): return -1
        
        if self.history[-1].count(['silly','simon'])>=1:
            if not any(['sassy','sausage'] in a for a in self.history[:-1]): return -1
            return 0

    def solve(self):
        sol = self._calculate()
        
        for x in range(4):
            self.local_header()
            print(f"Display: {self.code_disp}")
            print(f"Symbol and Color: ")
            for _ in range(len(self.history[-1])):
                print(f" {'Left  : ' if _==0 else 'Middle: ' if _==1 else 'Right : '}{' '.join(map(lambda x:x.capitalize(), self.history[-1][_]))}")
            print(f"{self.answer_pretext}{'Roll' if sol==-1 else 'Keep'}")
            if sol==-1 and x!=3:
                input()
                self.display()
            else:
                break