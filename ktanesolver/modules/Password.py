from .__basemod__ import BaseSolver
import colorama as c

class Password(BaseSolver):
    NAME = 'Password'
    bank = ["about","after","again","below","could","every","first","found","great","house","large","learn","never","other","place","plant","point","right","small","sound","spell","still","study","their","there","these","thing","think","three","water","where","which","world","would","write"]

    def display(self, bad=False):
        ans = []
        
        for x in range(5):
            self.local_header()
            if bad: print(c.Fore.RED+"NO SOLUTION"+c.Style.RESET_ALL+' - Try inputting the letters again to find the correct solution')
            print(f"Possible letters for each column (Newline represents columns, each letter separated by comma space. Enter '-' to stop inputting):")
            for z in range(len(ans)):
                print(f"> {', '.join(ans[z]).upper()}")
            temp_ans = input(f"> ").lower().split(', ')

            if temp_ans == ['-'] and len(ans)>0: break
            elif len(temp_ans)!=5: continue
            elif not all(a.isalpha() for a in temp_ans): continue
            else: ans.append(temp_ans)
        
        self.local_header()
        print(f"Possible letters for each column (Newline represents columns, each letter separated by comma space. Enter '-' to stop inputting):")
        for z in range(len(ans)):
            print(f"> {', '.join(ans[z]).upper()}")
        self.ans = ans
    
    def _calculate(self):
        candidates = [a for a in self.bank if a[0] in self.ans[0]]
        for i in range(1, len(self.ans)):
            candidates = [a for a in candidates if a[i] in self.ans[i]]
            if len(candidates)==0:
                return None
        if len(candidates)==0: return None
        return ', '.join(candidates)

    def solve(self):
        ans = self._calculate()
        
        while ans is None:
            self.display(True)
            ans = self._calculate()

        print(f"{self.answer_pretext}Possible Words: {ans}")