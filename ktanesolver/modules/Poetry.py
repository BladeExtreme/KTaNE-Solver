import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
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
        rcParams['toolbar'] = 'none'

        if not hasattr(self, 'loaded_images'):
            self.loaded_images = {}
            for name in self.friend_list:
                key = name.lower().replace(' ', '_')
                path = f"ktanesolver/resources/Poetry/{key}.png"
                self.loaded_images[key] = mpimg.imread(path)

        while True:
            images = [name.lower().replace(' ', '_') for name in self.friend_list]
            fig, axs = plt.subplots(2, 2, figsize=(6, 6))
            axs = axs.flatten()

            for i, key in enumerate(images):
                ax = axs[i]
                img = self.loaded_images[key]
                ax.imshow(img)
                ax.set_title(f"{self.friend_list[i].capitalize()}", fontsize=8)
                ax.axis('off')
                ax.set_navigate(False)

            for j in range(i + 1, len(axs)):
                axs[j].axis('off')

            self.local_header()
            plt.tight_layout()
            plt.show(block=False)

            ans = input("Character: ").lower()
            friend_lookup = [name.lower() for name in self.friend_list]

            if ans not in friend_lookup:
                plt.close(fig)
                continue
            else:
                self.character = ans
                plt.close(fig)
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