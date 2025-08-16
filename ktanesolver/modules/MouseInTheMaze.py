import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
from .__basemod__ import BaseSolver

class MouseInTheMaze(BaseSolver):
    NAME = 'Mouse in the Maze'
    maze_list = list('123456')
    sphere_dict = [
        {'blue':'white', 'yellow':'yellow', 'white':'green', 'green':'blue'},
        {'yellow':'blue', 'white':'yellow', 'blue':'white', 'green':'green'},
        {'white':'green', 'blue':'yellow', 'green':'blue', 'yellow':'white'},
        {'white':'blue', 'yellow':'yellow', 'blue':'green', 'green':'white'},
        {'white':'yellow', 'green':'white', 'yellow':'blue', 'blue':'green'},
        {'white':'blue', 'blue':'green', 'green':'yellow', 'yellow':'white'}
    ]
    sphere_pos = [
        {'green': [2,2], 'blue': [7,2], 'white': [2,7], 'yellow': [7,7]},
        {'white': [2,2], 'yellow': [7,2], 'blue': [2,7], 'green': [7,7]},
        {'green': [2,2], 'blue': [7,2], 'yellow': [2,7], 'white': [7,7]},
        {'yellow': [2,2], 'white': [7,2], 'green': [2,7], 'blue': [7,7]},
        {'yellow': [2,2], 'green': [7,2], 'blue': [2,7], 'white': [7,7]}
    ]
    mazes = [
        [
            [11, 10, 8, 10, 12, 11, 8, 10, 10, 12],
            [13, 13, 3, 12, 3, 14, 5, 8, 10, 6],
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

    def to_middle(self):
        looking = 'U'
        queue = [[self.starting_position, looking, []]]
        vis = set()
        goal = {(4,4),(4,5),(5,4),(5,5)}

        while queue:
            node, look, path = queue.pop(0)

            if tuple(node) in vis: continue
            vis.add(tuple(node))
            if tuple(node) in goal: return path, node, look

            wall = bin(self.mazes[self.maze-1][node[1]][node[0]])[2:].zfill(4)
            neighbors = [a for a in range(4) if wall[a] != '1']

            for x in neighbors:
                if x == 0:
                    new_node = [node[0], node[1]-1]
                    if look == 'R': move = 'LF'
                    elif look == 'L': move = 'RF'
                    elif look == 'D': move = 'RRF'
                    else: move = 'F'
                    new_look = 'U'
                elif x == 1:
                    new_node = [node[0]+1, node[1]]
                    if look == 'R': move = 'F'
                    elif look == 'L': move = 'RRF'
                    elif look == 'D': move = 'LF'
                    else: move = 'RF'
                    new_look = 'R'
                elif x == 2:
                    new_node = [node[0], node[1]+1]
                    if look == 'R': move = 'RF'
                    elif look == 'L': move = 'LF'
                    elif look == 'D': move = 'F'
                    else: move = 'RRF'
                    new_look = 'D'
                else:  # x == 3
                    new_node = [node[0]-1, node[1]]
                    if look == 'R': move = 'RRF'
                    elif look == 'L': move = 'F'
                    elif look == 'D': move = 'RF'
                    else: move = 'LF'
                    new_look = 'L'

                new_path = path + [move]
                queue.append([new_node, new_look, new_path])
        return None


    def display(self):
        rcParams['toolbar'] = 'none'
        if not hasattr(self, 'loaded_images'):
            self.loaded_images = {}
            for name in self.maze_list:
                key = name.lower().replace(' ', '[')
                path = f"ktanesolver/resources/MouseInTheMaze/{key}.png"
                self.loaded_images[key] = mpimg.imread(path)

        while 1:
            images = [name.lower().replace(' ', '[') for name in self.maze_list]
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

            ans = input(f"Maze Number: #").lower()

            if not ans.isdigit():
                plt.close(fig)
                continue
            elif int(ans) not in range(1, 7):
                plt.close(fig)
                continue
            else:
                self.maze = int(ans)
                plt.close(fig)
                break
        
        while 1:
            self.local_header()
            print(f"Maze Number: #{self.maze}")
            fig = plt.figure(figsize=(4, 4))
            ax = fig.add_subplot(111)
            
            img = self.loaded_images[str(self.maze)]
            ax.imshow(img)
            ax.set_title(f"Maze #{self.maze}")
            
            rows, cols = img.shape[0], img.shape[1]
            n_rows, n_cols = 10, 10

            ax.set_xticks([(i+0.5) * cols / n_cols for i in range(n_cols)])
            ax.set_xticklabels([chr(65 + i) for i in range(n_cols)])
            ax.xaxis.tick_top()

            ax.set_yticks([(i+0.5) * rows / n_rows for i in range(n_rows)])
            ax.set_yticklabels([str(i+1) for i in range(n_rows)])

            ax.set_xticks([i * cols / n_cols for i in range(n_cols+1)], minor=True)
            ax.set_yticks([i * rows / n_rows for i in range(n_rows+1)], minor=True)
            ax.grid(which="minor", color="black", linewidth=0.5)

            plt.show(block=False)

            ans = input("Starting Position (Letter first, the number. E.g. A1): ").upper()

            if len(ans)!=2:
                plt.close(fig)
                continue
            elif not (ans[0].isalpha() and ans[1].isdigit()):
                plt.close(fig)
                continue
            elif ans[0] not in 'ABCDEFGHI':
                plt.close(fig)
                continue
            elif ans[1] not in '123456789':
                plt.close(fig)
                continue
            else:
                self.starting_position = [ord(ans[0]) - ord('A'), int(ans[1]) - 1]
                plt.close(fig)
                break

        sol, last_coord, last_look = self.to_middle()

        while 1:
            self.local_header()
            print(f"Maze Number: #{self.maze}")
            print(f"Starting Position: {''.join([chr(self.starting_position[0] + ord('A')), str(self.starting_position[1] + 1)])}")
            print(f"{self.answer_pretext}Path to Middle (R means look right, L means look left, F means forward):\n {', '.join(sol)}")
            print()
            ans = input(f"Torus Color (Blue, Yellow, White, Green): ").lower()

            if ans not in ['blue', 'yellow', 'white', 'green']: continue
            else:
                self.torus_color = ans
                self.last_coord = last_coord
                self.last_look = last_look
                break
    
    def _calculate(self):
        queue = [[self.last_coord, self.last_look, []]]
        goal = self.sphere_pos[self.maze-1][self.sphere_dict[self.maze-1][self.torus_color]]
        vis = set()

        while queue:
            node, look, path = queue.pop(0)

            if tuple(node) in vis: continue
            vis.add(tuple(node))
            if node==goal: return path

            wall = bin(self.mazes[self.maze-1][node[1]][node[0]])[2:].zfill(4)
            neighbors = [a for a in range(4) if wall[a] != '1']

            for x in neighbors:
                if x == 0:
                    new_node = [node[0], node[1]-1]
                    if look == 'R': move = 'LF'
                    elif look == 'L': move = 'RF'
                    elif look == 'D': move = 'RRF'
                    else: move = 'F'
                    new_look = 'U'
                elif x == 1:
                    new_node = [node[0]+1, node[1]]
                    if look == 'R': move = 'F'
                    elif look == 'L': move = 'RRF'
                    elif look == 'D': move = 'LF'
                    else: move = 'RF'
                    new_look = 'R'
                elif x == 2:
                    new_node = [node[0], node[1]+1]
                    if look == 'R': move = 'RF'
                    elif look == 'L': move = 'LF'
                    elif look == 'D': move = 'F'
                    else: move = 'RRF'
                    new_look = 'D'
                else:
                    new_node = [node[0]-1, node[1]]
                    if look == 'R': move = 'RRF'
                    elif look == 'L': move = 'F'
                    elif look == 'D': move = 'RF'
                    else: move = 'LF'
                    new_look = 'L'

                new_path = path + [move]
                queue.append([new_node, new_look, new_path])


    def solve(self):
        sol = self._calculate()

        self.local_header()
        print(f"Maze Number: #{self.maze}")
        print(f"Starting Position: {''.join([chr(self.starting_position[0] + ord('A')), str(self.starting_position[1] + 1)])}")
        print(f"Torus Color: {self.torus_color}")
        print(f"{self.answer_pretext}Path to Goal (R means look right, L means look left, F means forward):\n {', '.join(sol)}")
        pass