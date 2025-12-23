from .__basemod__ import BaseSolver

class EpelleMoiCa(BaseSolver):
    NAME = 'EpelleMoiCa'
    bank = ['abasourdi', 'aberrant', 'abrasive', 'acatalectique', 'accueil','acrobatie', 'aligot', 'amphigourique', 'analgésiante', 'antipasti','apparition', 'approvisionnement', 'aptonyme', 'axolotl', 'aïeux','baril', 'bedonnant', 'berlingot', 'burlesque', 'canneberge','capharnaüm', 'caravansérail', 'cassis', 'cathéter', 'chiffonnade','chrysanthème', 'coccyx', 'croquignolesque', 'curcubitacé', 'dichotomie','dictionnaire', 'ecchymose', 'effiloche', 'équilatéral', 'équinoxe','éraflure', 'gourgandine', 'gringalet', 'hallogène', 'histrion','hortillonnage', 'hurluberlu', 'hypothétique', 'hébéphrénie', 'idylle','incarcération', 'inexorable', 'iridescent', 'kamoulox', 'kérosène','lagéniforme', 'luthérien', 'maelström', 'mirliflore', 'myxomatose','méningocoque', 'neurasthénique', 'nihilisme', 'nonobstant', 'œuvre','omniprésence', 'oxymore', 'paillette', 'palefrenière', 'personnalité','plexiglas', 'pluviôse', 'polymnie', 'polysyndète', 'popeline','presbytère', 'profession', 'pâmoison', 'péjorative', 'péroné','pérégrination', 'quadripède', 'quenouillon', 'quetsche', 'quolibet','remembrance', 'rhododendron', 'serpillère', 'spleen', 'sycophante','syllepse', 'syllogisme', 'terminus', 'thyroïde', 'thébaïde','torréfaction', 'ubiquité', 'vagabond', 'vertèbre', 'victuaille','virevolte', 'véracité', 'ytterbium', 'zeugma', 'ziggurat']

    def display(self):
        while 1:
            submit = False; play = False
            self.local_header()
            for y in range(20):
                for x in range(5):
                    try:
                        text = f"{str((y+1)+(x*20)).zfill(2)}. {self.bank[(y+1)+(x*20)]}"
                        print(text, end=" "*(30-len(text)))
                    except: pass
                print()
            print()
            print(f"Enter Command:\n - Input 'Submit #' with # substituted with a number from the options above to submit the audio\n - Input 'Play #' with # substituted with a number from the options above to play an audio using pygame.")
            ans = input(f"cmd > ").lower().split(' ')

            if len(ans)!=2: continue
            elif ans[0] not in ['submit', 'play']: continue
            elif not ans[1].isdigit(): continue
            elif int(ans[1]) not in range(1, len(self.bank)+1): continue
            else:
                self.answer = int(ans[1])
                if ans[0]=='submit':
                    break
                else:
                    self.playAudio()
        
    def _calculate(self):
        print(self.answer)
        return self.bank[self.answer].upper()

    def solve(self):
        sol = self._calculate()
        self.local_header()
        for y in range(20):
            for x in range(5):
                try:
                    text = f"{str((y+1)+(x*20)).zfill(2)}. {self.bank[(y+1)+(x*20)]}"
                    print(text, end=" "*(30-len(text)))
                except: pass
            print()
        print()
        print(f"Enter Command:\n - Input 'Submit #' with # substituted with a number from the options above to submit the audio\n - Input 'Play #' with # substituted with a number from the options above to play an audio using pygame.")
        print(f"cmd/Listening > submit {str(self.bank[self.answer])}\n")
        print(f"{self.answer_pretext}{sol}")
    
    def playAudio(self):
        pass