from ..tools.image import img_close, img_open, img_initialize
from .__basemod__ import BaseSolver

class MortalKombat(BaseSolver):
    NAME = 'Mortal Kombat'
    characters_list = ['Johnny Cage','Kano','Liu Kang','Raiden','Scorpion','Sonya Blade','Sub Zero']
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    charactermoves = {
        'johnnycage': ['⇦⇨A', '⇦⇨B', '⇩⇩C', ['⇩⇩⇦C⇧B', '⇦⇦⇦BB⇧', '⇩⇦⇧⇩AB']],
        'kano': ['⇧⇩C', '⇨⇨B', '⇩⇦A', ['A⇩B⇧⇦C', '⇧⇧⇨⇨CB', 'ABC⇦⇦⇧']],
        'liukang': ['⇨⇨C', '⇨⇧A', '⇦⇩B', ['⇩⇨B⇦B⇩', '⇨⇨⇩A⇧C', '⇨⇨⇦⇦⇧A']],
        'raiden': ['⇦⇦B', '⇩⇨A', '⇩⇧C', ['AA⇦⇧⇨B', '⇩⇧⇩⇧BB', 'C⇧⇦AB⇩']],
        'scorpion': ['⇦⇦A', '⇦⇨C', '⇧⇧B', ['⇨⇨⇨BBB', '⇧⇧⇩⇦AC', 'A⇨B⇩C⇩']],
        'sonyablade': ['⇧⇨A', '⇩⇦C', '⇨⇦B', ['⇨⇦⇦⇨CB', '⇩⇧⇨B⇦A', '⇧⇧⇩⇦AC']],
        'subzero': ['⇨⇧B', '⇨⇨A', '⇨⇩C', ['⇦⇧⇨⇩CC', '⇨⇩⇦⇧AA', '⇧⇨A⇦⇧B']]
    }
    whattouse = {
        'johnnycage': [None, [0,2,1], [1,0,2], [2,1,0], [1,2,0], [0,1,2], [2,0,1]],
        'kano': [[2,0,1], None, [1,0,2], [0,1,2], [2,1,0], [1,2,0], [0,2,1]],
        'liukang': [[1,2,0],[0,1,2],None,[2,0,1],[0,2,1],[1,0,2],[2,1,0]],
        'raiden': [[2,1,0],[1,2,0],[0,2,1],None,[2,0,1],[1,0,2],[0,1,2]],
        'scorpion': [[0,1,2],[2,0,1],[1,0,2],[2,1,0],None,[1,2,0],[0,2,1]],
        'sonyablade': [[2,1,0],[1,2,0],[0,2,1],[0,1,2],[2,0,1],None,[1,0,2]],
        'subzero': [[0,2,1],[1,0,2],[2,1,0],[0,1,2],[2,0,1],[1,2,0],None]
    }
    char2idx = {
        'johnnycage': 0, 'kano': 1, 'liukang': 2,
        'raiden': 3, 'scorpion': 4, 'sonyablade': 5,
        'subzero': 6
    }

    def display(self):      
        while True:
            self.local_header()
            img_initialize(self.NAME, self.characters_list, 4, 4)
            img_open()
            ans = input("Player Character [Johnny Cage, Kano, Liu Kang, Raiden, Scorpion, Sonya Blade, Sub Zero]: ").lower()
            character_lookup = [name.lower() for name in self.characters_list]

            if ans not in character_lookup:
                img_close()
                continue
            else:
                self.player = ans.replace(' ', '')
                img_close()
                break
        
        while True:
            self.local_header()
            img_initialize(self.NAME, self.characters_list, 4, 4)
            img_open()
            print(f"Player Character: {self.characters_list[self.char2idx[self.player]]}")
            ans = input(f"Enemy Character [Johnny Cage, Kano, Liu Kang, Raiden, Scorpion, Sonya Blade, Sub Zero]: ").lower()
            character_lookup = [name.lower() for name in self.characters_list]

            if ans not in character_lookup:
                img_close()
                continue
            elif ans==self.player:
                img_close()
                continue
            else:
                self.enemy = ans.replace(' ', '')
                img_close()
                break

    def _calculate(self):
        ans = [self.charactermoves[self.player][a] for a in self.whattouse[self.player][self.char2idx[self.enemy]]]
        ans.append(self.charactermoves[self.player][-1])
        if self.player == 'johnnycage':
            if self.enemy in ['kano', 'liukang', 'raiden']:
                if 'PARALLEL' in self.eg.uniqueports or 'SERIAL' in self.eg.uniqueports: ans[-1] = ans[-1][0]
                elif int(self.eg.sndigit[-1])%2 == 1: ans[-1] = ans[-1][1]
            else:
                if any([a in ['CAR*', 'CLR*', 'MSA*'] for a in self.eg.litind]) or any([a in ['BOB', 'NSA', 'FRK'] for a in self.eg.unlitind]): ans[-1][0]
                elif self.eg.batt%2==0: ans[-1][1]
        elif self.player == 'kano':
            if self.enemy in ['johnnycage', 'liukang', 'raiden']:
                if self.eg.batt-(self.eg.batt-self.eg.hold)*2 > (self.eg.batt-self.eg.hold)*2: ans[-1] = ans[-1][0]
                elif len(self.eg.unlitind)==0: ans[-1]=ans[-1][1]
            else:
                if any([a in ['A','I','U','E','O'] for a in self.eg.snletter]): ans[-1] = ans[-1][0]
                elif 'DVI-D' in self.eg.uniqueports or 'RJ-45' in self.eg.uniqueports: ans[-1] = ans[-1][1]
        elif self.player == 'liukang':
            if self.enemy in ['johnnycage', 'kano', 'raiden']:
                if len(self.eg.litind)>0: ans[-1] = ans[-1][0]
                elif 'STEREO RCA' in self.eg.uniqueports or 'PS/2' in self.eg.uniqueports: ans[-1] = ans[-1][1]
            else:
                if sum([int(a) for a in self.eg.sndigit]) in self.prime: ans[-1] = ans[-1][0]
                elif self.eg.batt-(self.eg.batt-self.eg.hold)*2 == 0: ans[-1] = ans[-1][1]
        elif self.player == 'raiden':
            if self.enemy in ['johnnycage', 'kano', 'liukang']:
                if self.eg.batt<=4: ans[-1] = ans[-1][0]
                elif any([a in ['L','P','T'] for a in self.eg.snletter]): ans[-1] = ans[-1][1]
            else:
                if len(self.eg.ind)==0: ans[-1] = ans[-1][0]
                elif [a for b in self.eg.ports for a in b].count("SERIAL") > 1: ans[-1] = ans[-1][1]
        elif self.player == 'scorpion':
            if self.enemy in ['johnnycage', 'kano', 'liukang']:
                if len([a for b in self.eg.ports for a in b])>3: ans[-1] = ans[-1][0]
                elif (self.eg.batt-self.eg.hold)*2 > self.eg.batt-(self.eg.batt-self.eg.hold)*2: ans[-1] = ans[-1][1]
            else:
                if int(self.eg.sndigit[-1])%2==0: ans[-1] = ans[-1][0]
                elif any([a in ['BOB*', 'FRK*'] for a in self.eg.litind]) or any([a in ['FRQ', 'CAR'] for a in self.eg.unlitind]): ans[-1] = ans[-1][1]
        elif self.player == 'sonyablade':
            if self.enemy in ['johnnycage', 'kano', 'liukang']:
                if len(self.eg.ind) > len([a for b in self.eg.ports for a in b]): ans[-1] = ans[-1][0]
                elif int(self.eg.sndigit[0]) > self.eg.batt: ans[-1] = ans[-1][1]
            else:
                if self.eg.batt > int(self.eg.sndigit[0]): ans[-1] = ans[-1][0]
                elif len([a for b in self.eg.ports for a in b]) > len(self.eg.ind): ans[-1] = ans[-1][1]
        elif self.player == 'subzero':
            if self.enemy in ['johnnycage', 'kano', 'liukang']:
                if sum([int(a) for a in self.eg.sndigit])%3==0: ans[-1] = ans[-1][0]
                elif self.eg.batt==0: ans[-1] = ans[-1][1]
            else:
                if len(self.eg.litind)==0: ans[-1] = ans[-1][0]
                elif 'PARALLEL' in self.eg.uniqueports or 'STEREO RCA' in self.eg.uniqueports: ans[-1] = ans[-1][1]
        if isinstance(ans[-1], list): ans[-1] = ans[-1][2]
        return ans

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Player Character: {self.characters_list[self.char2idx[self.player]]}")
        print(f"Enemy Character: {self.characters_list[self.char2idx[self.enemy]]}")
        print(f"{self.answer_pretext}Use: {', '.join(sol)}")