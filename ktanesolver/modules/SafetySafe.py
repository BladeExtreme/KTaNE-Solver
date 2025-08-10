from .__basemod__ import BaseSolver

class SafetySafe(BaseSolver):
    NAME = 'Safety Safe'
    table = [
        [8, 3, 4, 8, 9, 0], [10, 1, 3, 7, 3, 8], [2, 1, 1, 5, 3, 6], [11, 6, 11, 11, 7, 7], [0, 5, 5, 8, 2, 1], [4, 2, 7, 7, 1, 5], 
		[7, 4, 4, 2, 10, 5], [8, 3, 6, 6, 6, 5], [0, 11, 0, 0, 9, 10], [2, 11, 8, 0, 5, 6], [5, 2, 5, 1, 0, 4], [1, 9, 8, 11, 11, 11], 
		[1, 7, 9, 5, 6, 2], [9, 5, 1, 4, 4, 9], [5, 9, 8, 10, 2, 8], [3, 10, 9, 1, 9, 7], [4, 10, 6, 1, 4, 8], [8, 0, 4, 0, 6, 11], [9, 4, 0, 6, 3, 10], 
		[7, 6, 7, 11, 5, 3], [11, 9, 6, 3, 11, 1], [11, 11, 2, 8, 1, 0], [6, 0, 11, 6, 11, 2], [4, 2, 7, 2, 8, 10], [10, 7, 10, 10, 8, 9], 
		[3, 7, 1, 10, 0, 4], [7, 0, 3, 5, 8, 6], [9, 10, 10, 9, 1, 2], [2, 5, 11, 7, 7, 3], [10, 8, 10, 4, 10, 4], [6, 8, 0, 3, 5, 0], 
		[6, 3, 3, 3, 0, 11], [1, 1, 5, 2, 7, 3], [0, 6, 2, 4, 2, 1], [5, 4, 9, 9, 10, 7], [3, 8, 2, 9, 4, 9]
    ]

    def _calculate(self):
        validlitind = len([a for a in self.eg.snletter if any(b for b in self.eg.litind if a in b)]); validunlitind = len([a for a in self.eg.snletter if any(b for b in self.eg.unlitind if a in b)])
        offset = len(self.eg.uniqueports)*7 + validlitind*5 + validunlitind
        ans = [(self.table[int(self.eg.sn[a])+26][a]+offset)%12 if self.eg.sn[a].isnumeric() else (self.table[int(ord(self.eg.sn[a])-65)][a]+offset)%12 for a in range(len(self.eg.sn[:-1]))]
        ans.append((sum([self.table[int(self.eg.sn[a])+26][-1] if self.eg.sn[a].isnumeric() else self.table[int(ord(self.eg.sn[a])-65)][-1] for a in range(len(self.eg.sn))])+offset)%12)
        return ans

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Rotations: {', '.join(map(str, sol))}")