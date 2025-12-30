from .__basemod__ import BaseSolver

class ColoredButtons(BaseSolver):
    NAME = 'Colored Buttons'

    def display(self):
        pass

    def _calculate(self):
        ispresent = lambda x: x in self.eg.ind or x+'*' in self.eg.ind

        if ispresent('SND'): return 'Red'
        elif ispresent('CLR'): return 'Orange'
        elif ispresent('CAR'): return 'Yellow'
        elif ispresent('IND'): return 'Green'
        elif ispresent('FRQ'): return 'Blue'
        elif ispresent('SIG'): return 'Cyan'
        elif ispresent('NSA'): return 'Purple'
        elif ispresent('MSA'): return 'Magenta'
        elif ispresent('TRN'): return 'Brown'
        elif ispresent('BOB'): return 'Tan'
        elif ispresent('FRK'): return 'Grey'
        else: return 'Black'

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}{sol}")