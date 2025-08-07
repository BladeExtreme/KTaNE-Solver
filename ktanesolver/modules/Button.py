from .__basemod__ import BaseSolver

class Button(BaseSolver):
    NAME = 'The Button'
    
    def display(self):
        while 1:
            self.local_header()
            ans = input("Button Color [Blue, Red, Yellow, White]: ").lower()
            if not ans.isalpha(): continue
            elif ans not in ['blue','red','yellow','white']: continue
            else:
                self.color = ans
                break
        
        while 1:
            self.local_header()
            print(f"Button Color: {self.color.capitalize()}")
            ans = input("Button Label [Detonate, Press, Hold, Abort]: ").lower()
            if not ans.isalpha(): continue
            elif ans not in ['detonate', 'press', 'hold', 'abort']: continue
            else:
                self.label = ans
                break
    
    def _calculate(self):
        if self.color=='blue' and self.label=='abort': return 'HOLD'
        elif self.eg.batt>1 and self.label=='detonate': return 'TAP'
        elif self.color=='white' and 'CAR*' in self.eg.litind: return 'HOLD'
        elif self.eg.batt>=2 and 'FRK*' in self.eg.litind: return 'TAP'
        elif self.color=='yellow': return 'HOLD'
        elif self.color=='red' and self.label=='hold': return 'TAP'
        else: return 'HOLD'

    def solve(self):
        ans = self._calculate()
        if ans=='TAP':
            self.local_header()
            print(f"Button Color: {self.color.capitalize()}")
            print(f"Button Label: {self.label.capitalize()}\n")
            print(f"{self.answer_pretext}Tap")
            return
        elif ans=='HOLD':
            while 1:
                self.local_header()
                print(f"Button Color: {self.color.capitalize()}")
                print(f"Button Label: {self.label.capitalize()}")
                print(f"{self.answer_pretext}Hold\n\n")
                ans2 = input(f"Strip Color [Blue, White, Yellow, Other]: ").lower()

                if not ans2.isalpha():
                    continue
                elif ans2 not in ['blue','white','yellow','other']: continue

                self.local_header()
                print(f"Button Color: {self.color.capitalize()}")
                print(f"Button Label: {self.label.capitalize()}")
                print(f"{self.answer_pretext}Hold\n\n")
                print(f"Strip Color: {ans2.capitalize()}")

                if ans2=='blue': print(f"{self.answer_pretext}Release when 4 is in the countdown timer")
                elif ans2=='yellow': print(f"{self.answer_pretext}Release when 5 is in the countdown timer")
                else: print(f"{self.answer_pretext}Release when 1 is in the countdown timer")
                break
            return