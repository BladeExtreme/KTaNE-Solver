from .__basemod__ import BaseSolver
import colorama as c
import heapq

class MysticSquare(BaseSolver):
    NAME = 'Mystic Square'
    table = [
        [1, 3, 5, 4, 6, 7, 2, 8],
        [2, 5, 7, 3, 8, 1, 4, 6],
        [6, 4, 8, 1, 7, 3, 5, 2],
        [8, 1, 2, 5, 3, 4, 6, 7],
        [3, 2, 6, 8, 4, 5, 7, 1],
        [7, 6, 1, 2, 5, 8, 3, 4],
        [4, 7, 3, 6, 1, 2, 8, 5],
        [5, 8, 4, 7, 2, 6, 1, 3]
    ]

    def display(self):
        self.grid = [-1 for a in range(9)]
        stage = 0

        while stage<8:
            grid = [
                [f"╔═══╦","═══╦","═══╗"],
                [f"║ {' ' if self.grid[0]==-1 else str(self.grid[0])} ║",f" {' ' if self.grid[1]==-1 else str(self.grid[1])} ║",f" {' ' if self.grid[2]==-1 else str(self.grid[2])} ║"],
                [f"╠═══╬","═══╬","═══╣"],
                [f"║ {' ' if self.grid[3]==-1 else str(self.grid[3])} ║",f" {' ' if self.grid[4]==-1 else str(self.grid[4])} ║",f" {' ' if self.grid[5]==-1 else str(self.grid[5])} ║"],
                [f"╠═══╬","═══╬","═══╣"],
                [f"║ {' ' if self.grid[6]==-1 else str(self.grid[6])} ║",f" {' ' if self.grid[7]==-1 else str(self.grid[7])} ║",f" {' ' if self.grid[8]==-1 else str(self.grid[8])} ║"],
                [f"╚═══╩","═══╩","═══╝"]
            ]
            self.local_header()
            for a in grid:
                print(''.join(a))
            
            print(f"Number on each grid [1-8, 0 if empty] (In reading order. Each number represent single grid, separated by space. Each line represent rows): ")
            for a in range(len(self.grid)):
                if self.grid[a]!=-1:
                    if a%3==0: print(f"> ", end="")
                    print(self.grid[a], end=" ")
                    if a%3==2: print()
            ans = input(f"> ").lower().split(' ')

            if len(ans)!=3: continue
            elif not all(a.isdigit() for a in ans): continue
            elif not all(int(a) in range(0,9) for a in ans): continue
            elif len(set(ans))!=3: continue
            elif any(int(a) in self.grid for a in ans): continue
            else:
                self.grid[stage:stage+3] = list(map(lambda x: int(x), ans))
                stage+=3
    
    def _findskull(self):
        state = 0 if any(self.grid[a] in list(map(lambda x: int(x), self.eg.sndigit)) for a in range(0,9,2)) else 1
        using = self.table[self.grid[4]-1] if state==0 else [self.table[a][self.grid[4]-1] for a in range(8)]
        node = self.grid.index(0)

        def is_on_edge(n):
            edges = {
                'l': n%3==0,
                'r': n%3==2,
                't': n<3,
                'b': n>=6
            }
            return edges

        for a in using:
            edge_c = is_on_edge(node)
            neighbors = []

            if not edge_c['l']: neighbors.append(self.grid[node-1])
            if not edge_c['r']: neighbors.append(self.grid[node+1])
            if not edge_c['t']: neighbors.append(self.grid[node-3])
            if not edge_c['b']: neighbors.append(self.grid[node+3])

            if a in neighbors:
                node = self.grid.index(a)
        return self.grid[node]

    def _calculate(self):
        target = [1, 2, 3, 4, 5, 6, 7, 8, 0]

        def is_on_edge(n):
            return {
                'l': n % 3 == 0,
                'r': n % 3 == 2,
                't': n < 3,
                'b': n >= 6
            }

        def heuristic(grid):
            return sum(grid[i] == target[i] for i in range(9))

        queue = []
        heapq.heappush(queue, (-heuristic(self.grid), self.grid, []))
        visited = set()

        while queue:
            _, curr_grid, path = heapq.heappop(queue)

            if curr_grid == target:
                return path

            key = tuple(curr_grid)
            if key in visited:
                continue
            visited.add(key)

            zero = curr_grid.index(0)
            edges = is_on_edge(zero)

            def add_move(offset):
                new_grid = curr_grid.copy()
                move_val = new_grid[zero + offset]
                new_grid[zero], new_grid[zero + offset] = new_grid[zero + offset], new_grid[zero]
                heapq.heappush(queue, (-heuristic(new_grid), new_grid, path + [move_val]))

            if not edges['l']: add_move(-1)
            if not edges['r']: add_move(1)
            if not edges['t']: add_move(-3)
            if not edges['b']: add_move(3)

    def solve(self):
        sol = self._findskull()
        grid = [
            ["╔═══╦", "═══╦", "═══╗"],
            [f"║ {c.Fore.RED + str(self.grid[0]) + c.Style.RESET_ALL if self.grid[0] != -1 and self.grid[0] == sol else ' ' if self.grid[0] == -1 else str(self.grid[0])} ║",
            f" {c.Fore.RED + str(self.grid[1]) + c.Style.RESET_ALL if self.grid[1] != -1 and self.grid[1] == sol else ' ' if self.grid[1] == -1 else str(self.grid[1])} ║",
            f" {c.Fore.RED + str(self.grid[2]) + c.Style.RESET_ALL if self.grid[2] != -1 and self.grid[2] == sol else ' ' if self.grid[2] == -1 else str(self.grid[2])} ║"],
            ["╠═══╬", "═══╬", "═══╣"],
            [f"║ {c.Fore.RED + str(self.grid[3]) + c.Style.RESET_ALL if self.grid[3] != -1 and self.grid[3] == sol else ' ' if self.grid[3] == -1 else str(self.grid[3])} ║",
            f" {c.Fore.RED + str(self.grid[4]) + c.Style.RESET_ALL if self.grid[4] != -1 and self.grid[4] == sol else ' ' if self.grid[4] == -1 else str(self.grid[4])} ║",
            f" {c.Fore.RED + str(self.grid[5]) + c.Style.RESET_ALL if self.grid[5] != -1 and self.grid[5] == sol else ' ' if self.grid[5] == -1 else str(self.grid[5])} ║"],
            ["╠═══╬", "═══╬", "═══╣"],
            [f"║ {c.Fore.RED + str(self.grid[6]) + c.Style.RESET_ALL if self.grid[6] != -1 and self.grid[6] == sol else ' ' if self.grid[6] == -1 else str(self.grid[6])} ║",
            f" {c.Fore.RED + str(self.grid[7]) + c.Style.RESET_ALL if self.grid[7] != -1 and self.grid[7] == sol else ' ' if self.grid[7] == -1 else str(self.grid[7])} ║",
            f" {c.Fore.RED + str(self.grid[8]) + c.Style.RESET_ALL if self.grid[8] != -1 and self.grid[8] == sol else ' ' if self.grid[8] == -1 else str(self.grid[8])} ║"],
            ["╚═══╩", "═══╩", "═══╝"]
        ]
        self.local_header()
        for a in grid:
            print(''.join(a))
        print(f"Number on each grid: ")
        for a in range(len(self.grid)):
            if self.grid[a]!=-1:
                if a%3==0: print(f"> ", end="")
                print(self.grid[a], end=" ")
                if a%3==2: print()
        print(f"{self.answer_pretext}Skull under the number: {sol}")

        input()
        stage = 0
        self.grid = [-1 for a in range(9)]

        while stage<8:
            grid = [
                [f"╔═══╦","═══╦","═══╗"],
                [f"║ {' ' if self.grid[0]==-1 else str(self.grid[0])} ║",f" {' ' if self.grid[1]==-1 else str(self.grid[1])} ║",f" {' ' if self.grid[2]==-1 else str(self.grid[2])} ║"],
                [f"╠═══╬","═══╬","═══╣"],
                [f"║ {' ' if self.grid[3]==-1 else str(self.grid[3])} ║",f" {' ' if self.grid[4]==-1 else str(self.grid[4])} ║",f" {' ' if self.grid[5]==-1 else str(self.grid[5])} ║"],
                [f"╠═══╬","═══╬","═══╣"],
                [f"║ {' ' if self.grid[6]==-1 else str(self.grid[6])} ║",f" {' ' if self.grid[7]==-1 else str(self.grid[7])} ║",f" {' ' if self.grid[8]==-1 else str(self.grid[8])} ║"],
                [f"╚═══╩","═══╩","═══╝"]
            ]
            
            self.local_header()
            for a in grid:
                print(''.join(a))
            print(f"New Numbers on each grid [1-8, 0 if empty] (In reading order. Each number represent single grid, separated by space. Each line represent rows): ")
            for a in range(len(self.grid)):
                if self.grid[a]!=-1:
                    if a%3==0: print(f"> ", end="")
                    print(self.grid[a], end=" ")
                    if a%3==2: print()
            ans = input(f"> ").lower().split(' ')

            if len(ans)!=3: continue
            elif not all(a.isdigit() for a in ans): continue
            elif not all(int(a) in range(0,9) for a in ans): continue
            elif len(set(ans))!=3: continue
            elif any(int(a) in self.grid for a in ans): continue
            else:
                self.grid[stage:stage+3] = list(map(lambda x: int(x), ans))
                stage+=3
        
        sol = self._calculate()
        grid = [
            [f"╔═══╦","═══╦","═══╗"],
            [f"║ {' ' if self.grid[0]==-1 else str(self.grid[0])} ║",f" {' ' if self.grid[1]==-1 else str(self.grid[1])} ║",f" {' ' if self.grid[2]==-1 else str(self.grid[2])} ║"],
            [f"╠═══╬","═══╬","═══╣"],
            [f"║ {' ' if self.grid[3]==-1 else str(self.grid[3])} ║",f" {' ' if self.grid[4]==-1 else str(self.grid[4])} ║",f" {' ' if self.grid[5]==-1 else str(self.grid[5])} ║"],
            [f"╠═══╬","═══╬","═══╣"],
            [f"║ {' ' if self.grid[6]==-1 else str(self.grid[6])} ║",f" {' ' if self.grid[7]==-1 else str(self.grid[7])} ║",f" {' ' if self.grid[8]==-1 else str(self.grid[8])} ║"],
            [f"╚═══╩","═══╩","═══╝"]
        ]
        
        self.local_header()
        for a in grid:
            print(''.join(a))
        print(f"New Numbers on each grid: ")
        for a in range(len(self.grid)):
            if self.grid[a]!=-1:
                if a%3==0: print(f"> ", end="")
                print(self.grid[a], end=" ")
                if a%3==2: print()
        print(f"{self.answer_pretext}Press these numbers: {', '.join(list(map(str, sol)))}")