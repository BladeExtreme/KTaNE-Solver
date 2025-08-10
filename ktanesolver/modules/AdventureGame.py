from .__basemod__ import BaseSolver

class AdventureGame(BaseSolver):
    NAME = 'Adventure Game'
    enemylist = {
        'demon': {'str': 50, 'dex': 50, 'int': 50},
        'dragon': {'str': 10, 'dex': 11, 'int': 13},
        'eagle': {'str': 4, 'dex': 7, 'int': 3},
        'goblin': {'str': 3, 'dex': 6, 'int': 5},
        'golem': {'str': 9, 'dex': 4, 'int': 7},
        'troll': {'str': 8, 'dex': 5, 'int': 4},
        'lizard': {'str': 4, 'dex': 6, 'int': 3},
        'wizard': {'str': 4, 'dex': 3, 'int': 8}
    }
    weaponlist = {
		'broadsword': ['str', 0],
		'caber': ['str', 2],
		'nasty knife': ['dex', 0],
		'longbow': ['dex', 2],
		'magic orb': ['int', 0],
		'grimoire': ['int', 2]
    }

    def display(self):
        self.player = {'str': 0, 'int': 0, 'dex': 0}
        feet_symbol = "'"
        inch_symbol = '"'
        while 1:
            self.local_header()
            ans = input(f"Enemy: ").lower()

            if ans not in self.enemylist: continue
            else:
                self.enemy = ans
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            ans = input(f"STR: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['str'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            ans = input(f"INT: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['int'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            ans = input(f"DEX: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['dex'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            ans = input(f"Height (Feet represented with an apostrophe and Inch represented with quotation marks. No Spaces. E.g, 5\'7\"): ").lower().replace(' ', '').replace('\"', '').split('\'')

            if not all(a.isdigit() for a in ans): continue
            else:
                self.player['height'] = [int(ans[0]), int(ans[1])]
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
            ans = input(f"Temperature (No need to type °C): ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['temperature'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
            print(f"Temperature: {self.player['temperature']}°C")
            ans = input(f"Gravity (Use dot `.` as a decimal point. No need to write m/s²): ").lower()

            if not ans.replace('.', '').isdigit(): continue
            else:
                self.player['gravity'] = float(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
            print(f"Temperature: {self.player['temperature']}°C")
            print(f"Gravity: {self.player['gravity']} m/s²")
            ans = input(f"Pressure (No need to write kPa): ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['pressure'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
            print(f"Temperature: {self.player['temperature']}°C")
            print(f"Gravity: {self.player['gravity']} m/s²")
            print(f"Pressure: {self.player['pressure']} kPa")
            ans = input(f"\nWeapons (Weapon list, separated by a comma space): ").lower().split(', ')

            if len(ans)!=3: continue
            elif not all(a in self.weaponlist for a in ans): continue
            else:
                self.player['weapons'] = ans
                break
        potion = False
        self.itemlist = {
            'balloon': self.player['gravity']<9.3 or (self.player['pressure']>110 and self.enemy!='eagle'),
            'battery': self.eg.batt<=1 and self.enemy not in ['golem', 'wizard'],
            'bellows': (self.enemy in ['dragon', 'eagle'] and self.player['pressure']>105) or (self.enemy not in ['dragon', 'eagle'] and self.player['pressure']<95),
            'cheat code': False,
            'crystal ball': self.player['int']>int(self.eg.sndigit[-1]) and self.enemy!='wizard',
            'feather': self.player['dex']>self.player['str'] or self.player['dex']>self.player['int'],
            'hard drive': any([a for b in self.eg.ports for a in b].count(x)>=2 for x in self.eg.uniqueports),
            'lamp': self.player['temperature']<12 and self.enemy!='lizard',
            'moonstone': len(self.eg.unlitind)>=2,
            'potion': True,
            'small dog': self.enemy not in ['demon', 'dragon', 'troll'],
            'stepladder': self.player['height'][0]<4 and self.enemy not in ['goblin', 'lizard'],
            'sunstone': len(self.eg.litind)>=2,
            'symbol': self.enemy in ['demon', 'golem'] or self.player['temperature']>31,
            'ticket': (self.player['height'][0]>4 or (self.player['height'][0]==4 and self.player['height'][1]>=6)) and (self.player['gravity']>=9.2 and self.player['gravity']<=10.4),
            'trophy': self.player['str']>int(self.eg.sndigit[0]) or self.enemy=='troll'
        }

        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            print(f"DEX: {self.player['dex']}")
            print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
            print(f"Temperature: {self.player['temperature']}°C")
            print(f"Gravity: {self.player['gravity']} m/s²")
            print(f"Pressure: {self.player['pressure']} kPa")
            print(f"\nWeapons: {', '.join(self.player['weapons'])}")
            ans = input(f"Items (Item list, include everything. Each item are separated by a comma space): ").lower().split(', ')

            if len(ans)!=(5 if not potion else 4): continue
            elif not all(a in self.itemlist for a in ans): continue
            else:
                if 'potion' in ans:
                    potion = True
                    self.repotion()
                    ans.remove('potion')
                self.player['items'] = ans
                break
    
    def repotion(self):
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            ans = input(f"STR: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['str'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            ans = input(f"INT: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['int'] = int(ans)
                break
        
        while 1:
            self.local_header()
            print(f"{self.enemy.capitalize()}\n")
            print(f"STR: {self.player['str']}")
            print(f"INT: {self.player['int']}")
            ans = input(f"DEX: ").lower()

            if not ans.isdigit(): continue
            else:
                self.player['dex'] = int(ans)
                break

    def _calculate(self):
        items_to_use = []; weapon_to_use = []
        
        for a in self.player['items']:
            if self.itemlist[a]: items_to_use.append(a)
        
        for a in self.player['weapons']:
            weapon_to_use.append([a, (self.player[self.weaponlist[a][0]]+self.weaponlist[a][1])-self.enemylist[self.enemy][self.weaponlist[a][0]]])
        
        return items_to_use+[sorted(weapon_to_use, key=lambda x: x[1])[0][0]]

    def solve(self):
        feet_symbol = "'"
        inch_symbol = '"'
        sol = self._calculate()
        self.local_header()
        print(f"{self.enemy.capitalize()}\n")
        print(f"STR: {self.player['str']}")
        print(f"INT: {self.player['int']}")
        print(f"DEX: {self.player['dex']}")
        print(f"Height: {feet_symbol.join(map(str, self.player['height']))}{inch_symbol}")
        print(f"Temperature: {self.player['temperature']}°C")
        print(f"Gravity: {self.player['gravity']} m/s²")
        print(f"Pressure: {self.player['pressure']} kPa")
        print(f"\nWeapons: {', '.join(self.player['weapons'])}")
        print(f"Items: {', '.join(map(lambda a: a.capitalize(), self.player['items']))}")
        print(f"{self.answer_pretext}Use: {', '.join(map(lambda a: a.capitalize(), sol))}")