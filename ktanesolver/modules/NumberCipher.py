from .__basemod__ import BaseSolver

class NumberCipher(BaseSolver):
    NAME = 'The Number Cipher'

    def display(self):
        while True:
            self.local_header()
            ans = input(f"Color Led [Red, Blue, Green, Off] (Separated by comma space): ").lower().split(', ')
            
            if len(ans)!=3: continue
            elif not all(a in ['red','blue','green','off'] for a in ans): continue
            else:
                self.color = [a for a in ans if a!='off']
                break
        
        while True:
            self.local_header()
            print(f"Color Led: {', '.join(self.color)}")
            ans = input(f"Numbers (Separated by comma space): ").lower().split(', ')
            
            if len(ans)!=3: continue
            elif not all(a.isdigit() for a in ans): continue
            elif not all(int(a) in range(0,10) for a in ans): continue
            else:
                self.numbers = map(int, ans)
                break

    def _calculate(self):
        def digital_root(n):
            return n%9 if n%9!=9 else 9

        formula = {
            'A': lambda a,b,c: digital_root((a*b)+c),
            'B': lambda a,b,c: (a+c)%10,
            'C': lambda a,b,c: (a*c)%10,
            'D': lambda a,b,c: digital_root((a*b*c)),
            'E': lambda a,b,c: digital_root(a+(b*c)),
            'F': lambda a,b,c: (b*c)%10,
            'G': lambda a,b,c: (b-c)%10,
            'H': lambda a,b,c: digital_root(a+b+c)
        }
        diagram = 'HBGFACED'; gt = []

        if 'red' in self.color: gt.append('1')
        else: gt.append('0')

        if 'green' in self.color: gt.append('1')
        else: gt.append('0')

        if 'blue' in self.color: gt.append('1')
        else: gt.append('0')

        ans = formula[diagram[int(''.join(gt), 2)]](self.numbers[0], self.numbers[1], self.numbers[2])
        return ans


    def solve(self):
        sol = self._calculate()
        print(f"Color Led: {', '.join(self.color)}")
        print(f"Numbers: {', '.join(self.numbers)}")
        print(f"{self.answer_pretext}Submit: {sol}")