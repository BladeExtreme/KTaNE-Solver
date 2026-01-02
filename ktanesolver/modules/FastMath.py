from .__basemod__ import BaseSolver

class FastMath(BaseSolver):
    NAME = 'Fast Math'
    table = [
        [25, 11, 53, 97, 2, 42, 51, 97, 12, 86, 55, 73, 33],
        [54, 7, 32, 19, 84, 33, 27, 78, 26, 46, 9, 13, 58],
        [86, 37, 44, 1, 5, 26, 93, 49, 18, 69, 23, 40, 22],
        [54, 28, 77, 93, 11, 0, 35, 61, 27, 48, 13, 72, 80],
        [99, 36, 23, 95, 67, 5, 26, 17, 44, 60, 26, 41, 67],
        [74, 95, 3, 4, 56, 23, 54, 29, 52, 38, 10, 76, 98],
        [88, 46, 37, 96, 2, 52, 81, 37, 12, 70, 14, 36, 78],
        [54, 43, 12, 65, 94, 3, 47, 23, 16, 62, 73, 46, 21],
        [7, 33, 26, 1, 67, 26, 27, 77, 83, 14, 27, 93, 9],
        [63, 64, 94, 27, 48, 84, 33, 10, 16, 74, 43, 99, 4],
        [35, 39, 3, 25, 47, 62, 38, 45, 88, 48, 34, 31, 27],
        [67, 30, 27, 71, 9, 11, 44, 37, 18, 40, 32, 15, 78],
        [13, 23, 26, 85, 92, 12, 73, 56, 81, 7, 75, 47, 99]
    ]
    flag = False; stage = 1; offset = None
    
    def display(self):
        while True:
            self.local_header()
            print(f"STAGE {self.stage}")
            ans = input(f"Display (seperated with space. If the stage ends, enter '-'): ").lower().split(' ')

            if ans == ['-']:
                self.flag = True
                break

            if len(ans)!=2: continue
            elif not all(a.upper() in ['A','B','C','D','E','G','K','N','P','S','T','X','Z'] for a in ans): continue
            else:
                self.disp = ans
                break

    def offset_calc(self):
        offset = 0
        if 'MSA*' in self.eg.litind: offset+=20
        if 'SERIAL' in self.eg.uniqueports: offset+=14
        if any([a in ['F','A','S','T'] for a in self.eg.snletter]): offset-=5
        if 'RJ-45' in self.eg.uniqueports: offset+=27
        if self.eg.batt>3: offset-=15
        return offset

    def _calculate(self):
        letters = 'abcdegknpstxz'

        if self.flag: return None
        if self.offset is None: self.offset = self.offset_calc()
        number = (self.table[letters.index(self.disp[0])][letters.index(self.disp[1])]+self.offset)%100
        if number<0: number+=50
        return number

    def solve(self):
        while True:
            sol = self._calculate()
            if self.flag: 
                print(f"{self.answer_pretext}Module is solved.")
                break

            self.local_header()
            print(f"STAGE {self.stage}")
            print(f"Display (seperated with space. If the stage ends, enter '-'): {' '.join(a.upper() for a in self.disp)}")
            print(f"{self.answer_pretext}{str(sol).zfill(2)}")
            input()
            self.stage+=1
            self.display()