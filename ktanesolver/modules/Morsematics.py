from .__basemod__ import BaseSolver
from ..tools.morse import translate, reverseTranslate

class Morsematics(BaseSolver):
    NAME = 'Morsematics'

    def display(self):
        self.morse_code = []
        while 1:
            self.local_header()
            ans = input(f"Left Morse (. or -): ").lower()
            if not all(a in ['.', '-']  for a in ans): continue
            elif translate(ans) == -1: continue
            else:
                self.morse_code.append(ans)
                break
        
        while 1:
            self.local_header()
            print(f"Left Morse: {self.morse_code[0]}")
            ans = input(f"Middle Morse (. or -): ").lower()
            if not all(a in ['.', '-']  for a in ans): continue
            elif translate(ans) == -1: continue
            else:
                self.morse_code.append(ans)
                break
        
        while 1:
            self.local_header()
            print(f"Left Morse: {self.morse_code[0]}")
            print(f"Middle Morse: {self.morse_code[1]}")
            ans = input(f"Right Morse (. or -): ").lower()
            if not all(a in ['.', '-']  for a in ans): continue
            elif translate(ans) == -1: continue
            else:
                self.morse_code.append(ans)
                break
    
    def _calculate(self):
        received = [ord(translate(a).upper())-ord('A')+1 for a in self.morse_code]
        receivedL = [translate(a).upper() for a in self.morse_code]
        square = [1,4,9,16,25,36,49]
        prime = [2,3,5,7,11,13,17,19,23]

        A = self.eg.sn[3]
        B = self.eg.sn[4]

        if A.isalpha(): A = ord(A)-ord('A')+1
        else: A = int(A)
        if B.isalpha(): B = ord(B)-ord('A')+1
        else: B = int(B)

        for a in self.eg.ind:
            if any(b in a for b in receivedL):
                if '*' in a:
                    A+=1
                    if A<=0: A+=26
                    elif A>26: A-=26
                else:
                    B+=1
                    if B<=0: B+=26
                    elif B>26: B-=26

        if (A+B)-26 if A+B>26 else A+B in square:
            A+=4
            if A>26: A-=26
        else:
            B-=4
            if B>26: B-=26
    
        A+=max(received)
        if A>26: A-=26


        for a in received:
            if a in prime:
                A-=a
                if A<=0: A+=26
        
        for b in received:
            if b in square:
                B-=b
                if B<=0: B+=26
        
        for x in received:
            if x%self.eg.batt==0:
                A-=x
                B-=x
                if A<=0: A+=26
                if B<=0: B+=26

        if A==B:
            return reverseTranslate(chr(ord('A')+A-1))
        elif A>B:
            total = A-B
            while total<=0:
                total+=26
            return reverseTranslate(chr(ord('A')+total-1))
        elif A<B:
            total = A+B
            while total>26:
                total-=26
            return reverseTranslate(chr(ord('A')+total-1))

    def solve(self):
        sol = self._calculate()
        print(f"{self.answer_pretext}Morse: {sol}")