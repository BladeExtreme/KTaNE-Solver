from .__basemod__ import BaseSolver

class ColoredSquares(BaseSolver):
    NAME = 'Colored Squares'
    table = [
        ['blue', 'column', 'red', 'yellow', 'row', 'green', 'magenta'],
        ['row', 'green', 'blue', 'magenta', 'red', 'column', 'yellow'],
        ['yellow', 'magenta', 'green', 'row', 'blue', 'red', 'column'],
        ['blue', 'green', 'yellow', 'column', 'red', 'row', 'magenta'],
        ['yellow', 'row', 'blue', 'magenta', 'column', 'red', 'green'],
        ['magenta', 'red', 'yellow', 'green', 'column', 'blue', 'row'],
        ['green', 'row', 'column', 'blue', 'magenta', 'yellow', 'red'],
        ['magenta', 'red', 'green', 'blue', 'yellow', 'column', 'row'],
        ['column', 'yellow', 'red', 'green', 'row', 'magenta', 'blue'],
        ['green', 'column', 'row', 'red', 'magenta', 'blue', 'yellow'],
        ['red', 'yellow', 'row', 'column', 'green', 'magenta', 'blue'],
        ['column', 'blue', 'magenta', 'red', 'yellow', 'row', 'green'],
        ['row', 'magenta', 'column', 'yellow', 'blue', 'green', 'red'],
        ['red', 'blue', 'magenta', 'row', 'green', 'yellow', 'column'],
        ['column', 'row', 'column', 'row', 'column', 'row', 'column']
    ]
    column_index = {
        'red': 0, 'blue': 1, 'green': 2,
        'yellow': 3, 'magenta': 4, 'row': 5,
        'column': 6
    }

    def display(self):
        while True:
            self.local_header()
            ans = input("Color of the Fewest Squares [Red, Blue, Green, Yellow, Magenta]: ").lower()

            if not ans.isalpha(): continue
            elif ans not in ['red','blue','green','yellow','magenta']: continue
            else:
                self.color = ans
                self.total = 1
                break
    
    def _calculate(self):
        return self.table[self.total-1][self.column_index[self.color]]

    def solve(self):
        while self.total!=16:
            sol = self._calculate()
            self.local_header()
            print(f"Color Pressed: {self.color.capitalize()}")
            print(f"Total Pressed: {self.total}\n")
            print(f"{self.answer_pretext}Press: {sol.capitalize()}")
            ans = input(f"New Total Pressed: ").lower()

            if not ans.isdigit(): continue
            elif int(ans)<self.total or int(ans)>16: continue
            else:
                self.total = int(ans)
                self.color = sol
        
        self.local_header()
        print(f"Color Pressed: {self.color}")
        print(f"Total Pressed: {self.total}\n")
        print(f"{self.answer_pretext}Finished, proceed back to the menu.")