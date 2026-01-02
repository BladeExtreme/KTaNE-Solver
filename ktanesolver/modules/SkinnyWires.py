from .__basemod__ import BaseSolver
from collections import Counter

class SkinnyWires(BaseSolver):
    NAME = 'Skinny Wires'
    
    def display(self):
        wires = []
        while True:
            self.local_header()
            print(f"Guide:\n - There are 5 wires on the module, each row represent a wire. \n For each row/wire, there will be 3 information required. A color, the letter port and its number port.\n - Seperate each information with a space.\n - The possible colors are: [Red, Orange, Yellow, Green, Blue, White, Black, Gray, Pink]\n - The possible letters are: [A, B, C]\n - The possible numbers are: [1, 2, 3]\n")
            for a in wires:
                print(f" > {' '.join([x.capitalize() for x in a])}")
            ans = input(f" > ").lower().split(' ')

            if len(ans)!=3: continue
            elif ans[0] not in ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'black', 'gray','pink']: continue
            elif ans[1] not in 'abc': continue
            elif ans[2] not in '123': continue
            else:
                wires.append(ans)
                if len(wires)==5:
                    self.wires = wires
                    break

    def _calculate(self):
        colors = [a[0] for a in self.wires]
        letters = [a[1] for a in self.wires]
        numbers = [a[2] for a in self.wires]
        items = list(list(a[0] for a in self.wires if a[1] in b) for b in 'abc')+list(list(a[0] for a in self.wires if a[2] in b) for b in '123')
        print(items)
        
        if colors.count('red')==1 and colors.count('black')==1 and colors.count('white')==1 and colors.count('green')==1 and colors.count('orange')==1: return [a for a in self.wires if a[0]=='red'][0]
        elif letters.count('a')==0 and list(a[0] for a in self.wires if a[2]=='3').count('black')>=1: return [a for a in self.wires if a[1]=='b'][0]
        elif numbers.count('2')==2 and list(a[0] for a in self.wires if a[2]=='2').count('green')>=1: return [a for a in self.wires if a[2] in '13'][0]
        elif len(set(colors))==2: return [a for a in self.wires if a[0]==sorted(self.wires, key=lambda x: x[0])[0][0]]
        elif any(any(count >= 3 for count in Counter(sublist).values()) for sublist in (items)): return [a for a in self.wires if a[0]==sorted(self.wires, key=lambda x: x[0], reverse=True)[0][0]][0]
        elif any(a[2]=='3' for a in self.wires if a[0]=='blue'): return [a for a in self.wires if a[0]=='blue' and a[2]=='3'][0]
        elif colors.count('green')==1 and colors.count('orange')>=1: return [a for a in self.wires if a[0]=='green'][0]
        elif colors.count('white')==1 and colors.count('black')==1 and (any(a[0]=='white' and a[2]=='1' for a in self.wires) ^ any(a[0]=='black' and a[2]=='1' for a in self.wires)): return [a for a in self.wires if a[0] in ['white', 'black'] and a[2]!='1'][0]
        elif any(a for a in self.wires if a[0]=='yellow' and a[1]=='c'): return [a for a in self.wires if a[0]=='yellow' and a[1]=='c'][0]
        elif colors.count('pink')>1: return [a for a in self.wires if a[0]=='pink'][0]
        elif colors.count('red')>=1 and colors.count('orange')>=1 and colors.count('blue')==0: return [a for a in self.wires if a[0]=='orange'][0]
        elif numbers.count('3')==0: return [a for a in self.wires if a[2]=='1'][0]
        elif any(a for a in self.wires if a[1]=='a' and a[2]=='2'): return [a for a in self.wires if a[1]=='a' and a[2]=='2'][0]
        elif colors.count('green')==0: return [a for a in self.wires if a[1]==min(letters)][0]
        elif colors.count('blue')==0: return [a for a in self.wires if a[2]==max(numbers)][0]
        elif any(colors.count(a)>1 for a in list(set(colors))): return [a for a in self.wires if colors.count(a[0])>1][0]
        elif colors.count('yellow'): return [a for a in self.wires if a[0]=='yellow'][0]
        elif colors.count('black'): return [a for a in self.wires if a[0]=='black'][0]
        elif colors.count('white'): return [a for a in self.wires if a[0]=='white'][0]
        else: return [a for a in self.wires if a[1]=='a'][0]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Guide:\n - There are 5 wires on the module, each row represent a wire. \n For each row/wire, there will be 3 information required. A color, the letter port and its number port.\n - Seperate each information with a space.\n - The possible colors are: [Red, Orange, Yellow, Green, Blue, White, Black, Gray, Pink]\n - The possible letters are: [A, B, C]\n - The possible numbers are: [1, 2, 3]\n")
        for a in self.wires:
            print(f" > {' '.join([x.capitalize() for x in a])}")
        print(f"\n{self.answer_pretext}Cut the {sol[0].capitalize()} wire, from the {sol[1].capitalize()} port, to the {sol[2].capitalize()} port")