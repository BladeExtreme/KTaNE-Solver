from .__basemod__ import BaseSolver

class DivisibleNumbers(BaseSolver):
    NAME = 'Divisible Numbers'
    num_list = []; starting_time = None; stage = 1

    def display(self):
        while True:
            self.local_header()
            print(f"STAGE {self.stage}")
            ans = input(f"Number on Screen: ").lower()

            if not ans.isdigit(): continue
            else:
                self.number = int(ans)
                self.num_list.append(self.number)
                break
        
        if self.starting_time is None:
            while True:
                self.local_header()
                print(f"STAGE {self.stage}")
                print(f"Number on Screen: {self.number}")
                ans = input(f"Starting Bomb Time (in minutes): ")

                if not ans.isdigit(): continue
                elif int(ans) < 0: continue
                else:
                    self.starting_time = int(ans)
                    break

    def _calculate(self):
        def process(n):
            if self.eg.batt >= 3: return n%3==0
            elif len(self.eg.litind)>len(self.eg.unlitind): return n%9==0
            elif self.num_list[0]<1000: return n%6==0
            elif self.starting_time<10: return n%4==0
            elif int(self.eg.sndigit[-1])%2==0: return n%2==0
            elif self.eg.modules>10: return n%5==0
            else: return n%10==0
        
        return process(self.number)


    def solve(self):
        for a in range(3):
            sol = self._calculate()
            self.local_header()
            print(f"STAGE {self.stage}")
            print(f"{self.answer_pretext}Press {'Red' if not sol else 'Green'} button.")
            if self.stage==3: break
            input(); self.stage+=1; self.display()