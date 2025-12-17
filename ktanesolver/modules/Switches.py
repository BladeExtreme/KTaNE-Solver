from .__basemod__ import BaseSolver
from collections import deque

class Switches(BaseSolver):
    NAME = 'Switches'
    forbidden = [4,11,15,18,19,23,24,26,28,30]

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Current State [Up, Down] (In order of left to right, separate with comma space): ").lower().split(', ')

            if len(ans)!=5: continue
            elif not all(a in ['up','down'] for a in ans): continue
            elif int(''.join(['0' if a=='down' else '1' for a in ans]), 2) in self.forbidden: continue
            else:
                self.current = int(''.join(['0' if a=='down' else '1' for a in ans]), 2)
                break
        
        while 1:
            self.local_header()
            print(f"Current State: {', '.join(['Up' if a=='1' else 'Down' for a in bin(self.current)[2:].zfill(5)])}")
            ans = input(f"Target State [Up, Down] (In order of left to right, separate with comma space): ").lower().split(', ')

            if len(ans)!=5: continue
            elif not all(a in ['up','down'] for a in ans): continue
            elif int(''.join(['0' if a=='down' else '1' for a in ans]), 2) in self.forbidden: continue
            else:
                self.target = int(''.join(['0' if a=='down' else '1' for a in ans]), 2)
                break
    
    def _calculate(self):
        queue = deque([self.current, []])
        vis = set()

        while 1:
            node, path = queue.popleft()
            if node==self.target: return path
            elif node in vis or node in self.forbidden: continue

            for a in range(5):
                nodeBin = list(bin(node)[2:].zfill(5))
                nodeBin[a] = str((int(nodeBin[a])+1)%2)
                queue.append([int(''.join(nodeBin), 2), path+[a]])

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Current State: {', '.join(['Up' if a=='1' else 'Down' for a in bin(self.current)[2:].zfill(5)])}")
        print(f"Target State: {', '.join(['Up' if a=='1' else 'Down' for a in bin(self.target)[2:].zfill(5)])}")
        print(f"{self.answer_pretext}Flip the switch in these order: {', '.join([str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th') for a in sol])}")