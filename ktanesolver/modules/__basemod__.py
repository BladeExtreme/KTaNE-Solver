from ..other.header import header
from ..edgework import Edgework
import colorama as c #type: ignore
import keyboard as kb

c.init(autoreset=True)

class BaseSolver:
    NAME = ''
    answer_pretext = c.Fore.GREEN+'ANSWER'+c.Style.RESET_ALL+' - '
    fail_pretext = c.Fore.RED+'ERROR'+c.Style.RESET_ALL+' - '

    def local_header(self):
        header()
        print(f"Solver - {self.NAME}\n")

    def __init__(self, edgework:Edgework):
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def display(self):
        pass

    def solve(self):
        pass

    def _calculate(self):
        pass

    def resolve(self):
        pass