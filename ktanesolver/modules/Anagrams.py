from .__basemod__ import BaseSolver

class Anagrams(BaseSolver):
    NAME = 'Anagrams'
    bank = {
        tuple(sorted({'s', 'm', 'e', 'r', 'a', 't'})): ['stream', 'master', 'tamers'],
        tuple(sorted({'l', 'o', 'e', 'p', 'd'})): ['looped', 'poodle', 'pooled'],
        tuple(sorted({'l', 'e', 'r', 'a', 'c'})): ['cellar', 'caller', 'recall'],
        tuple(sorted({'s', 'e', 'a', 't', 'd'})): ['seated', 'sedate', 'teased'],
        tuple(sorted({'s', 'u', 'e', 'r', 'c'})): ['rescue', 'secure', 'recuse'],
        tuple(sorted({'s', 'e', 'r', 'a', 'h'})): ['rashes', 'shears', 'shares'],
        tuple(sorted({'b', 'l', 'e', 'y', 'r', 'a'})): ['barely', 'barley', 'bleary'],
        tuple(sorted({'s', 'u', 'e', 'r', 't', 'd'})): ['duster', 'rusted', 'rudest']
    }

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Word: ").lower()
            
            if len(ans)!=6: continue
            elif tuple(sorted(set(ans))) not in self.bank.keys(): continue
            else:
                self.word = ans
                break
    
    def _calculate(self):
        return self.bank[tuple(sorted(set(self.word)))]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Word: {self.word}")
        print(f"{self.answer_pretext}{', '.join([a.capitalize() for a in sol if a!=self.word])}")