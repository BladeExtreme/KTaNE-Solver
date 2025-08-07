from .__basemod__ import BaseSolver

class Wires(BaseSolver):
    NAME = 'Wires'

    def display(self):
        while 1:
            self.local_header()
            ans = input("Wire Colors (Each wire is seperated by a comma space) [Blue, Red, Yellow, White, Black]: ").lower().split(', ')
            if not all([a.isalpha() for a in ans]): continue
            elif len(ans) not in range(3, 7): continue
            elif not all([a in ['blue','red','yellow','white', 'black'] for a in ans]): continue
            else:
                self.wire_list = ans
                break
    
    def _calculate(self):
        match len(self.wire_list):
            case 3:
                if self.wire_list==['blue','blue','red']: return 1
                elif 'red' not in self.wire_list: return 1
                else: return 2
            case 4:
                if self.wire_list.count('red')>=2 and self.eg.sndigit[-1]%2==1: return [i for i, x in enumerate(self.wire_list) if x=='red'][-1]
                elif self.wire_list[-1]=='yellow' and 'red' not in self.wire_list: return 0
                elif self.wire_list.count('blue')==1: return 0
                elif self.wire_list.count('yellow')==2: return 3
                else: return 1
            case 5:
                if self.wire_list[-1]=='black' and self.eg.sndigit[-1]%2==1: return 3
                elif self.wire_list.count('red')==1 and self.wire_list.count('yellow')>=2: return 0
                elif 'black' not in self.wire_list: return 1
                else: return 0
            case 6:
                if 'yellow' not in self.wire_list and self.eg.sndigit[-1]%2==1: return 2
                elif self.wire_list.count('yellow') and self.wire_list.count('white')>=2: return 3
                elif 'red' not in self.wire_list: return 5
                else: return 3

    def solve(self):
        ans = self._calculate()
        self.local_header()
        print(f"Wire Colors: {', '.join([x.capitalize() for x in self.wire_list])}")
        print(f"{self.answer_pretext}Cut the {ans+1}{'st' if ans==0 else 'nd' if ans==1 else 'rd' if ans==2 else 'th'} wire")
