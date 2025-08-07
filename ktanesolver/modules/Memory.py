from .__basemod__ import BaseSolver
import colorama as c

c.init()

class Memory(BaseSolver):
    NAME = 'Memory'

    def __init__(self, edgework):
        self.STAGE = 1
        self.buttonsdisp = [
            ['-----', '-----', '-----', '-----'],
            ['| 1 |', '| 2 |', '| 3 |', '| 4 |'],
            ['-----', '-----', '-----', '-----']
        ]
        self.button = []; self.disp = 0; self.presses = []
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def showGoodButton(self, pos=0):
        print(' '.join(self.buttonsdisp[0]))
        for x in range(len(self.buttonsdisp[1])):
            if x==pos-1: print(c.Back.GREEN+self.buttonsdisp[1][x][0]+self.buttonsdisp[1][x][1:-1]+self.buttonsdisp[1][x][-1], end=" ")
            else: print(self.buttonsdisp[1][x][0]+self.buttonsdisp[1][x][1:-1]+self.buttonsdisp[1][x][-1], end=" ")
        print()
        print(' '.join(self.buttonsdisp[2]))
        print()

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE} of 5")
            self.showGoodButton()
            ans = input("Display (1-4): ").lower()

            if not ans.isdigit(): continue
            elif int(ans) not in range(1, 5): continue
            else:
                self.disp = ans
                break
        
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE} of 5")
            self.showGoodButton()
            print(f"Display: {self.disp}")
            ans = input(f"Label from 1st position to 4th (left to right, seperated by comma space): ").lower().split(', ')

            if not all(a.isdigit() for a in ans): continue
            elif not all(int(a) in range(1, 5) for a in ans): continue
            elif not len(set(ans))!=4: continue
            else:
                self.button = ans
                break
    
    def _calculate(self):
        disp = int(self.disp)
        labels = [int(x) for x in self.button]

        if self.STAGE == 1:
            match disp:
                case 1 | 2: pos = 2
                case 3: pos = 3
                case 4: pos = 4
            label = labels[pos - 1]
            self.presses.append({'p': pos, 'l': label})
            return self.presses[-1]

        elif self.STAGE == 2:
            match disp:
                case 1: label = 4; pos = labels.index(label) + 1
                case 2 | 4: pos = self.presses[0]['p']; label = labels[pos - 1]
                case 3: pos = 1; label = labels[0]
            self.presses.append({'p': pos, 'l': label})
            return self.presses[-1]

        elif self.STAGE == 3:
            match disp:
                case 1: label = self.presses[1]['l']; pos = labels.index(label) + 1
                case 2: label = self.presses[0]['l']; pos = labels.index(label) + 1
                case 3: pos = 3; label = labels[pos - 1]
                case 4: label = 4; pos = labels.index(label) + 1
            self.presses.append({'p': pos, 'l': label})
            return self.presses[-1]
        
        elif self.STAGE == 4:
            match disp:
                case 1: pos = self.presses[0]['p']
                case 2: pos = 1
                case 3 | 4: pos = self.presses[1]['p']
            label = labels[pos - 1]
            self.presses.append({'p': pos, 'l': label})
            return self.presses[-1]

        elif self.STAGE == 5:
            match disp:
                case 1: label = self.presses[0]['l']
                case 2: label = self.presses[1]['l']
                case 3: label = self.presses[3]['l']
                case 4: label = self.presses[2]['l']
            pos = labels.index(label) + 1
            self.presses.append({'p': pos, 'l': label})
            return self.presses[-1]

        return {}

    def solve(self):
        while 1:
            sol = self._calculate()
            self.local_header()
            print(f"STAGE {self.STAGE} of 5")
            self.showGoodButton(sol['p'])
            print(f"Display: {self.disp}")
            print(f"Label: {', '.join(self.button)}")
            print(f"{self.answer_pretext}Press the {str(sol['p'])+('st' if sol['p']==1 else 'nd' if sol['p']==2 else 'rd' if sol['p']==3 else 'th')} button")
            if self.STAGE<5:
                input()

                self.STAGE+=1
                self.display()
            elif self.STAGE==5: break