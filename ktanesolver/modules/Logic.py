from .__basemod__ import BaseSolver

class Logic(BaseSolver):
    NAME = 'Logic'
    operator_list = {
        'AND': lambda x,y: x and y,
        'OR': lambda x,y: x or y,
        'XOR': lambda x,y: x ^ y,
        'NAND': lambda x,y: not(x and y),
        'NOR': lambda x,y: not(x or y),
        'XNOR': lambda x,y: not(x ^ y),
        'IMP': lambda x,y: not(x) or y,
        'IMPBY': lambda x,y: x or not(y)
    }

    def display(self):
        self.logic = []; self.history = []
        self.statement = {
            'A': self.eg.batt==len(self.eg.ind), 'N': self.eg.hold>2,
            'B': len(self.eg.snletter)>len(self.eg.sndigit), 'O': len(self.eg.litind)>0 and len(self.eg.unlitind)>0,
            'C': 'IND' in self.eg.unlitind or 'IND*' in self.eg.litind, 'P': 'PARALLEL' in self.eg.uniqueports,
            'D': 'FRK' in self.eg.unlitind or 'FRK*' in self.eg.litind, 'Q': len([a for b in self.eg.ports for a in b])==2,
            'E': len(self.eg.unlitind)==1, 'R': 'PS/2' in self.eg.uniqueports,
            'F': len(self.eg.uniqueports)>1, 'S': sum([int(a) for a in self.eg.sndigit])>10,
            'G': self.eg.batt>2, 'T': 'MSA' in self.eg.unlitind or 'MSA*' in self.eg.litind,
            'H': self.eg.batt<2, 'U': self.eg.hold==1,
            'I': int(self.eg.sndigit[-1])%2==1, 'V': all([a not in "AIUEO" for a in self.eg.snletter]),
            'J': self.eg.batt>4, 'W': len(self.eg.ind)==0,
            'K': len(self.eg.litind)==1, 'X': len(self.eg.ind)==1,
            'L': len(self.eg.ind)==2, 'Y': len([a for b in self.eg.ports for a in b])>5,
            'M': [a for b in self.eg.ports for a in b]==set([a for b in self.eg.ports for a in b]), 'Z': len([a for b in self.eg.ports for a in b])<2
        }
        while 1:
            self.local_header()
            print(f'''Guide:
 - Use capital letters for variables (e.g., A, B, C)
 - Use a Space between variables and operators (e.g, `A AND B`)
 - DO NOT use a space between:
    - Brackets and their contents (`[A AND B]`)
    - NOT Operator (!) and the variable (`!A`, `!B`)
 - All brackets must be square brackets `[]`
 - Use "!" to represent logical NOT (i.e, `!A` means `NOT A`)
 - Logic symbols are not supported. Use logic operators in full word, which can be seen in the table below''')
            print(f'''
Logic Operators to Gates:
 ∧ - AND         ↓ - NOR
 ∨ - OR          ↔ - XNOR
 ⊻ - XOR         → - IMP
 | - NAND        ← - IMPBY

''')

            ans = input(f"Top Logic: ").upper().split(' ')

            if len(ans)!=5: continue
            if ans[1] not in self.operator_list or ans[3] not in self.operator_list: continue
            elif not ('[' in ans[0] and ']' in ans[2]) and not ('[' in ans[2] and ']' in ans[4]): continue
            elif any(a not in self.statement for a in list(map(lambda x: ''.join(y for y in x if y.isalpha()), [ans[0], ans[2], ans[4]]))): continue
            elif any(a.replace('[','').replace(']','')[0]!='!' for a in [ans[0], ans[2], ans[4]] if len(a.replace('[','').replace(']',''))==2): continue
            else:
                first_open_idx = next((i for i, x in enumerate(ans) if '[' in x), -1)
                last_close_idx = next((i for i, x in reversed(list(enumerate(ans))) if ']' in x), -1)
                logiclist = ans[first_open_idx : last_close_idx + 1]

                if first_open_idx > 0:
                    outer_operator = ans[first_open_idx - 1]
                    if outer_operator=='IMP': outer_operator='IMPBY'
                    elif outer_operator=='IMPBY': outer_operator='IMP'
                    remaining_term = ans[0]
                else:
                    outer_operator = ans[last_close_idx + 1]
                    remaining_term = ans[-1]
                
                logiclist+=[outer_operator, remaining_term]

                logicfunc = ' '.join(logiclist).replace('[', '').replace(']', '').split(' ')
                self.logic.append(logicfunc)
                self.history.append(ans)
                break
        
        while 1:
            self.local_header()
            print(f'''Guide:
 - Use capital letters for variables (e.g., A, B, C)
 - Use a Space between variables and operators (e.g, `A AND B`)
 - DO NOT use a space between:
    - Brackets and their contents (`[A AND B]`)
    - NOT Operator (!) and the variable (`!A`, `!B`)
 - All brackets must be square brackets `[]`
 - Use "!" to represent logical NOT (i.e, `!A` means `NOT A`)
 - Logic symbols are not supported. Use logic operators in full word, which can be seen in the table below''')
            print(f'''
Logic Operators to Gates:
 ∧ - AND         ↓ - NOR
 ∨ - OR          ↔ - XNOR
 ⊻ - XOR         → - IMP
 | - NAND        ← - IMPBY

''')

            print(f"Top Logic: {' '.join(self.history[0])}")
            ans = input(f"Bottom Logic: ").upper().split(' ')

            if len(ans)!=5: continue
            if ans[1] not in self.operator_list or ans[3] not in self.operator_list: continue
            elif not ('[' in ans[0] and ']' in ans[2]) and not ('[' in ans[2] and ']' in ans[4]): continue
            elif any(a not in self.statement for a in list(map(lambda x: ''.join(y for y in x if y.isalpha()), [ans[0], ans[2], ans[4]]))): continue
            elif any(a.replace('[','').replace(']','')[0]!='!' for a in [ans[0], ans[2], ans[4]] if len(a.replace('[','').replace(']',''))==2): continue
            else:
                first_open_idx = next((i for i, x in enumerate(ans) if '[' in x), -1)
                last_close_idx = next((i for i, x in reversed(list(enumerate(ans))) if ']' in x), -1)
                logiclist = ans[first_open_idx : last_close_idx + 1]

                if first_open_idx > 0:
                    outer_operator = ans[first_open_idx - 1]
                    if outer_operator=='IMP': outer_operator='IMPBY'
                    elif outer_operator=='IMPBY': outer_operator='IMP'
                    remaining_term = ans[0]
                else:
                    outer_operator = ans[last_close_idx + 1]
                    remaining_term = ans[-1]
                
                logiclist+=[outer_operator, remaining_term]

                logicfunc = ' '.join(logiclist).replace('[', '').replace(']', '').split(' ')
                self.logic.append(logicfunc)
                self.history.append(ans)
                break
    
    def _calculate(self):
        sol = []
        for a in self.logic:
            sol.append(self.operator_list[a[3]](self.operator_list[a[1]](self.statement[a[0]], self.statement[a[2]]), self.statement[a[4]]))
        return sol

    def solve(self):
        sol = self._calculate()
        self.local_header()

        self.local_header()
        print(f'''Guide:
 - Use capital letters for variables (e.g., A, B, C)
 - Use a Space between variables and operators (e.g, `A AND B`)
 - DO NOT use a space between:
    - Brackets and their contents (`[A AND B]`)
    - NOT Operator (!) and the variable (`!A`, `!B`)
 - All brackets must be square brackets `[]`
 - Use "!" to represent logical NOT (i.e, `!A` means `NOT A`)
 - Logic symbols are not supported. Use logic operators in full word, which can be seen in the table below''')
        print(f'''
Logic Operators to Gates:
 ∧ - AND         ↓ - NOR
 ∨ - OR          ↔ - XNOR
 ⊻ - XOR         → - IMP
 | - NAND        ← - IMPBY

''')

        print(f"Top Logic: {' '.join(self.history[0])}")
        print(f"Bottom Logic: {' '.join(self.history[1])}")
        print(f"{self.answer_pretext}Logics:\n - Top: {str(sol[0])}\n - Bottom: {str(sol[1])}")