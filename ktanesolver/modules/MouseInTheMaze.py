import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
from .__basemod__ import BaseSolver

class MouseInTheMaze(BaseSolver):
    NAME = 'Mouse in the Maze'
    maze_list = list('123456')

    def load_maze(self):
        mazes = [
            [
                [11, 10, 8, 10, 12, 11, 8, 10, 10, 12],
                [13, 13, 2, 12, 3, 14, 5, 8, 10, 6],
                [5, 1, 12, 3, 10, 10, 6, 1, 10, 12],
                [5, 5, 1, 10, 10, 12, 9, 4, 13, 5],
                [3, 6, 5, 9, 12, 5, 5, 5, 3, 6],
                [9, 10, 6, 5, 1, 2, 6, 3, 10, 12],
                [5, 9, 8, 6, 3, 10, 12, 9, 10, 6],
                [5, 5, 1, 10, 10, 12, 3, 2, 10, 12],
                [5, 7, 5, 13, 11, 6, 8, 10, 10, 6],
                [3, 10, 6, 3, 10, 10, 2, 10, 10, 14]
            ],[
                [9, 10, 12, 9, 10, 10, 14, 9, 10, 12],
                [3, 12, 5, 3, 8, 8, 10, 6, 9, 6],
                [13, 5, 3, 10, 4, 1, 12, 11, 2, 12],
                [5, 3, 8, 10, 6, 7, 1, 12, 9, 6],
                [3, 12, 3, 10, 8, 14, 5, 5, 3, 12],
                [9, 6, 9, 8, 6, 9, 6, 1, 10, 4],
                [3, 10, 4, 3, 10, 4, 11, 2, 12, 5],
                [9, 12, 3, 10, 14, 5, 9, 8, 6, 7],
                [5, 3, 10, 10, 10, 6, 5, 5, 11, 12],
                [3, 10, 10, 10, 10, 10, 6, 3, 10, 6]
            ],[
                [9, 10, 10, 12, 9, 8, 10, 12, 9, 14],
                [3, 10, 14, 1, 4, 5, 9, 6, 3, 12],
                [9, 10, 10, 4, 7, 5, 7, 13, 9, 6],
                [5, 9, 10, 6, 9, 2, 10, 6, 3, 12],
                [5, 3, 10, 10, 0, 10, 10, 8, 10, 6],
                [3, 10, 10, 12, 5, 9, 12, 5, 9, 14],
                [9, 10, 10, 4, 5, 7, 5, 5, 3, 12],
                [5, 9, 12, 5, 3, 10, 6, 3, 12, 5],
                [5, 7, 5, 5, 9, 12, 9, 12, 3, 4],
                [3, 10, 6, 3, 6, 3, 6, 3, 10, 6]
            ],[
                [9, 10, 10, 12, 9, 10, 10, 8, 10, 12],
                [5, 9, 10, 4, 5, 9, 10, 6, 13, 5],
                [5, 3, 14, 3, 6, 1, 8, 12, 1, 6],
                [3, 10, 10, 10, 12, 5, 5, 3, 6, 13],
                [9, 14, 11, 12, 5, 5, 3, 10, 10, 4],
                [5, 9, 10, 6, 5, 3, 10, 10, 12, 5],
                [3, 0, 10, 10, 6, 9, 14, 9, 6, 5],
                [9, 2, 10, 8, 12, 3, 10, 2, 10, 4],
                [5, 9, 12, 5, 5, 9, 12, 9, 10, 6],
                [3, 6, 3, 6, 3, 6, 3, 2, 10, 14]
            ],[
                [9, 10, 10, 10, 12, 13, 9, 10, 10, 12],
                [1, 10, 10, 12, 3, 6, 1, 10, 12, 5],
                [3, 10, 12, 3, 10, 10, 6, 13, 5, 7],
                [9, 8, 6, 9, 10, 10, 10, 6, 1, 12],
                [5, 1, 10, 6, 11, 12, 9, 14, 5, 5],
                [5, 5, 9, 10, 12, 5, 5, 9, 6, 5],
                [5, 5, 3, 12, 5, 1, 6, 5, 11, 6],
                [5, 3, 10, 6, 5, 5, 9, 4, 9, 12],
                [1, 10, 10, 10, 6, 5, 5, 5, 5, 5],
                [3, 10, 10, 10, 10, 2, 6, 3, 6, 7]
            ],[
                [9, 12, 11, 8, 10, 12, 9, 10, 10, 12],
                [5, 5, 9, 6, 9, 6, 3, 12, 9, 4],
                [5, 3, 6, 9, 2, 10, 8, 6, 5, 5],
                [1, 12, 11, 2, 12, 9, 6, 9, 6, 5],
                [7, 5, 9, 8, 4, 1, 10, 6, 9, 6],
                [9, 4, 7, 5, 5, 3, 12, 11, 6, 13],
                [5, 3, 10, 6, 3, 12, 3, 12, 13, 5],
                [5, 9, 14, 9, 10, 2, 12, 5, 3, 4],
                [5, 3, 12, 3, 10, 12, 5, 3, 10, 4],
                [3, 10, 2, 10, 10, 6, 3, 10, 10, 6]
            ]
        ]
        pass

    def display(self):
        rcParams['toolbar'] = 'none'
        if not hasattr(self, 'loaded_images'):
            self.loaded_images = {}
            for name in self.maze_list:
                key = name.lower().replace(' ', '_')
                path = f"ktanesolver/resources/MouseInTheMaze/{key}.png"
                self.loaded_images[key] = mpimg.imread(path)

        while 1:
            images = [name.lower().replace(' ', '_') for name in self.maze_list]
            fig, axs = plt.subplots(3, 2, figsize=(6, 6))
            axs = axs.flatten()

            for i, key in enumerate(images):
                ax = axs[i]
                img = self.loaded_images[key]
                ax.imshow(img)
                ax.set_title(f"Maze #{self.maze_list[i].capitalize()}", fontsize=8)
                ax.axis('off')
                ax.set_navigate(False)

            for j in range(i + 1, len(axs)):
                axs[j].axis('off')

            self.local_header()
            plt.tight_layout()
            plt.show(block=False)

            ans = input(f"Maze Number: ").lower()

            if not ans.isdigit():
                plt.close(fig)
                continue
            elif int(ans) not in range(1, 7):
                plt.close(fig)
                continue
            else:
                self.maze = ans
                plt.close(fig)
                break
        
        while 1:
            pass

        pass