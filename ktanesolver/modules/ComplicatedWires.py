from .__basemod__ import BaseSolver

class ComplicatedWires(BaseSolver):
    NAME = 'Complicated Wires'
    table = [
        ['c','s','s','s'],
        ['c','c','d','p'],
        ['d','b','p','s'],
        ['b','b','p','d']
    ]

    def display(self):
        self.wires = []
        while 1:
            self.local_header()
            ans = input(f"Wire Colors [Red, Blue, White, RedBlue] (Seperated with comma space): ").lower().split(', ')

            if not all([a.isalpha() for a in ans]): continue
            elif not all([a in ['red','blue','white','redblue'] for a in ans]): continue
            else:
                for a in ans: self.wires.append({'c': a, 's': False, 'l': False})
                break
        
        while 1:
            self.local_header()
            print(f"Wire Colors: {', '.join([a['c'].capitalize() for a in self.wires])}")
            ans = input(f"Stars on Wire (1-{len(self.wires)}, seperated with comma space): ").lower().split(', ')

            if not all([a.isdigit() for a in ans]): continue
            elif not all([int(a)-1 in range(len(self.wires)) for a in ans]): continue
            else:
                for a in ans:
                    self.wires[int(a)-1]['s'] = True
                break
        
        while 1:
            self.local_header()
            print(f"Wire Colors: {', '.join([a['c'].capitalize() for a in self.wires])}")
            print(f"Stars on Wire: {', '.join([str(a+1) for a in range(len(self.wires)) if self.wires[a]['s']])}")
            ans = input(f"LED on Wire (1-{len(self.wires)}, seperated with comma space): ").lower().split(', ')

            if not all([a.isdigit() for a in ans]): continue
            elif not all([int(a)-1 in range(len(self.wires)) for a in ans]): continue
            else:
                for a in ans:
                    self.wires[int(a)-1]['l'] = True
                break
    
    def _calculate(self):
        ans = []
        for a in range(len(self.wires)):
            row = int(str(int(self.wires[a]['l']))+str(int(self.wires[a]['s'])), 2)
            col = ['white','red','blue','redblue'].index(self.wires[a]['c'])

            get = self.table[row][col]
            print(row, col)
            match get:
                case 'c': ans.append(a+1)
                case 'd': pass
                case 's': 
                    if int(self.eg.sndigit[-1])%2==0: ans.append(a+1)
                case 'p': 
                    if 'PARALLEL' in self.eg.uniqueports: ans.append(a+1)
                case 'b':
                    if self.eg.batt>=2: ans.append(a+1)
        input()
        return [str(a)+('st' if a==1 else 'nd' if a==2 else 'rd' if a==3 else 'th') for a in ans]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Wire Colors: {', '.join([a['c'].capitalize() for a in self.wires])}")
        print(f"Stars on Wire: {', '.join([str(a+1) for a in range(len(self.wires)) if self.wires[a]['s']])}")
        print(f"LED on Wire: {', '.join([str(a+1) for a in range(len(self.wires)) if self.wires[a]['l']])}")
        print(f"{self.answer_pretext}Cut wires on the: {', '.join(sol)}")