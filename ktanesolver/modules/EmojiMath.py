import re   
from .__basemod__ import BaseSolver

class EmojiMath(BaseSolver):
    NAME = 'Emoji Math'
    emojis = [':)', '=(', '(:', ')=', ':(', '):', '=)', '(=', ':|', '|:']
    
    def display(self):
        self.operation = None
        self.text_disp = ''
        while 1:
            self.local_header()
            ans = input(f"Operation [{', '.join(self.emojis)}] [+, -]\n > ").lower()
            
            syn_match = re.search(r'([+\-])', ans)
            if not syn_match: continue
            operator = syn_match.group(1)
            operands = ans.split(operator)

            if len(operands)!=2: continue
            elif operator not in '+-': continue
            
            left = operands[0].strip(); right = operands[1].strip()
            if not all(left[a:a+2] in self.emojis for a in range(0, len(left), 2)) or not all(right[a:a+2] in self.emojis for a in range(0, len(right), 2)): continue
            else:
                def operation(a, b, op):
                    match op:
                        case '+': return a+b
                        case '-': return a-b
                
                lnum = int(''.join([str(self.emojis.index(left[a:a+2])) for a in range(0, len(left), 2)]))
                rnum = int(''.join([str(self.emojis.index(right[a:a+2])) for a in range(0, len(right), 2)]))
                self.operation = operation(lnum, rnum, operator)
                self.text_disp = ans
                break
    
    def solve(self):
        self.local_header()
        print(f"Operation: {self.text_disp}")
        print(f"{self.answer_pretext}{self.operation}")