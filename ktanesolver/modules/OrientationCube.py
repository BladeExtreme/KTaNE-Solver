from .__basemod__ import BaseSolver

class OrientationCube(BaseSolver):
    NAME = 'Orientation Cube'

    def display(self):
        self.temp = False
        while 1:
            self.local_header()
            ans = input(f"Eye Position [Front, Right, Back, Left]: ").lower()

            if ans not in ['front', 'right', 'back', 'left']: continue
            else:
                self.eye = ans
                break
    
    def prompt(self, temp:dict[list]):
        self.temp = True
        while 1:
            self.local_header()
            print(f"Eye Position: {self.eye.capitalize()}")
            print(f"{self.answer_pretext}Move: Clockwise")
            print()
            
            ans = input(f"New Eye Position [{', '.join(list(map(lambda x: x.capitalize(), list(temp.keys()))))}]: ").lower()

            if ans not in list(temp.keys()): continue
            else:
                self.neweye = ans
                break
        return temp[self.neweye]
    
    def _calculate(self):
        if 'R' in self.eg.snletter:
            match self.eye:
                case 'front': return ['Clockwise']
                case 'right': return ['Left', 'Counter-clockwise']
                case 'back': return ['Counter-clockwise']
                case 'left': return ['Left', 'Clockwise']
        elif 'TRN' in self.eg.unlitind or 'TRN*' in self.eg.litind:
            match self.eye:
                case 'front': return ['Counter-clockwise']
                case 'right': return ['Clockwise', 'Right']
                case 'back': return ['Clockwise']
                case 'left': return ['Clockwise', 'Left']
        elif 'PS/2' in self.eg.uniqueports or self.eg.strikes>0:
            match self.eye:
                case 'front': return ['Counter-clockwise', 'Left']
                case 'right': return ['Left', 'Clockwise']
                case 'back': return ['Clockwise', 'Left']
                case 'left': return ['Left', 'Counter-clockwise']
        elif '7' in self.eg.sndigit or '8' in self.eg.sndigit:
            match self.eye:
                case 'front': return ['Clockwise', 'Left', 'Left']
                case 'right': return ['Right', 'Clockwise', 'Right']
                case 'back': return ['Counter-clockwise', 'Left', 'Left']
                case 'left': return ['Right', 'Counter-clockwise', 'Right']
        elif self.eg.batt>=3 or self.eye=='left':
            match self.eye:
                case 'front': return self.prompt({'left': ['Right', 'Counter-clockwise'], 'front': ['Clockwise'], 'right': ['Right', 'Clockwise']})
                case 'right': return self.prompt({'front': ['Left', 'Clockwise'], 'right': ['Clockwise'], 'back': ['Left', 'Counter-clockwise']})
                case 'back': return self.prompt({'right': ['Left', 'Clockwise'], 'back': ['Clockwise'], 'left': ['Left', 'Counter-clockwise']})
                case 'left': return self.prompt({'front': ['Left', 'Counter-clockwise'], 'left': ['Clockwise'], 'back': ['Left', 'Clockwise']})
        else:
            match self.eye:
                case 'front': return ['Counter-clockwise']
                case 'right': return ['Clockwise', 'Right']
                case 'back': return ['Clockwise']

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Eye Position: {self.eye.capitalize()}")
        if self.temp:
            print(f"{self.answer_pretext}Move: Clockwise")
            print()
            print(f"New Eye Position: {self.neweye.capitalize()}")
        print(f"{self.answer_pretext}Move: {', '.join(sol)}")