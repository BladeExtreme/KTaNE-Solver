from .__basemod__ import BaseSolver
import math

class Pathfinder(BaseSolver):
    NAME = 'Pathfinder'

    def __init__(self, edgework):
        self.grid = []
        self.display()
        self.solve()
        input()

    def display(self):
        while 1:
            self.local_header()
            ans = input("Grid (Top left to bottom right, columns are separated by spaces, rows are separated by lines):\n").split(' ')

            if len(ans)!=4: continue
            elif not all(x.isdigit() for x in ans): continue
            elif ans[0]=='0' and len(self.grid)==0: continue
            else:
                self.grid.append([int(x) for x in ans])
                if len(self.grid)==4: break

    def _calculate(self):
        def heuristic(node, grid):
            return max(
                sum(v for row in grid for v in row),
                abs(node[0]-3) + abs(node[1]-3)
            )

        def dfs(node, path, grid):
            x, y = node
            s_r = sum(v for row in grid for v in row)
            g = len(path)
            h = heuristic(node, grid)
            f = g + h
            min_excess = math.inf
            
            if f > bound: return f
            if (s_r % 2) != ((abs(x - 3) + abs(y - 3)) % 2): return math.inf
            if node == (3, 3) and s_r == 0: return path

            moves = []
            if y > 0: moves.append(("Up", (x, y - 1)))
            if x < 3: moves.append(("Right", (x + 1, y)))
            if y < 3: moves.append(("Down", (x, y + 1)))
            if x > 0: moves.append(("Left", (x - 1, y)))
            moves.sort(
                key=lambda m: grid[m[1][1]][m[1][0]],
                reverse=True
            )

            for move, (nx, ny) in moves:
                if grid[ny][nx] == 0:
                    continue
                new_grid = [row[:] for row in grid]
                new_grid[ny][nx] -= 1
                result = dfs((nx, ny), path + [move], new_grid)
                if isinstance(result, list):
                    return result
                min_excess = min(min_excess, result)
            return min_excess
        
        bound = heuristic(tuple([0, 0]), self.grid)
        while 1:
            t = dfs(tuple([0, 0]), [], self.grid)
            if isinstance(t, list): return ', '.join(t)
            if t == math.inf: return None
            bound = t

    def solve(self):
        ans = self._calculate()
        self.local_header()
        print(f"Grid: ")
        for a in self.grid:
            print(' '.join(str(z) for z in a))
        print(f"{self.answer_pretext}Move: {ans}")