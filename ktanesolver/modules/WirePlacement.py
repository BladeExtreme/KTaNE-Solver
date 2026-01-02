from .__basemod__ import BaseSolver

class WirePlacement(BaseSolver):
    NAME = 'Wire Placement'
    table = {
        "yellow": {'black': ['d2', 'a3', 'd1'], 'blue': ['d1', 'c3', 'a1'], 'red': ['d2', 'a2', 'b2'], 'white': ['a2', 'a4', 'b4'], 'yellow': ['d1', 'a3', 'a4']},
        "blue": {'black': ['a2','c3'], 'blue': ['c4','c2'], 'red': ['a1','c1'], 'white': ['c4','d3'], 'yellow': ['d4','b1']},
        "white": {'black': ['d3','b2'], 'blue': ['d2','c1'], 'red': ['d4','b4'], 'white': ['b3','a1'], 'yellow': ['b2','c1']},
        "red": {'black': ['a1','c4'], 'blue': ['c3','d3'], 'red': ['c4','b1'], 'white': ['b2','c1'], 'yellow': ['b3','c2']},
        "black": {'black': ['b1'], 'blue': ['d4'], 'red': ['a4'], 'white': ['d2'], 'yellow': ['b4']}
    }

    def display(self):      
        wires = []; locations = []
        while True:
            self.local_header()
            print(f"Guide:\n - Enter all wires' information: colors and their locations.\n - To input, write down the color first and then the 2 locations, all of them are seperated by a space.\n - To enter location, enter the 2 grid's location where the wire is in.\n - To notate the location for a wire, write the letter (column) and then the number (row).\n - Wire whose location already existed on the input before will not be accepted.\n - Acceptable colors are: [Red, Yellow, Blue, White, Black]\n - Acceptable letters are: [A, B, C, D]\n - Acceptable numbers are: [1, 2, 3, 4]\n - Example: Red A2 B2\n")
            for a in wires:
                print(f" > {' '.join(_.capitalize() for _ in a)}")
            ans = input(f" > ").lower().split(' ')

            if len(ans) != 3: continue
            elif ans[0] not in ['red', 'yellow', 'blue', 'white', 'black']: continue
            elif any(x not in ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2', 'a3', 'b3', 'c3', 'd3', 'a4', 'b4', 'c4', 'd4'] for x in ans[1:]): continue
            elif any(x in locations for x in ans[1:]): continue
            else:
                wires.append(ans)
                locations.append(ans[1])
                locations.append(ans[2])
                if len(locations)==16:
                    self.wires = wires
                    break

    def _calculate(self):
        cut = []; c3wire = [a[0] for a in self.wires if 'c3' in a[1:]][0]
        for a in self.wires:
            print([b for b in a[1:]], a[0], self.table[a[0]][c3wire])
            if any([b in self.table[a[0]][c3wire] for b in a[1:]]):
                cut.append(tuple([a[0], tuple(a[1:])]))
        return cut

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Guide:\n - Enter all wires' information: colors and their locations.\n - To input, write down the color first and then the 2 locations, all of them are seperated by a space.\n - To enter location, enter the 2 grid's location where the wire is in.\n - To notate the location for a wire, write the letter (column) and then the number (row).\n - Wire whose location already existed on the input before will not be accepted.\n - Acceptable colors are: [Red, Yellow, Blue, White, Black]\n - Acceptable letters are: [A, B, C, D]\n - Acceptable numbers are: [1, 2, 3, 4]\n - Example: Red A2 B2\n")
        for a in self.wires:
            print(f" > {' '.join(_.capitalize() for _ in a)}")
        print(f"\n{self.answer_pretext}Cut:")
        for a in sol:
            print(f" > {a[0].capitalize()} wire in [{', '.join(x.capitalize() for x in a[1])}]")