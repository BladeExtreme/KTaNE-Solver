from .__basemod__ import BaseSolver

class WireSequence(BaseSolver):
    NAME = 'Wire Sequence'

    def __init__(self, edgework):
        self.STAGE = 1
        self.wire_appear = {'red': 0, 'black': 0, 'blue': 0}
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def display(self):
        self.wire_list = []
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE} of 4")
            ans = input("1st Wire Color & Connected To (Seperated by comma space) [Blue, Red, Black] [A, B, C]: ").lower().split(', ')

            if len(ans)!=2: continue
            elif not ans[0].isalpha() or not ans[1].isalpha(): continue
            elif ans[0] not in ['blue', 'red', 'black'] or ans[1] not in 'abc': continue
            else:
                self.wire_list.append(ans)
                break
        
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE} of 4")
            print(f"1st Wire Color & Connected To: {self.wire_list[0][0].capitalize()} -> {self.wire_list[0][1].capitalize()}")
            ans = input("2nd Wire Color & Connected To (Seperated by comma space) [Blue, Red, Black] [A, B, C]: ").lower().split(', ')
            if len(ans)!=2: continue
            elif not ans[0].isalpha() or not ans[1].isalpha(): continue
            elif ans[0] not in ['blue', 'red', 'black'] or ans[1] not in 'abc': continue
            else:
                self.wire_list.append(ans)
                break
        
        while 1:
            self.local_header()
            print(f"STAGE {self.STAGE} of 4")
            print(f"1st Wire Color & Connected To: {self.wire_list[0][0].capitalize()} -> {self.wire_list[0][1].capitalize()}")
            print(f"2nd Wire Color & Connected To: {self.wire_list[1][0].capitalize()} -> {self.wire_list[1][1].capitalize()}")
            ans = input("3rd Wire Color & Connected To (Seperated by comma space) [Blue, Red, Black] [A, B, C]: ").lower().split(', ')
            if len(ans)!=2: continue
            elif not ans[0].isalpha() or not ans[1].isalpha(): continue
            elif ans[0] not in ['blue', 'red', 'black'] or ans[1] not in 'abc': continue
            else:
                self.wire_list.append(ans)
                break
        
        self.local_header()
        print(f"STAGE {self.STAGE} of 4")
        print(f"1st Wire Color & Connected To: {self.wire_list[0][0].capitalize()} -> {self.wire_list[0][1].capitalize()}")
        print(f"2nd Wire Color & Connected To: {self.wire_list[1][0].capitalize()} -> {self.wire_list[1][1].capitalize()}")
        print(f"3rd Wire Color & Connected To: {self.wire_list[2][0].capitalize()} -> {self.wire_list[2][1].capitalize()}")
    
    def _calculate(self):
        wire_occur = {
            'red': ['c','b','ac','b','ac','abc','ab','b'],
            'blue': ['b','ac','b','a','b','bc','c','ac','a'],
            'black': ['abc','ac','b','ac','b','bc','ab','c','c']
        }
        cut = []

        for x in range(3):
            target = self.wire_list[x][1]; color = self.wire_list[x][0]
            if target in wire_occur[color][self.wire_appear[color]]: cut.append(x)
            self.wire_appear[color]+=1
            self.wire_appear[color] = self.wire_appear[color]%8
        return [str(x+1)+('st' if x==0 else 'nd' if x==1 else 'rd' if x==2 else 'th') for x in cut]

    def solve(self):
        ans = self._calculate()
        if ans==[]: print(f"{self.answer_pretext}Skip this stage")
        else: print(f"{self.answer_pretext}Cut the: {', '.join(ans)} wire(s)")
        self.STAGE+=1
        
        for x in range(3):
            input()
            self.display()
            ans = self._calculate()
            if ans==[]: print(f"{self.answer_pretext}Skip this stage")
            else: print(f"{self.answer_pretext}Cut the: {', '.join(ans)} wire(s)")
            self.STAGE+=1
        self.STAGE = 1
        self.wire_appear = {'red': 0, 'black': 0, 'blue': 0}