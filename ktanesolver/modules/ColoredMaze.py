from .__basemod__ import BaseSolver

class ColoredMaze(BaseSolver):
    NAME = 'Colored Maze'

    def display(self):
        pass

    def _calculate(self):
        table = [
            ['OR', 'OOR', 'GBP', 'BP'],
            ['OOR', 'BOOR', 'RBBP', 'BBP'],
            ['OPGR', 'PYBP', 'PPYBP', 'GOO'],
            ['BP', 'YBP', 'YPPYBP', 'OO']
        ]
        row = int(self.eg.sndigit[0])%4
        col = int(ord(self.eg.snletter[0])-ord('A')+1)%4
        col_dic = {
            'R': 'Red',
            'O': 'Orange',
            'Y': 'Yellow',
            'G': 'Green',
            'B': 'Blue',
            'P': 'Purple'
        }

        return [col_dic[a] for a in table[row][col]]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}{', '.join(a.capitalize() for a in sol)}")