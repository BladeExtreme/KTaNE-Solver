from .__basemod__ import BaseSolver

class Stars(BaseSolver):
    NAME = 'Stars'
    table = [
        [[2, 3, 4], [1, 4, 4, 3], [5, 5, 5, 3, 3], [1, 2, 3, 4, 5], [2, 5]],
        [[3, 2, 1], [0], [1, 2, 1], [1, 1, 2, 2, 3, 3], [5, 1, 4]],
        [[4, 2, 5, 1, 2, 3], [5, 4, 3, 2, 1], [4, 2, 3], [5, 3, 1], [1, 1, 4]],
        [[1], [2, 2], [3, 3, 3], [0], [1, 3, 5]],
        [[2, 5], [4, 1, 4], [1, 5, 4, 4, 3, 2], [3, 4, 2], [5]],
        [[3, 2, 4, 2], [4, 4, 3, 1, 2], [5, 5, 2, 5], [1, 2, 3, 4, 5, 4, 3, 2, 1], [3, 3, 3, 3, 1]],
        [[0], [2, 3], [1, 5], [3], [3, 4, 1, 2, 1, 2, 4]],
        [[5, 5], [4, 3, 2, 4, 5], [1, 1, 1], [5, 4, 3], [1, 5, 2]],
        [[1, 1, 1, 5, 5, 5], [5, 3, 5, 4], [2, 2, 5], [3, 1], [1, 4, 2]],
        [[1, 4, 2, 5, 3], [5, 2, 4, 5], [2, 4, 4, 1, 3], [5, 4, 3, 1, 2], [5, 2]]
    ]
    
    def display(self):
        while True:
            self.local_header()
            ans = input(f"Middle Number: ").lower()

            if not ans.isdigit(): continue
            elif int(ans) not in range(10): continue
            else:
                self.row = int(ans)
                break

    def _calculate(self):
        col = 0 if 'RJ-45' in self.eg.uniqueports else 1 if self.eg.batt>3 else 2 if any(a in 'STAR' for a in self.eg.snletter) else 3 if len(self.eg.litind)==0 else 4
        ans = self.table[self.row][col]

        return ans

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Middle Number: {self.row}")
        print(f"{self.answer_pretext}{'Submit instantly' if sol==[0] else 'Press, in order: The '+(', '.join(str(a)+('st' if a==1 else 'nd' if a==2 else 'rd' if a==3 else 'th') for a in sol))}")