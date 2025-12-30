from .__basemod__ import BaseSolver

class CurlyWires(BaseSolver):
    NAME = 'Curly Wires'
    table = {
        'red': [1,8,5,7,0,3,6,4,2],
        'blue': [9,5,3,6,4,1,2,7,0],
        'green': [4,3,8,2,9,6,0,1,5],
        'white': [2,9,1,8,4,7,3,5,6],
        'black': [3,7,4,0,6,2,5,1,8]
    }
    cut_order = [
        [
            [[3,1,2],[2,1,3],[1,3,2]],
            [[3,2,1],[1,2,3],[2,3,1]],
            [[2,1,3],[3,2,1],[1,2,3]]
        ],[
            [[1,3,2],[2,1,3],[2,3,1]],
            [[2,1,3],[1,2,3],[3,2,1]],
            [[3,1,2],[3,2,1],[1,3,2]]
        ]
    ]

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Wires (Left to right order, seperate with comma space) [Red, Blue, Green, White, Black]: ").lower().split(', ')

            if len(ans) != 3: continue
            elif not all(a in ['red', 'blue', 'green', 'white', 'black'] for a in ans): continue
            elif 'red' not in ans: continue
            elif ans.count('blue')>=3 or ans.count('red')>1: continue
            else:
                self.wires = ans
                break

    def _calculate(self):
        cut_order = self.cut_order[0 if any(a in 'AIUEO' for a in self.eg.snletter) else 1][self.wires.count('blue')][self.wires.index('red')]

        ans = []; let1 = self.eg.snletter[0]
        col = 0 if let1 in 'ABC' else 1 if let1 in 'DE' else 2 if let1 in 'FGH' else 3 if let1 in 'IJK' else 4 if let1 in 'LMN' else 5 if let1 in 'PQR' else 6 if let1 in 'STU' else 7 if let1 in 'VW' else 8 if let1 in 'XZ' else 9
        for a in cut_order:
            ans.append([self.wires[a-1].capitalize(), self.table[self.wires[a-1]][col]])
        return ans

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Wires: {', '.join([a.capitalize() for a in self.wires])}\n")
        print(f"{self.answer_pretext}")
        for a in range(len(sol)):
            print(f"{a+1}. {sol[a][0]}{' '*(8-len(sol[a][0]))}| Cut when the timer has: {sol[a][1]}")