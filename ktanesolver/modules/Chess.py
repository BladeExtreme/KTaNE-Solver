from .__basemod__ import BaseSolver

class Chess(BaseSolver):
    NAME = 'Chess'

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Positions (Each position separated with comma space): ").lower().split(', ')

            if len(ans)!=6: continue
            elif not all(a[0].isalpha() and a[1].isdigit() for a in ans): continue
            elif not all(a[0] in 'abcdef' and a[1] in '123456' for a in ans): continue
            else:
                self.positions = list(map(lambda x: [ord(x[0])-ord('a'), int(x[1])-1], ans))
                self.history = ans
                break
    
    def moves(self, table, row, col, piece):
        if piece=='k':
            directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(6) and c in range(6) and table[r][c] == 0:
                    table[r][c] = 1
        elif piece=='n':
            directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(6) and c in range(6) and table[r][c] == 0:
                    table[r][c] = 1
        else:
            if piece=='r':
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
            elif piece=='b':
                directions = [(1,1),(-1,1),(1,-1),(-1,-1)]
            elif piece=='q':
                directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
            for dr, dc in directions:
                r, c = row+dr, col+dc
                while r in range(6) and c in range(6):
                    if table[r][c]==0:  table[r][c]=1
                    elif table[r][c]!=1: break
                    r += dr
                    c += dc
        return table

    def _calculate(self):
        self.piece = [0,0,0,0,0,0]
        self.table = [[0 for a in range(6)] for b in range(6)]

        self.piece[3] = 'r'
        self.piece[4] = 'q' if (self.positions[4][0]+self.positions[4][1])%2==1 else 'r'
        self.piece[0] = 'k' if self.piece[4] == 'q' else 'b'
        self.piece[1] = 'r' if int(self.eg.sndigit[-1])%2==1 else 'n'
        self.piece[2] = 'q' if self.piece.count('r')<2 else 'k'
        self.piece[5] = 'q' if self.piece.count('q')==0 else 'n' if self.piece.count('n')==0 else 'b'

        for a in range(len(self.piece)): self.table[self.positions[a][1]][self.positions[a][0]] = self.piece[a]
        for a in range(len(self.piece)):
            self.table = self.moves(self.table, self.positions[a][1], self.positions[a][0], self.piece[a])
        
        if len(a for a in [x for y in self.table for x in y] if 0 in a)>1: return

        for a in self.table:
            if 0 in a:
                num = self.table.index(a); let = a.index(0)
                print(let)
                return "".join([['A','B','C','D','E','F'][let],str(num+1)])

    def solve(self):
        sol = self._calculate()

        self.local_header()
        print(f"Positions: {', '.join(map(lambda x: x.upper(), self.history))}")
        
        if sol is None:
            print(f"{self.answer_pretext}Coordinates are not Correct")

            while 1:
                self.local_header()
                ans = input(f"Positions (Each position separated with comma space): ").lower().split(', ')

                if len(ans)!=6: continue
                elif not all(a[0].isalpha() and a[1].isdigit() for a in ans): continue
                elif not all(a[0] in 'abcdef' and a[1] in '123456' for a in ans): continue
                else:
                    self.positions = list(map(lambda x: [ord(x[0])-ord('a'), int(x[1])-1], ans))
                    self.history = ans
                    sol = self._calculate()
                    self.local_header()
                    print(f"Positions: {', '.join(map(lambda x: x.upper(), self.history))}")
                    if sol is None: continue
                    else: break
        print(f"{self.answer_pretext}Coordinate: {sol}")
        pass