from .__basemod__ import BaseSolver

class AccessCodes(BaseSolver):
    NAME = 'Access Codes'

    def _calculate(self):
        grid = 'CFDEABFBACEDDCEABFEDCBFAAEBFDCBAFDCE'
        base10_sn = [int(a, 36) for a in self.eg.sn]
        ans = []
        up = 0; down = 0

        for a in base10_sn:
            for b in range(up):
                a-=10
                if a<0 and (a%10) in range(6, 10): a+=30
                elif a<0: a+=40

            for b in range(down):
                a+=10
                if a in range(36, 40): a-=30
                elif a>=40: a-=40

            temp = grid[a]
            ans.append(temp)

            match temp:
                case 'A':
                    grid = grid[-1]+grid[0:-1]
                case 'B':
                    up+=1
                case 'C':
                    down+=1
                case 'D':
                    grid = grid[1:]+grid[0]
                case 'E':
                    grid = ''.join(map(lambda x: chr(((ord(x)-ord('A')+1)%6)+ord('A')), grid))
                case 'F':
                    grid = ''.join(map(lambda x: chr(((ord(x)-ord('A')-1)%6)+ord('A')), grid))
        
        return ''.join(ans)
                
    
    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Code: {sol}")