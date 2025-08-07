from .__basemod__ import BaseSolver

class Maze(BaseSolver):
    NAME = 'Maze'

    def __init__(self, edgework):
        self.hint = None; self.target = None; self.player = None; self.maze_to_use = None
        self.maze_disp = [
            [
                ['     ', '  A  ', '  B  ', '  C  ', '  D  ', '  E  ', '  F  ', '     '],
                ['    ╔', '═════', '═════', '═════', '═════', '═════', '═════', '╗    ']
            ],
            [
                [' 1  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],
            [
                ['    ║', '     ', '     ', '     ', '     ', '     ', '     ', '║    '],
                [' 2  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],
            [
                ['    ║', '     ', '     ', '     ', '     ', '     ', '     ', '║    '],
                [' 3  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],
            [
                ['    ║', '     ', '     ', '     ', '     ', '     ', '     ', '║    '],
                [' 4  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],
            [
                ['    ║', '     ', '     ', '     ', '     ', '     ', '     ', '║    '],
                [' 5  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],
            [
                ['    ║', '     ', '     ', '     ', '     ', '     ', '     ', '║    '],
                [' 6  ║', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '  ●  ', '║    '],
            ],[
                ['    ╚', '═════', '═════', '═════', '═════', '═════', '═════', '╝    '],
                ['     ', '     ', '     ', '     ', '     ', '     ', '     ', '     '],
            ]
        ]
        self.mazes = [
            [
                [9, 10, 12, 9, 10, 14],
                [5, 9, 6, 3, 10, 12],
                [5, 3, 12, 9, 10, 4],
                [5, 11, 2, 6, 11, 4],
                [1, 10, 12, 9, 14, 5],
                [3, 14, 3, 6, 11, 6]
            ],[
                [11, 8, 14, 9, 8, 14],
                [9, 6, 9, 6, 3, 12],
                [5, 9, 6, 9, 10, 4],
                [1, 6, 9, 6, 13, 5],
                [5, 13, 5, 9, 6, 5],
                [7, 3, 6, 3, 10, 6]
            ],[
                [9, 10, 12, 13, 9, 12],
                [7, 13, 5, 3, 6, 5],
                [9, 4, 5, 9, 12, 5],
                [5, 5, 5, 5, 5, 5],
                [5, 3, 6, 5, 5, 5],
                [3, 10, 10, 6, 3, 6]
            ],[
                [9, 12, 11, 10, 10, 12],
                [5, 5, 9, 10, 10, 4],
                [5, 3, 6, 9, 14, 5],
                [5, 11, 10, 2, 10, 4],
                [1, 10, 10, 10, 12, 5],
                [3, 10, 14, 11, 6, 7]
            ],[
                [11, 10, 10, 10, 8, 12],
                [9, 10, 10, 8, 6, 7],
                [1, 12, 11, 6, 9, 12],
                [5, 3, 10, 12, 7, 5],
                [5, 9, 10, 2, 14, 5],
                [7, 3, 10, 10, 10, 6]
            ],[
                [13, 9, 12, 11, 8, 12],
                [5, 5, 5, 9, 6, 5],
                [1, 6, 7, 5, 9, 6],
                [3, 12, 9, 4, 5, 13],
                [9, 6, 7, 5, 3, 4],
                [3, 10, 10, 6, 11, 6]
            ],[
                [9, 10, 10, 12, 9, 12],
                [5, 9, 14, 3, 6, 5],
                [3, 6, 9, 14, 9, 6],
                [9, 12, 1, 10, 6, 13],
                [5, 7, 3, 10, 12, 5],
                [3, 10, 10, 10, 2, 6]
            ],[
                [13, 9, 10, 12, 9, 12],
                [1, 2, 14, 3, 6, 5],
                [5, 9, 10, 10, 12, 5],
                [5, 3, 12, 11, 2, 6],
                [5, 13, 3, 10, 10, 14],
                [3, 2, 10, 10, 10, 14]
            ],[
                [13, 9, 10, 10, 8, 12],
                [5, 5, 9, 14, 5, 5],
                [1, 2, 6, 9, 6, 5],
                [5, 13, 9, 6, 11, 4],
                [5, 5, 5, 9, 12, 5],
                [3, 6, 3, 6, 3, 6]
            ]
        ]
        self.hint_coords = [
            [{'x': 0, 'y': 1}, {'x': 5, 'y': 2}],
            [{'x': 1, 'y': 3}, {'x': 4, 'y': 1}],
            [{'x': 3, 'y': 3}, {'x': 5, 'y': 3}],
            [{'x': 0, 'y': 0}, {'x': 0, 'y': 3}],
            [{'x': 3, 'y': 5}, {'x': 4, 'y': 2}],
            [{'x': 2, 'y': 4}, {'x': 4, 'y': 0}],
            [{'x': 1, 'y': 0}, {'x': 1, 'y': 5}],
            [{'x': 2, 'y': 3}, {'x': 3, 'y': 0}],
            [{'x': 0, 'y': 4}, {'x': 2, 'y': 1}]
        ]
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def show_maze(self):
        for a in range(len(self.maze_disp)):
            for b in range(len(self.maze_disp[a])):
                print(''.join(self.maze_disp[a][b]))

    def display(self):
        while 1:
            self.local_header()
            self.show_maze()
            ans = input("Hints (White Circles) (Seperated by comma space, 2 coordinates): ").lower().split(', ')

            if len(ans)!=2: continue
            elif not all([len(a)==2 for a in ans]): continue
            elif not (any([a.isalpha() for a in ans[0]]) and any([a.isdigit() for a in ans[0]])) or not (any([a.isalpha() for a in ans[1]]) and any([a.isdigit() for a in ans[1]])): continue
            elif not int(''.join([a for a in ans[0] if a.isdigit()])) in range(1,7) or not int(''.join([a for a in ans[1] if a.isdigit()])) in range(1,7): continue
            elif not all([a in 'abcdef' for a in ans[0] if a.isalpha()]) or not all([a in 'abcdef' for a in ans[0] if a.isalpha()]): continue
            elif [a for a in ans[0] if a.isalpha()]==[a for a in ans[1] if a.isalpha()] and [a for a in ans[0] if a.isdigit()]==[a for a in ans[1] if a.isdigit()]: continue
            else:
                self.hint = [
                    {'x': int([ord(a) for a in ans[0] if a.isalpha()][0])-int(ord('a')), 'y': int([a for a in ans[0] if a.isdigit()][0])-1, },
                    {'x': int([ord(a) for a in ans[1] if a.isalpha()][0])-int(ord('a')), 'y': int([a for a in ans[1] if a.isdigit()][0])-1, }
                ]
                if not any(sorted(sublist, key=lambda d: (d['x'], d['y'])) == sorted(self.hint, key=lambda d: (d['x'], d['y'])) for sublist in self.hint_coords): continue
                else:
                    self.maze_to_use = [sorted(sublist, key=lambda d: (d['x'], d['y'])) == sorted(self.hint, key=lambda d: (d['x'], d['y'])) for sublist in self.hint_coords].index(True)
                    break
        
        while 1:
            self.local_header()
            self.show_maze()
            print(f"Hints (White Circles): {'ABCDEF'[self.hint[0]['x']]+str(self.hint[0]['y']+1)}, {'ABCDEF'[self.hint[1]['x']]+str(self.hint[1]['y']+1)}")
            ans = input("Target (Red Triangle): ").lower()

            if len(ans)!=2: continue
            elif not (any([a.isalpha() for a in ans]) and any([a.isdigit() for a in ans])): continue
            elif not int(''.join([a for a in ans if a.isdigit()])) in range(1,7): continue
            elif not all([a in 'abcdef' for a in ans if a.isalpha()]): continue
            else:
                self.target = {
                    'x': int(ord([a for a in ans if a.isalpha()][0]))-int(ord('a')),
                    'y': int([a for a in ans if a.isdigit()][0])-1
                }
                break
        
        while 1:
            self.local_header()
            self.show_maze()
            print(f"Hints (White Circles): {'ABCDEF'[self.hint[0]['x']]+str(self.hint[0]['y']+1)}, {'ABCDEF'[self.hint[1]['x']]+str(self.hint[1]['y']+1)}")
            print(f"Target (Red Triangle): {'ABCDEF'[self.target['x']]+str(self.target['y']+1)}")
            ans = input("Player (White Square): ").lower()

            if len(ans)!=2: continue
            elif not (any([a.isalpha() for a in ans]) and any([a.isdigit() for a in ans])): continue
            elif not int(''.join([a for a in ans if a.isdigit()])) in range(1,7): continue
            elif not all([a in 'abcdef' for a in ans if a.isalpha()]): continue
            else:
                self.player = {
                    'x': int(ord([a for a in ans if a.isalpha()][0]))-int(ord('a')),
                    'y': int([a for a in ans if a.isdigit()][0])-1
                }
            break

        self.local_header()
        self.show_maze()
        print(f"Hints (White Circles): {'ABCDEF'[self.hint[0]['x']]+str(self.hint[0]['y']+1)}, {'ABCDEF'[self.hint[1]['x']]+str(self.hint[1]['y']+1)}")
        print(f"Target (Red Triangle): {'ABCDEF'[self.target['x']]+str(self.target['y']+1)}")
        print(f"Player (White Square): {'ABCDEF'[self.player['x']]+str(self.player['y']+1)}")
    
    def _calculate(self):
        queue = [[tuple([self.player['x'], self.player['y']]), []]]
        vis = set()

        while 1:
            node, path = queue.pop(0)
            if node in vis: continue
            elif node==tuple([self.target['x'], self.target['y']]): return ', '.join(path)
            else:
                vis.add(node)
                walls = bin(self.mazes[self.maze_to_use][node[1]][node[0]])[2:].zfill(4)
                
                if walls[0]=='0': queue.append([tuple([node[0], node[1]-1]), path+['Up']])
                if walls[1]=='0': queue.append([tuple([node[0]+1, node[1]]), path+['Right']])
                if walls[2]=='0': queue.append([tuple([node[0], node[1]+1]), path+['Down']])
                if walls[3]=='0': queue.append([tuple([node[0]-1, node[1]]), path+['Left']])

    def solve(self):
        ans = self._calculate()
        self.local_header()
        self.show_maze()
        print(f"Hints (White Circles): {'ABCDEF'[self.hint[0]['x']]+str(self.hint[0]['y']+1)}, {'ABCDEF'[self.hint[1]['x']]+str(self.hint[1]['y']+1)}")
        print(f"Target (Red Triangle): {'ABCDEF'[self.target['x']]+str(self.target['y']+1)}")
        print(f"Player (White Square): {'ABCDEF'[self.player['x']]+str(self.player['y']+1)}")
        print(f"{self.answer_pretext}Move: {ans}")