from .__basemod__ import BaseSolver

class LuckyDice(BaseSolver):
    NAME = 'Lucky Dice'
    flag = False; purple_flag = None; yellow_flag = None; complete_flag = False
    iteration = 0; state = [True, True, True]
        
    def intiative(self):
        die = []
        while True:
            self.local_header()
            print(f"ITERATION: {self.iteration}")
            print(f"Guide:\n - There 3 dies on the module with different colors.\n - Input the color of each die in any order, but no duplicate colors are allowed\n - The acceptable colors are: [Red, Pink, Purple, Orange, Yellow, Cyan, Blue, White, Gray, Black]\n - After initializing the color of each die, you will be asked to input the number of each die.\n - The acceptable numbers are: [1, 2, 3, 4, 5, 6]\n")
            for a in range(len(die)):
                print(f"{str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th')}'s die color: {die[a].capitalize()}")
            ans = input(f"{str(len(die)+1)+('st' if len(die)==0 else 'nd' if len(die)==1 else 'rd' if len(die)==2 else 'th')}'s die color: ").lower()

            if ans not in ['red', 'pink', 'purple', 'orange', 'yellow', 'cyan', 'blue', 'white', 'gray', 'black']: continue
            elif ans in die: continue
            else:
                die.append(ans)
                if len(die)==3:
                    self.die = die
                    break
    
    def display(self):
        if not self.flag:
            self.intiative()
            self.flag = True
        rolls = []
        while True:
            self.local_header()
            print(f"ITERATION: {self.iteration}")
            print(f"Guide:\n - There 3 dies on the module with different colors.\n - Input the color of each die in any order, but no duplicate colors are allowed\n - The acceptable colors are: [Red, Pink, Purple, Orange, Yellow, Cyan, Blue, White, Gray, Black]\n - After initializing the color of each die, you will be asked to input the number of each die.\n - The acceptable numbers are: [1, 2, 3, 4, 5, 6]\n")
            for a in range(len(self.die)):
                print(f"{str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th')}'s die color: {self.die[a].capitalize()}")
            print()
            for a in range(len(rolls)):
                print(f"{str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th')}'s die roll: {rolls[a]}")
            ans = input(f"{str(len(rolls)+1)+('st' if len(rolls)==0 else 'nd' if len(rolls)==1 else 'rd' if len(rolls)==2 else 'th')}'s die roll: ").lower()

            if not ans.isdigit(): continue
            elif int(ans) not in range(1, 7): continue
            else:
                rolls.append(int(ans))
                if len(rolls)==3:
                    self.rolls = rolls
                    break
        self.full_dice = {a: b for a, b in zip(self.die, self.rolls)}

    def _calculate(self):
        def red():
            return all(self.full_dice['red'] > self.full_dice[a] for a in self.full_dice.keys() if a!='red')
        def pink():
            return self.full_dice['pink']%2==1
        def purple():
            if self.purple_flag is None:
                self.purple_flag = self.full_dice['purple']%2
                return False
            elif self.purple_flag!=self.full_dice['purple']%2: return True
            else:
                self.purple_flag = self.full_dice['purple']%2
                return False
        def orange():
            return any(self.full_dice['orange'] > self.full_dice[a] for a in self.full_dice.keys() if a!='orange')
        def yellow():
            if self.yellow_flag is None:
                self.yellow_flag = self.full_dice['yellow']
                return False
            elif self.full_dice['yellow']==(7-self.yellow_flag): return True
            else:
                self.yellow_flag = self.full_dice['yellow']
                return False
        def cyan():
            return len(self.full_dice['cyan'] > self.full_dice[a] for a in self.full_dice.keys() if a!='cyan')==1
        def blue():
            return self.full_dice['blue']%2==0
        def white():
            return all(self.full_dice['white'] < self.full_dice[a] for a in self.full_dice.keys() if a!='white')
        def gray():
            if self.full_dice['gray']==1: return True
            else: return all(self.full_dice['red'] > self.full_dice[a] for a in self.full_dice.keys() if a!='red')
        def black():
            return self.full_dice['black'] in [2,3,5]

        funcdict = {
            'red': red,
            'pink': pink,
            'purple': purple,
            'orange': orange,
            'yellow': yellow,
            'cyan': cyan,
            'blue': blue,
            'white': white,
            'gray': gray,
            'black': black
        }

        ans = []
        for a in self.full_dice.keys():
            ans.append(funcdict[a]())
            if self.state[self.die.index(a)]!=False:
                self.state[self.die.index(a)] = funcdict[a]()

        if self.state.count(True)==1: self.complete_flag = True
        return self.state.index(True)

    def solve(self):
        while True:
            sol = self._calculate()
            self.local_header()
            print(f"ITERATION: {self.iteration}")
            print(f"Guide:\n - There 3 dies on the module with different colors.\n - Input the color of each die in any order, but no duplicate colors are allowed\n - The acceptable colors are: [Red, Pink, Purple, Orange, Yellow, Cyan, Blue, White, Gray, Black]\n - After initializing the color of each die, you will be asked to input the number of each die.\n - The acceptable numbers are: [1, 2, 3, 4, 5, 6]\n")
            for a in range(len(self.die)):
                print(f"{str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th')}'s die color: {self.die[a].capitalize()}")
            print()
            for a in range(len(self.rolls)):
                print(f"{str(a+1)+('st' if a==0 else 'nd' if a==1 else 'rd' if a==2 else 'th')}'s die roll: {self.rolls[a]}")
            print(f"\n{self.answer_pretext}{'Roll again' if self.complete_flag is False else 'Press the '+self.die[sol].capitalize()+' die.'}")
            if self.complete_flag: break
            else:
                input()
                self.iteration+=1
                self.display()