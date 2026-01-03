from .__basemod__ import BaseSolver

class SimonStates(BaseSolver):
    NAME = 'Simon States'
    priority = {
        'red': ['red','blue','green','yellow'],
        'yellow': ['blue','yellow','red','green'],
        'green': ['green','red','yellow','blue'],
        'blue': ['yellow','green','blue','red']
    }
    flashes = []; pressed = []; dominant = None

    def display(self):
        if self.dominant is None:
            while True:
                self.local_header()
                ans = input(f"Dominant Color (Top Right) [Red, Blue, Green, Yellow]: ").lower()

                if ans not in ['red','blue','yellow','green']: continue
                else:
                    self.dominant = ans
                    break
        
        while True:
            self.local_header()
            print(f"Dominant Color: {self.dominant.capitalize()}")
            print(f"Flashed Color (Separate with a comma space) [Red, Blue, Green, Yellow]: ")
            for a in self.flashes:
                print(f" > {', '.join(map(lambda x: x.capitalize(), a))}")
            ans = input(f" > ").lower().split(', ')

            if len(ans) not in range(1,5): continue
            elif not all(a in ['red','blue','yellow','green'] for a in ans): continue
            elif len(set(ans))!=len(ans): continue
            else:
                self.flashes.append(ans)
                break
    
    def _calculate(self):
        stage = len(self.flashes)

        match stage:
            case 1:
                if len(self.flashes[stage-1])==1: return self.flashes[stage-1][0]
                elif len(self.flashes[stage-1])==2 and 'blue' in self.flashes[stage-1]: return self.priority[self.dominant][0]
                elif len(self.flashes[stage-1])==2: return 'blue'
                elif len(self.flashes[stage-1])==3 and 'red' in self.flashes[stage-1]: return self.priority[self.dominant][-1]
                elif len(self.flashes[stage-1])==3: return 'red'
                else: return self.priority[self.dominant][1]
            case 2:
                if sorted(['red','blue'])==self.flashes[stage-1]: return [a for a in self.priority[self.dominant] if a not in self.flashes][0]
                elif len(self.flashes[stage-1])==2: return [a for a in self.priority[self.dominant][::-1] if a not in self.flashes][0]
                elif len(self.flashes[stage-1])==1 and 'blue' not in self.flashes[stage-1]: return 'blue'
                elif len(self.flashes[stage-1])==1: return 'yellow'
                elif len(self.flashes[stage-1])==4: return self.pressed[0]
                else: return [a for a in self.priority[self.dominant] if a not in self.flashes][0]
            case 3:
                if len(self.flashes[stage-1])==3 and any(a in self.pressed for a in self.flashes[stage-1]): return [a for a in self.priority[self.dominant] if a not in self.flashes[stage-1] and a not in self.pressed][0]
                elif len(self.flashes[stage-1])==3: return self.priority[self.dominant][0]
                elif len(self.flashes[stage-1])==2 and all(a in self.pressed for a in self.flashes[stage-1]): return [a for a in self.priority[self.dominant] if a not in self.flashes[stage-1] and a not in self.pressed][0]
                elif len(self.flashes[stage-1])==2: return self.pressed[0]
                elif len(self.flashes[stage-1])==1: return self.flashes[stage-1][0]
                else: return self.priority[self.dominant][-2]
            case 4:
                if len(set(self.pressed))==3: return [a for a in self.priority[self.dominant] if a not in self.pressed][0]
                elif len(self.flashes[stage-1])==3 and any(a not in self.pressed for a in self.priority[self.dominant] if a not in self.flashes[stage-1]): return [a for a in self.priority[self.dominant] if a not in self.flashes[stage-1]][0]
                elif len(self.flashes[stage-1])==3: return self.priority[self.dominant][-1]
                elif len(self.flashes[stage-1])==1: return self.flashes[stage-1][0]
                else: return 'green'

    def solve(self):
        while True:
            sol = self._calculate()
            self.pressed.append(sol)
            self.local_header()
            print(f"Dominant Color: {self.dominant.capitalize()}")
            print(f"Flashed Color:")
            for a in range(len(self.flashes)):
                print(f" > {', '.join(map(lambda x: x.capitalize(), self.flashes[a]))}")
            print(f"\n{self.answer_pretext}Press - {', '.join(map(lambda x: x.capitalize(), self.pressed))}")
            if len(self.pressed)!=4:
                print(f"lol: {len(self.pressed)}")
                input()
                self.display()
            else:
                break