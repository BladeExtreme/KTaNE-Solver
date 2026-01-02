from ..tools.image import img_close, img_open, img_initialize
from .__basemod__ import BaseSolver

class Poetry(BaseSolver):
    NAME = 'Poetry'
    friend_list = ['melanie', 'hana', 'lacy', 'jane']
    grid = [
        ['', 'clarity', 'flow', 'fatigue', 'hollow', ''],
        ['energy', 'sunshine', 'ocean', 'reflection', 'identity', 'black'],
        ['crowd', 'heart', 'weather', 'words', 'past', 'solitary'],
        ['relax', 'dance', 'weightless', 'morality', 'gaze', 'failure'],
        ['bunny', 'lovely', 'romance', 'future', 'focus', 'search'],
        ['', 'cookies', 'compassion', 'creation', 'patience', '']
    ]

    def display(self):      
        while True:
            self.local_header()
            img_initialize(self.NAME, self.friend_list, 2, 2)
            img_open()
            ans = input("Character: ").lower()
            friend_lookup = [name.lower() for name in self.friend_list]

            if ans not in friend_lookup:
                img_close()
                continue
            else:
                self.character = ans
                img_close()
                break
        
        while True:
            self.local_header()
            print(f"Character: {self.character.capitalize()}")
            words = [b for c in self.grid for b in c]
            ans = input(f"Words (Seperate with comma space): ").lower().split(', ')

            if len(ans)!=6: continue
            elif any(a not in words for a in ans): continue
            else:
                self.words = ans
                break
    
    def display_2(self):
        while True:
            self.local_header()
            print(f"Character: {self.character.capitalize()}")
            words = [b for c in self.grid for b in c]
            ans = input(f"Words (Seperate with comma space): ").lower().split(', ')

            if len(ans)!=6: continue
            elif any(a not in words for a in ans): continue
            else:
                self.words = ans
                break
    
    def _calculate(self):
        flip = 0
        match self.character:
            case 'melanie': flip = 0
            case 'hana': flip = 1
            case 'lacy': flip = 2
            case 'jane': flip = 3
        grid = self.grid.copy(); flatten_grid = []
        for _ in range(flip): grid = [list(row) for row in zip(*reversed(grid))]
        for d in range(11):
            for r in range(6):
                c = d-r
                if 0 <= c < 6:
                    flatten_grid.append(grid[r][c])
        return flatten_grid[min(flatten_grid.index(a) for a in self.words)]

    def solve(self):
        for a in range(3):
            self.local_header()
            sol = self._calculate()
            print(f"STAGE {a+1}")
            print(f"{self.answer_pretext}{sol.capitalize()}")
            if a<2: input(); self.display_2()